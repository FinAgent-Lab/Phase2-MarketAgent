/**
 * API Service Layer
 * 
 * This module provides an abstraction layer for chat API calls.
 * It supports both OpenAI GPT and Dify API endpoints.
 * 
 * To switch providers, just change the API_PROVIDER constant or set it via environment variable.
 */

// API Provider: 'openai' or 'dify'
const API_PROVIDER = import.meta.env.VITE_API_PROVIDER || 'openai';

// API Configuration
const config = {
  openai: {
    baseUrl: import.meta.env.VITE_OPENAI_BASE_URL || 'https://api.openai.com/v1',
    apiKey: import.meta.env.VITE_OPENAI_API_KEY || '',
    model: import.meta.env.VITE_OPENAI_MODEL || 'gpt-4o-mini',
  },
  dify: {
    // Use proxy in development to avoid CORS issues
    baseUrl: import.meta.env.DEV ? '/api/dify' : (import.meta.env.VITE_DIFY_BASE_URL || 'https://api.dify.ai/v1'),
    apiKey: import.meta.env.VITE_DIFY_API_KEY || '',
  },
};

/**
 * Sends a chat message to OpenAI API
 * @param {Array} messages - Array of message objects with role and content
 * @param {AbortSignal} signal - Optional abort signal for cancellation
 * @returns {Promise<string>} - The assistant's response
 */
async function sendToOpenAI(messages, signal) {
  // Check if using OpenRouter (for additional headers)
  const isOpenRouter = config.openai.baseUrl.includes('openrouter.ai');
  
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${config.openai.apiKey}`,
  };

  // OpenRouter requires/recommends additional headers
  if (isOpenRouter) {
    headers['HTTP-Referer'] = window.location.origin;
    headers['X-Title'] = 'FinAgent Market';
  }

  const response = await fetch(`${config.openai.baseUrl}/chat/completions`, {
    method: 'POST',
    headers,
    body: JSON.stringify({
      model: config.openai.model,
      messages: messages.map(msg => ({
        role: msg.role,
        content: msg.content,
      })),
    }),
    signal,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.error?.message || `API Error: ${response.status}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

/**
 * Sends a chat message to Dify API (Streaming mode)
 * @param {Array} messages - Array of message objects with role and content
 * @param {string} conversationId - Optional conversation ID for multi-turn
 * @param {AbortSignal} signal - Optional abort signal for cancellation
 * @param {Function} onChunk - Callback for each streamed chunk (for real-time UI updates)
 * @returns {Promise<{answer: string, conversationId: string}>} - Response with answer and conversation ID
 */
async function sendToDify(messages, conversationId, signal, onChunk) {
  // Dify uses the last user message as query
  const lastUserMessage = [...messages].reverse().find(m => m.role === 'user');
  
  const response = await fetch(`${config.dify.baseUrl}/chat-messages`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${config.dify.apiKey}`,
    },
    body: JSON.stringify({
      inputs: {},
      query: lastUserMessage?.content || '',
      response_mode: 'streaming',
      conversation_id: conversationId || '',
      user: 'user',
    }),
    signal,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.message || `API Error: ${response.status}`);
  }

  // Parse SSE stream
  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let answer = '';
  let resultConversationId = conversationId || '';

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value, { stream: true });
    const lines = chunk.split('\n');

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const jsonStr = line.slice(6);
        if (jsonStr.trim() === '') continue;
        
        try {
          const data = JSON.parse(jsonStr);
          
          // Handle different event types
          if (data.event === 'message' || data.event === 'agent_message') {
            answer += data.answer || '';
            if (data.conversation_id) {
              resultConversationId = data.conversation_id;
            }
            // Call onChunk callback for real-time UI updates
            if (onChunk) {
              onChunk(answer, resultConversationId);
            }
          } else if (data.event === 'message_end') {
            if (data.conversation_id) {
              resultConversationId = data.conversation_id;
            }
          } else if (data.event === 'error') {
            throw new Error(data.message || 'Dify API Error');
          }
        } catch (e) {
          // Skip invalid JSON lines
          if (e.message !== 'Dify API Error') continue;
          throw e;
        }
      }
    }
  }

  return {
    answer: answer.trim(),
    conversationId: resultConversationId,
  };
}

/**
 * Unified chat API function
 * Automatically routes to the correct provider based on configuration
 * 
 * @param {Array} messages - Array of message objects with role and content
 * @param {Object} options - Optional parameters
 * @param {string} options.conversationId - Conversation ID (used by Dify)
 * @param {AbortSignal} options.signal - Abort signal for cancellation
 * @param {Function} options.onChunk - Callback for streaming chunks (real-time UI updates)
 * @returns {Promise<{answer: string, conversationId?: string}>}
 */
export async function sendChatMessage(messages, options = {}) {
  const { conversationId, signal, onChunk } = options;

  try {
    if (API_PROVIDER === 'dify') {
      return await sendToDify(messages, conversationId, signal, onChunk);
    } else {
      const answer = await sendToOpenAI(messages, signal);
      return { answer };
    }
  } catch (error) {
    if (error.name === 'AbortError') {
      throw new Error('요청이 취소되었습니다.');
    }
    throw error;
  }
}

/**
 * Get current API provider
 * @returns {string} - Current provider name
 */
export function getProvider() {
  return API_PROVIDER;
}

/**
 * Check if API is configured
 * @returns {boolean}
 */
export function isConfigured() {
  if (API_PROVIDER === 'dify') {
    return !!config.dify.apiKey;
  }
  return !!config.openai.apiKey;
}


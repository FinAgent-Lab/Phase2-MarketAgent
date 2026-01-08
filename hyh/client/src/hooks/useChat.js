import { useState, useCallback, useRef } from 'react';
import { sendChatMessage, getProvider } from '../services/api';

/**
 * Custom hook for managing chat state and interactions
 */
export function useChat() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [conversationId, setConversationId] = useState(null);
  const abortControllerRef = useRef(null);

  /**
   * Generate a unique message ID
   */
  const generateId = () => `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;

  /**
   * Send a message and get AI response
   */
  const sendMessage = useCallback(async (content) => {
    if (!content.trim() || isLoading) return;

    // Create user message
    const userMessage = {
      id: generateId(),
      role: 'user',
      content: content.trim(),
      timestamp: new Date().toISOString(),
    };

    // Add user message to state
    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    // Create abort controller for this request
    abortControllerRef.current = new AbortController();

    try {
      // Build messages array for API
      const apiMessages = [...messages, userMessage].map(msg => ({
        role: msg.role,
        content: msg.content,
      }));

      // Add system message if it's the first message
      if (apiMessages.length === 1) {
        apiMessages.unshift({
          role: 'system',
          content: '당신은 FinAgent, 금융 시장 분석을 도와주는 AI 어시스턴트입니다. 친절하고 전문적으로 답변해주세요.',
        });
      }

      // Send to API
      const response = await sendChatMessage(apiMessages, {
        conversationId,
        signal: abortControllerRef.current.signal,
      });

      // Update conversation ID if returned (Dify)
      if (response.conversationId) {
        setConversationId(response.conversationId);
      }

      // Create assistant message
      const assistantMessage = {
        id: generateId(),
        role: 'assistant',
        content: response.answer,
        timestamp: new Date().toISOString(),
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (err) {
      setError(err.message);
      console.error('Chat error:', err);
    } finally {
      setIsLoading(false);
      abortControllerRef.current = null;
    }
  }, [messages, isLoading, conversationId]);

  /**
   * Cancel the current request
   */
  const cancelRequest = useCallback(() => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
      abortControllerRef.current = null;
      setIsLoading(false);
    }
  }, []);

  /**
   * Clear all messages and start new conversation
   */
  const clearMessages = useCallback(() => {
    setMessages([]);
    setConversationId(null);
    setError(null);
  }, []);

  /**
   * Retry the last failed message
   */
  const retryLastMessage = useCallback(async () => {
    if (messages.length === 0) return;
    
    const lastUserMessage = [...messages].reverse().find(m => m.role === 'user');
    if (!lastUserMessage) return;

    // Remove the last user message and retry
    setMessages(prev => prev.filter(m => m.id !== lastUserMessage.id));
    await sendMessage(lastUserMessage.content);
  }, [messages, sendMessage]);

  return {
    messages,
    isLoading,
    error,
    conversationId,
    provider: getProvider(),
    sendMessage,
    cancelRequest,
    clearMessages,
    retryLastMessage,
  };
}



import { useState, useCallback } from 'react';
import { Sidebar } from './components/Sidebar';
import { ChatArea } from './components/ChatArea';
import { useChat } from './hooks/useChat';
import './App.css';

function App() {
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
  const [conversations, setConversations] = useState([]);
  const [currentConversationId, setCurrentConversationId] = useState(null);

  const { 
    messages, 
    isLoading, 
    error, 
    sendMessage, 
    cancelRequest, 
    clearMessages,
    retryLastMessage 
  } = useChat();

  const handleNewChat = useCallback(() => {
    clearMessages();
    setCurrentConversationId(null);
  }, [clearMessages]);

  const handleSelectConversation = useCallback((id) => {
    setCurrentConversationId(id);
    // TODO: Load conversation messages from storage
  }, []);

  const handleRefresh = useCallback(async () => {
    // TODO: Refresh conversation list from storage/API
    return new Promise(resolve => setTimeout(resolve, 500));
  }, []);

  const handleSendMessage = useCallback(async (content) => {
    await sendMessage(content);
    
    // Save conversation title from first message
    if (messages.length === 0 && content.trim()) {
      const newConv = {
        id: `conv_${Date.now()}`,
        title: content.slice(0, 30) + (content.length > 30 ? '...' : ''),
        createdAt: new Date().toISOString(),
      };
      setConversations(prev => [newConv, ...prev]);
      setCurrentConversationId(newConv.id);
    }
  }, [sendMessage, messages.length]);

  return (
    <div className="app">
      <Sidebar
        conversations={conversations}
        currentConversationId={currentConversationId}
        onNewChat={handleNewChat}
        onSelectConversation={handleSelectConversation}
        onRefresh={handleRefresh}
        isCollapsed={isSidebarCollapsed}
        onToggleCollapse={() => setIsSidebarCollapsed(prev => !prev)}
      />
      <ChatArea
        messages={messages}
        isLoading={isLoading}
        error={error}
        onSendMessage={handleSendMessage}
        onCancelRequest={cancelRequest}
        onRetry={retryLastMessage}
      />
    </div>
  );
}

export default App;

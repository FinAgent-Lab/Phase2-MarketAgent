import { useRef, useEffect } from 'react';
import { MessageBubble } from './MessageBubble';
import { ChatInput } from './ChatInput';
import './ChatArea.css';

export function ChatArea({ 
  messages, 
  isLoading, 
  error, 
  onSendMessage, 
  onCancelRequest,
  onRetry 
}) {
  const messagesEndRef = useRef(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  const isEmpty = messages.length === 0;

  return (
    <main className="chat-area">
      <header className="chat-area__header">
        <h1 className="chat-area__title">FinAgent_Market</h1>
        <button className="chat-area__settings-btn" aria-label="설정">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="12" cy="12" r="3"/>
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>
          </svg>
        </button>
      </header>

      <div className="chat-area__messages">
        {isEmpty ? (
          <div className="chat-area__empty">
            <h2 className="chat-area__empty-title">어디서부터 시작할까요?</h2>
            <p className="chat-area__empty-description">
              금융 시장에 대한 질문을 해보세요. 주식, 채권, 경제 지표 등 다양한 주제에 대해 도움을 드릴 수 있습니다.
            </p>
            <div className="chat-area__suggestions">
              <button 
                className="chat-area__suggestion"
                onClick={() => onSendMessage('오늘 주요 경제 뉴스가 뭐야?')}
              >
                오늘 주요 경제 뉴스가 뭐야?
              </button>
              <button 
                className="chat-area__suggestion"
                onClick={() => onSendMessage('미국 금리 전망 분석해줘')}
              >
                미국 금리 전망 분석해줘
              </button>
              <button 
                className="chat-area__suggestion"
                onClick={() => onSendMessage('삼성전자 주가 분석 부탁해')}
              >
                삼성전자 주가 분석 부탁해
              </button>
            </div>
          </div>
        ) : (
          <>
            {messages.map((message) => (
              <MessageBubble key={message.id} message={message} />
            ))}
            
            {isLoading && (
              <div className="chat-area__loading">
                <div className="chat-area__loading-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
                <button 
                  className="chat-area__cancel-btn"
                  onClick={onCancelRequest}
                >
                  취소
                </button>
              </div>
            )}

            {error && (
              <div className="chat-area__error">
                <p className="chat-area__error-message">{error}</p>
                <button 
                  className="chat-area__retry-btn"
                  onClick={onRetry}
                >
                  다시 시도
                </button>
              </div>
            )}
          </>
        )}
        <div ref={messagesEndRef} />
      </div>

      <ChatInput 
        onSend={onSendMessage} 
        disabled={isLoading} 
      />
    </main>
  );
}



import { useState } from 'react';
import './Sidebar.css';

export function Sidebar({ 
  conversations, 
  currentConversationId, 
  onNewChat, 
  onSelectConversation,
  onRefresh,
  isCollapsed,
  onToggleCollapse 
}) {
  const [isRefreshing, setIsRefreshing] = useState(false);

  const handleRefresh = async () => {
    setIsRefreshing(true);
    await onRefresh?.();
    setTimeout(() => setIsRefreshing(false), 500);
  };

  return (
    <aside className={`sidebar ${isCollapsed ? 'sidebar--collapsed' : ''}`}>
      <div className="sidebar__header">
        <button 
          className="sidebar__new-chat-btn"
          onClick={onNewChat}
          aria-label="새 채팅 시작"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <line x1="12" y1="8" x2="12" y2="16"/>
            <line x1="8" y1="12" x2="16" y2="12"/>
          </svg>
          <span className="sidebar__new-chat-text">새 채팅</span>
        </button>
        <button 
          className="sidebar__toggle-btn"
          onClick={onToggleCollapse}
          aria-label={isCollapsed ? '사이드바 펼치기' : '사이드바 접기'}
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <polyline points={isCollapsed ? "9 18 15 12 9 6" : "15 18 9 12 15 6"}/>
          </svg>
        </button>
      </div>

      <div className="sidebar__content">
        <div className="sidebar__section">
          <div className="sidebar__section-header">
            <span className="sidebar__section-title">최근 대화</span>
            <button 
              className={`sidebar__refresh-btn ${isRefreshing ? 'sidebar__refresh-btn--spinning' : ''}`}
              onClick={handleRefresh}
              aria-label="대화 목록 새로고침"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="23 4 23 10 17 10"/>
                <polyline points="1 20 1 14 7 14"/>
                <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>
              </svg>
            </button>
          </div>
          
          <div className="sidebar__conversation-list">
            {conversations.length === 0 ? (
              <p className="sidebar__empty-text">아직 대화가 없습니다</p>
            ) : (
              conversations.map(conv => (
                <button
                  key={conv.id}
                  className={`sidebar__conversation-item ${conv.id === currentConversationId ? 'sidebar__conversation-item--active' : ''}`}
                  onClick={() => onSelectConversation(conv.id)}
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                  </svg>
                  <span className="sidebar__conversation-title">{conv.title}</span>
                </button>
              ))
            )}
          </div>
        </div>
      </div>

      <div className="sidebar__footer">
        <div className="sidebar__user">
          <div className="sidebar__user-avatar">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
          </div>
          <span className="sidebar__user-name">FinAgent</span>
        </div>
      </div>
    </aside>
  );
}


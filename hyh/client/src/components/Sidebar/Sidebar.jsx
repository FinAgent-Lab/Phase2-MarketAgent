import { useState } from 'react';
import './Sidebar.css';

export function Sidebar({ 
  conversations, 
  currentConversationId, 
  onNewChat, 
  onSelectConversation,
  onRefresh,
  isCollapsed,
  onToggleCollapse,
  activeTab,
  onTabChange
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
          className="sidebar__toggle-btn"
          onClick={onToggleCollapse}
          aria-label={isCollapsed ? '사이드바 펼치기' : '사이드바 접기'}
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <polyline points={isCollapsed ? "9 18 15 12 9 6" : "15 18 9 12 15 6"}/>
          </svg>
        </button>
      </div>

      {/* Tab Navigation */}
      <div className="sidebar__tabs">
        <button
          className={`sidebar__tab ${activeTab === 'chat' ? 'sidebar__tab--active' : ''}`}
          onClick={() => onTabChange?.('chat')}
          aria-label="시황 분석"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
          </svg>
          <span className="sidebar__tab-text">시황 분석</span>
        </button>
        <button
          className={`sidebar__tab ${activeTab === 'recommend' ? 'sidebar__tab--active' : ''}`}
          onClick={() => onTabChange?.('recommend')}
          aria-label="개인 맞춤 추천"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
          </svg>
          <span className="sidebar__tab-text">개인 맞춤 추천</span>
        </button>
        <button
          className={`sidebar__tab ${activeTab === 'report' ? 'sidebar__tab--active' : ''}`}
          onClick={() => onTabChange?.('report')}
          aria-label="Daily Report"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14,2 14,8 20,8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
          </svg>
          <span className="sidebar__tab-text">Daily Report</span>
        </button>
      </div>

      <div className="sidebar__content">
        {activeTab === 'chat' && (
          <>
            <div className="sidebar__action-row">
              <button 
                className="sidebar__new-chat-btn"
                onClick={onNewChat}
                aria-label="새 채팅 시작"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <line x1="12" y1="8" x2="12" y2="16"/>
                  <line x1="8" y1="12" x2="16" y2="12"/>
                </svg>
                <span className="sidebar__new-chat-text">새 채팅</span>
              </button>
            </div>
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
          </>
        )}

        {activeTab === 'recommend' && (
          <div className="sidebar__section">
            <div className="sidebar__report-info">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
                <line x1="12" y1="17" x2="12.01" y2="17"/>
              </svg>
              <p className="sidebar__report-text">
                개인화된 투자 추천을 받아보세요.
              </p>
            </div>
          </div>
        )}

        {activeTab === 'report' && (
          <div className="sidebar__section">
            <div className="sidebar__report-info">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                <line x1="16" y1="2" x2="16" y2="6"/>
                <line x1="8" y1="2" x2="8" y2="6"/>
                <line x1="3" y1="10" x2="21" y2="10"/>
              </svg>
              <p className="sidebar__report-text">
                캘린더에서 날짜를 선택하면 해당 날짜의 데일리 리포트를 볼 수 있습니다.
              </p>
            </div>
          </div>
        )}
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



import './PersonalRecommend.css';

export function PersonalRecommend() {
  return (
    <div className="personal-recommend">
      <div className="personal-recommend__header">
        <h1 className="personal-recommend__title">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
          </svg>
          개인 맞춤 추천
        </h1>
        <span className="personal-recommend__divider">|</span>
        <span className="personal-recommend__subtitle">나만을 위한 투자 인사이트</span>
      </div>

      <div className="personal-recommend__content">
        <div className="personal-recommend__placeholder">
          <div className="personal-recommend__icon-wrapper">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
              <line x1="12" y1="17" x2="12.01" y2="17"/>
            </svg>
          </div>
          <h2 className="personal-recommend__placeholder-title">준비 중입니다</h2>
          <p className="personal-recommend__placeholder-text">
            개인화된 투자 추천 기능이 곧 제공될 예정입니다.<br />
            사용자의 투자 성향과 관심사를 기반으로<br />
            맞춤형 인사이트를 제공해 드립니다.
          </p>
          <div className="personal-recommend__features">
            <div className="personal-recommend__feature">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
              </svg>
              <span>포트폴리오 분석</span>
            </div>
            <div className="personal-recommend__feature">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                <path d="M2 17l10 5 10-5"/>
                <path d="M2 12l10 5 10-5"/>
              </svg>
              <span>맞춤형 종목 추천</span>
            </div>
            <div className="personal-recommend__feature">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
              <span>실시간 알림</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

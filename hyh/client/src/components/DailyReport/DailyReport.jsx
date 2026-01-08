import { useState, useEffect, useCallback } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import './DailyReport.css';

const GITHUB_RAW_BASE_URL = 'https://raw.githubusercontent.com/FinAgent-Lab/Phase2-MarketAgent/reports/hsy/daily_reports';

function formatDate(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

function getDaysInMonth(year, month) {
  return new Date(year, month + 1, 0).getDate();
}

function getFirstDayOfMonth(year, month) {
  return new Date(year, month, 1).getDay();
}

function getYesterday() {
  const today = new Date();
  return new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1);
}

export function DailyReport() {
  const [selectedDate, setSelectedDate] = useState(getYesterday);
  const [currentMonth, setCurrentMonth] = useState(getYesterday);
  const [markdown, setMarkdown] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [isCalendarOpen, setIsCalendarOpen] = useState(false);

  const fetchReport = useCallback(async (date) => {
    const dateStr = formatDate(date);
    const url = `${GITHUB_RAW_BASE_URL}/daily_report_${dateStr}.md`;
    
    setIsLoading(true);
    setError(null);
    setMarkdown('');

    try {
      const response = await fetch(url);
      if (!response.ok) {
        if (response.status === 404) {
          throw new Error(`${dateStr} 날짜의 리포트가 없습니다.`);
        }
        throw new Error(`리포트를 불러오는데 실패했습니다. (${response.status})`);
      }
      const text = await response.text();
      setMarkdown(text);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchReport(selectedDate);
  }, [selectedDate, fetchReport]);

  const handleDateClick = (day) => {
    const newDate = new Date(currentMonth.getFullYear(), currentMonth.getMonth(), day);
    setSelectedDate(newDate);
    setIsCalendarOpen(false);
  };

  const handlePrevMonth = () => {
    setCurrentMonth(prev => new Date(prev.getFullYear(), prev.getMonth() - 1, 1));
  };

  const handleNextMonth = () => {
    setCurrentMonth(prev => new Date(prev.getFullYear(), prev.getMonth() + 1, 1));
  };

  const handleYesterday = () => {
    const yesterday = getYesterday();
    setCurrentMonth(yesterday);
    setSelectedDate(yesterday);
  };

  const renderCalendar = () => {
    const year = currentMonth.getFullYear();
    const month = currentMonth.getMonth();
    const daysInMonth = getDaysInMonth(year, month);
    const firstDay = getFirstDayOfMonth(year, month);
    
    const days = [];
    const weekdays = ['일', '월', '화', '수', '목', '금', '토'];
    
    // Weekday headers
    weekdays.forEach((day, idx) => {
      days.push(
        <div key={`header-${idx}`} className="calendar__weekday">
          {day}
        </div>
      );
    });
    
    // Empty cells before first day
    for (let i = 0; i < firstDay; i++) {
      days.push(<div key={`empty-${i}`} className="calendar__day calendar__day--empty" />);
    }
    
    // Days of month
    const yesterday = getYesterday();
    const selectedDateStr = formatDate(selectedDate);
    
    for (let day = 1; day <= daysInMonth; day++) {
      const currentDate = new Date(year, month, day);
      const dateStr = formatDate(currentDate);
      const isYesterday = formatDate(yesterday) === dateStr;
      const isSelected = selectedDateStr === dateStr;
      // 오늘과 미래 날짜는 비활성화 (리포트는 전날까지만 존재)
      const isUnavailable = currentDate > yesterday;
      
      days.push(
        <button
          key={day}
          className={`calendar__day ${isYesterday ? 'calendar__day--latest' : ''} ${isSelected ? 'calendar__day--selected' : ''} ${isUnavailable ? 'calendar__day--future' : ''}`}
          onClick={() => !isUnavailable && handleDateClick(day)}
          disabled={isUnavailable}
        >
          {day}
        </button>
      );
    }
    
    return days;
  };

  const monthNames = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'];

  return (
    <div className="daily-report">
      <div className="daily-report__header">
        <div className="daily-report__header-left">
          <h1 className="daily-report__title">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
              <polyline points="14,2 14,8 20,8"/>
              <line x1="16" y1="13" x2="8" y2="13"/>
              <line x1="16" y1="17" x2="8" y2="17"/>
            </svg>
            Daily Report
          </h1>
          <span className="daily-report__divider">|</span>
          <span className="daily-report__subtitle">글로벌 거시경제 데일리 리포트</span>
        </div>
        
        <div className="daily-report__date-picker">
          <button 
            className={`daily-report__date-btn ${isCalendarOpen ? 'daily-report__date-btn--active' : ''}`}
            onClick={() => setIsCalendarOpen(prev => !prev)}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
              <line x1="16" y1="2" x2="16" y2="6"/>
              <line x1="8" y1="2" x2="8" y2="6"/>
              <line x1="3" y1="10" x2="21" y2="10"/>
            </svg>
            <span>{formatDate(selectedDate)}</span>
            <svg 
              width="14" 
              height="14" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              strokeWidth="2" 
              strokeLinecap="round" 
              strokeLinejoin="round"
              className={`daily-report__chevron ${isCalendarOpen ? 'daily-report__chevron--open' : ''}`}
            >
              <polyline points="6,9 12,15 18,9"/>
            </svg>
          </button>
          
          {isCalendarOpen && (
            <div className="calendar">
              <div className="calendar__notice">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <line x1="12" y1="16" x2="12" y2="12"/>
                  <line x1="12" y1="8" x2="12.01" y2="8"/>
                </svg>
                <span>매일 아침, 전날까지의 리포트가 발행됩니다</span>
              </div>
              <div className="calendar__header">
                <button className="calendar__nav-btn" onClick={handlePrevMonth}>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="15,18 9,12 15,6"/>
                  </svg>
                </button>
                <div className="calendar__title">
                  <span className="calendar__year">{currentMonth.getFullYear()}년</span>
                  <span className="calendar__month">{monthNames[currentMonth.getMonth()]}</span>
                </div>
                <button className="calendar__nav-btn" onClick={handleNextMonth}>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="9,18 15,12 9,6"/>
                  </svg>
                </button>
                <button className="calendar__today-btn" onClick={handleYesterday}>
                  최신
                </button>
              </div>
              <div className="calendar__grid">
                {renderCalendar()}
              </div>
            </div>
          )}
        </div>
      </div>

      <div className="daily-report__content">
        {isLoading && (
          <div className="daily-report__loading">
            <div className="daily-report__spinner" />
            <span>리포트를 불러오는 중...</span>
          </div>
        )}
        
        {error && (
          <div className="daily-report__error">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <line x1="12" y1="8" x2="12" y2="12"/>
              <line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
            <p>{error}</p>
            <button className="daily-report__retry-btn" onClick={() => fetchReport(selectedDate)}>
              다시 시도
            </button>
          </div>
        )}
        
        {!isLoading && !error && markdown && (
          <article className="daily-report__markdown">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
              {markdown}
            </ReactMarkdown>
          </article>
        )}
      </div>
    </div>
  );
}

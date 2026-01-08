import './MessageBubble.css';

export function MessageBubble({ message }) {
  const isUser = message.role === 'user';
  const isStreaming = message.isStreaming;
  const timestamp = new Date(message.timestamp).toLocaleTimeString('ko-KR', {
    hour: '2-digit',
    minute: '2-digit',
  });

  return (
    <div className={`message ${isUser ? 'message--user' : 'message--assistant'} ${isStreaming ? 'message--streaming' : ''}`}>
      {!isUser && (
        <div className="message__avatar">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M12 2L2 7l10 5 10-5-10-5z"/>
            <path d="M2 17l10 5 10-5"/>
            <path d="M2 12l10 5 10-5"/>
          </svg>
        </div>
      )}
      <div className="message__content-wrapper">
        <div className="message__bubble">
          <p className="message__content">
            {message.content}
            {isStreaming && <span className="message__cursor">▌</span>}
          </p>
        </div>
        {!isStreaming && <span className="message__timestamp">{timestamp}</span>}
      </div>
    </div>
  );
}



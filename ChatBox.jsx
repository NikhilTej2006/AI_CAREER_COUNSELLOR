import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./ChatBox.css";

function ChatBox() {
  const [input, setInput] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat, loading]);

  const formatMessage = (text) => {
    return {
      __html: text
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>')
        .replace(/\n/g, "<br>"),
    };
  };

  const sendMessage = async () => {
    if (!input.trim()) return;

    setChat((prev) => [...prev, { sender: "user", message: input }]);
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:5000/get-career", {
        message: input,
      });
      setChat((prev) => [...prev, { sender: "ai", message: res.data.reply }]);
    } catch {
      setChat((prev) => [
        ...prev,
        { sender: "ai", message: "Oops! Something went wrong." },
      ]);
    } finally {
      setInput("");
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="chat-wrapper">
      <div className="chat-header">🚀 Career Compass AI</div>

      <div className="chat-window">
        {chat.map((msg, i) => (
          <div key={i} className={`chat-bubble ${msg.sender}`}>
            <div className="avatar">{msg.sender === "user" ? "🧑" : "🤖"}</div>
            <div
              className="bubble-text"
              dangerouslySetInnerHTML={
                msg.sender === "ai"
                  ? formatMessage(msg.message)
                  : { __html: msg.message }
              }
            />
          </div>
        ))}

        {loading && (
          <div className="chat-bubble ai">
            <div className="avatar">🤖</div>
            <div className="typing">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}

        <div ref={bottomRef} />
      </div>

      <div className="input-row">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your interests (e.g., AI, gaming, finance)..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default ChatBox;

import React from "react";
import ChatBox from "./components/ChatBox";
import "./App.css";

function App() {
  return (
    <div className="app-wrapper">
      <header className="hero-section">
        <h1>🚀 Career Compass</h1>
        <div className="tagline-card">
          <h2>🌟 Discover Your Dream Career</h2>
          <p>
            Just type in your passions — like gaming, cooking, design, or tech — and let our AI
            guide you through career paths uniquely suited to your interests.
          </p>
        </div>
      </header>

      <div className="chatbox-area">
        <ChatBox />
      </div>
    </div>
  );
}

export default App;

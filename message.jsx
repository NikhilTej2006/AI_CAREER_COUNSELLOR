import React from 'react';
// import "./message.css";

const Message = ({sender,text}) => {
return (
<div className={`message ${sender === "user" ? "user" : "bot"}`}>
    <div className="bubble">
        <strong>{sender === "user" ? "You": "counselor"}</strong> {text}
    </div>
</div>
);
};

export default Message;
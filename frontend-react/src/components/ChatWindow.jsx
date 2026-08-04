import React from "react";
import "./ChatWindow.css";

const ChatWindow = ({ messages = [], loading }) => {

  return (
    <div className="chat-container">

      <div className="messages">

        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${
              msg.role === "user"
                ? "user-message"
                : "bot-message"
            }`}
          >

            <div className="message-content">
              <b>
                {msg.role === "user"
                  ? "You"
                  : "OmniAssistAI"}
              </b>

              <p>{msg.content}</p>
            </div>

          </div>
        ))}


        {loading && (
          <div className="message bot-message">
            <div className="message-content">
              <b>OmniAssistAI</b>
              <p>Thinking...</p>
            </div>
          </div>
        )}

      </div>

    </div>
  );
};


export default ChatWindow;
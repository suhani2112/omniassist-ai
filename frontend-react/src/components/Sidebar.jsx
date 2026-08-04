import React from "react";
import "./Sidebar.css";


function Sidebar({
  chats,
  activeChat,
  setActiveChat,
  newChat
}) {


  return (

    <div className="sidebar">


      <div className="sidebar-header">

        <h2>
          OmniAssistAI
        </h2>


        <button
          className="new-chat-btn"
          onClick={newChat}
        >
          + New Chat
        </button>

      </div>



      <div className="chat-list">


        {
          chats.length === 0 ? (

            <p className="empty-chat">
              No chats yet
            </p>

          ) : (

            chats.map((chat,index)=>(

              <div
                key={index}
                className={
                  activeChat === index
                  ? "chat-item active"
                  : "chat-item"
                }
                onClick={()=>{
                  setActiveChat(index);
                }}
              >

                💬

                <span>
                  {
                    chat.title ||
                    `Chat ${index+1}`
                  }
                </span>


              </div>

            ))

          )


        }


      </div>



      <div className="sidebar-footer">

        <p>
          🤖 OmniAssistAI
        </p>

      </div>


    </div>

  );

}


export default Sidebar;
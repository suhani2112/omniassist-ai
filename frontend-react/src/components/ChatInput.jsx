import { useState } from "react";


function ChatInput({ onSend }) {

  const [message, setMessage] = useState("");


  const handleSend = () => {

    if (!message.trim()) return;

    onSend(message);

    setMessage("");

  };


  return (

    <div className="border-t border-gray-700 bg-gray-800 p-4">

      <div className="flex gap-3">


        <input
          type="text"
          placeholder="Ask anything..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleSend();
            }
          }}
          className="
            flex-1
            rounded-xl
            border
            border-gray-600
            bg-gray-700
            p-4
            text-white
            outline-none
            focus:border-blue-500
          "
        />


        <button
          onClick={handleSend}
          className="
            rounded-xl
            bg-blue-600
            px-6
            text-white
            hover:bg-blue-700
          "
        >
          Send
        </button>


      </div>

    </div>

  );

}


export default ChatInput;
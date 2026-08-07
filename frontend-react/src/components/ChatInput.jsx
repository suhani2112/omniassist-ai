import { useState } from "react";


function ChatInput({ onSend }) {

  const [message,setMessage] = useState("");


  const handleSend = () => {

    if(!message.trim()) return;


    onSend(message);

    setMessage("");

  };



  return (

    <div
      className="
      p-5
      bg-gray-900
      border-t
      border-gray-700
      "
    >


      <div
        className="
        flex
        items-center
        gap-3
        rounded-2xl
        bg-gray-800
        border
        border-gray-700
        px-4
        py-3
        shadow-xl
        "
      >


        <input

          type="text"

          placeholder="Ask anything about your documents..."

          value={message}

          onChange={(e)=>setMessage(e.target.value)}

          onKeyDown={(e)=>{

            if(e.key==="Enter")
            {
              handleSend();
            }

          }}

          className="
          flex-1
          bg-transparent
          text-white
          placeholder-gray-500
          outline-none
          px-3
          "
        />



        <button

          onClick={handleSend}

          className="
          rounded-xl
          bg-blue-600
          px-6
          py-3
          font-medium
          text-white
          transition
          hover:bg-blue-700
          hover:scale-105
          "
        >

          Send ➤

        </button>


      </div>



      <p
        className="
        mt-3
        text-center
        text-xs
        text-gray-500
        "
      >
        OmniAssistAI can answer using your uploaded PDFs
      </p>


    </div>

  );
}


export default ChatInput;
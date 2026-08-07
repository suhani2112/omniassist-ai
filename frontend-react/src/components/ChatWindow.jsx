import React, { useEffect, useRef } from "react";


const ChatWindow = ({
  messages = [],
  loading,
  activePDF
}) => {


  const bottomRef = useRef(null);



  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages, loading]);




  return (

    <div
      className="
      flex-1
      overflow-y-auto
      bg-gray-950
      p-6
      space-y-5
      "
    >



      {/* Active PDF Badge */}

      <div
        className="
        rounded-xl
        border
        border-gray-700
        bg-gray-900
        px-4
        py-3
        text-sm
        text-gray-300
        "
      >

        📄 Using document:

        <span
          className="
          ml-2
          font-medium
          text-white
          "
        >

          {
            activePDF
            ?
            activePDF
            :
            "No PDF selected"
          }

        </span>


      </div>







      {/* Empty State */}

      {
        messages.length === 0 &&

        <div
          className="
          flex
          h-full
          flex-col
          items-center
          justify-center
          text-center
          "
        >


          <div
            className="
            mb-4
            text-6xl
            "
          >
            🤖
          </div>



          <h2
            className="
            text-xl
            font-semibold
            text-white
            "
          >
            Welcome to OmniAssistAI
          </h2>



          <p
            className="
            mt-2
            text-gray-400
            "
          >
            Upload a PDF and ask questions from your documents
          </p>


        </div>

      }







      {/* Messages */}

      {
        messages.map((msg,index)=>(


          <div
            key={index}
            className={`
            flex

            ${
              msg.role === "user"
              ?
              "justify-end"
              :
              "justify-start"
            }

            `}
          >




            <div
              className={`
              max-w-[75%]
              rounded-2xl
              px-5
              py-4
              shadow-xl


              ${
                msg.role === "user"

                ?

                "bg-blue-600 text-white rounded-br-none"

                :

                "bg-gray-800 text-gray-100 rounded-bl-none"

              }

              `}
            >





              {/* Message Header */}

              <div
                className="
                mb-2
                flex
                items-center
                gap-2
                text-xs
                opacity-70
                "
              >

                {
                  msg.role === "user"

                  ?

                  <>
                    👤 You
                  </>

                  :

                  <>
                    🤖 OmniAssistAI
                  </>

                }


              </div>






              {/* Content */}

              <p
                className="
                whitespace-pre-wrap
                leading-relaxed
                "
              >

                {msg.content}

              </p>



            </div>




          </div>


        ))

      }








      {/* Loading State */}


      {
        loading &&


        <div
          className="
          flex
          justify-start
          "
        >


          <div
            className="
            flex
            items-center
            gap-3
            rounded-2xl
            bg-gray-800
            px-5
            py-4
            text-gray-300
            "
          >

            <span>
              🤖
            </span>


            <span>
              OmniAssistAI is thinking
            </span>


            <span
              className="
              animate-pulse
              "
            >
              ...
            </span>


          </div>


        </div>

      }





      <div ref={bottomRef}/>



    </div>

  );

};


export default ChatWindow;
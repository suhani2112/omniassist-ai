import { useState } from "react";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import { sendMessage } from "../services/api";


function Home() {


  const [chats, setChats] = useState([
    {
      title: "New Chat",
      messages: [
        {
          role: "assistant",
          content:
            "👋 Welcome to OmniAssistAI!\n\nAsk me anything about your PDFs, programming, AI, ML, or anything else.",
        },
      ],
    },
  ]);


  const [activeChat, setActiveChat] = useState(0);

  const [loading, setLoading] = useState(false);



  const currentMessages =
    chats[activeChat]?.messages || [];





  const createNewChat = () => {

    const newChat = {

      title: "New Chat",

      messages: [
        {
          role: "assistant",
          content:
            "👋 Welcome to OmniAssistAI!\n\nStart a new conversation.",
        },
      ],

    };


    setChats((prev) => [
      ...prev,
      newChat,
    ]);


    setActiveChat((prev) => prev + 1);

  };





  const handleSend = async (question) => {


    if (!question.trim()) return;



    // Add user message

    setChats((prev) => {

      const updated = [...prev];


      updated[activeChat] = {

        ...updated[activeChat],

        title:
          updated[activeChat].title === "New Chat"
            ? question.slice(0, 25)
            : updated[activeChat].title,


        messages: [

          ...updated[activeChat].messages,

          {
            role: "user",
            content: question,
          },

        ],

      };


      return updated;

    });



    setLoading(true);



    try {


      const answer = await sendMessage(question);



      // Add AI response

      setChats((prev) => {

        const updated = [...prev];


        updated[activeChat] = {

          ...updated[activeChat],

          messages: [

            ...updated[activeChat].messages,

            {
              role: "assistant",
              content: answer,
            },

          ],

        };


        return updated;

      });



    } catch (error) {


      console.error(
        "Chat Error:",
        error
      );



      setChats((prev) => {

        const updated = [...prev];


        updated[activeChat] = {

          ...updated[activeChat],

          messages: [

            ...updated[activeChat].messages,

            {
              role: "assistant",
              content:
                "❌ Unable to connect to backend.",
            },

          ],

        };


        return updated;

      });


    }



    setLoading(false);

  };






  return (

    <div className="flex h-screen">


      {/* Sidebar */}

      <Sidebar

        chats={chats}

        activeChat={activeChat}

        setActiveChat={setActiveChat}

        newChat={createNewChat}

      />



      {/* Main Content */}

      <div className="flex flex-1 flex-col">


        <Navbar />



        <ChatWindow

          messages={currentMessages}

          loading={loading}

        />



        <ChatInput

          onSend={handleSend}

        />


      </div>


    </div>

  );

}


export default Home;
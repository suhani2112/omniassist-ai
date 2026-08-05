import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import { sendMessage } from "../services/api";

function Home() {
  // -----------------------------
  // Load chats from LocalStorage
  // -----------------------------
  const [chats, setChats] = useState(() => {
    const savedChats = localStorage.getItem("omni_chats");

    if (savedChats) {
      return JSON.parse(savedChats);
    }

    return [
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
    ];
  });

  // -----------------------------
  // Load active chat
  // -----------------------------
  const [activeChat, setActiveChat] = useState(() => {
    const savedActive = localStorage.getItem("omni_active_chat");

    return savedActive ? Number(savedActive) : 0;
  });

  const [loading, setLoading] = useState(false);

  // -----------------------------
  // Save chats automatically
  // -----------------------------
  useEffect(() => {
    localStorage.setItem(
      "omni_chats",
      JSON.stringify(chats)
    );
  }, [chats]);

  // -----------------------------
  // Save active chat automatically
  // -----------------------------
  useEffect(() => {
    localStorage.setItem(
      "omni_active_chat",
      activeChat
    );
  }, [activeChat]);

  const currentMessages =
    chats[activeChat]?.messages || [];

  // -----------------------------
  // Create New Chat
  // -----------------------------
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

    setChats((prev) => [...prev, newChat]);

    setActiveChat(chats.length);
  };

  // -----------------------------
  // Send Message
  // -----------------------------
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
      console.error(error);

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
      <Sidebar
        chats={chats}
        activeChat={activeChat}
        setActiveChat={setActiveChat}
        newChat={createNewChat}
      />

      <div className="flex flex-1 flex-col">
        <Navbar />

        <ChatWindow
          messages={currentMessages}
          loading={loading}
        />

        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
}

export default Home;
import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import { sendMessage } from "../services/api";


function Home() {


  // ------------------------------------
  // Chats
  // ------------------------------------

  const [chats, setChats] = useState(() => {


    const saved = localStorage.getItem(
      "omni_chats"
    );


    if(saved){

      return JSON.parse(saved);

    }


    return [

      {

        title:"New Chat",

        messages:[

          {

            role:"assistant",

            content:
            "👋 Welcome to OmniAssistAI!\n\nUpload a PDF or ask me anything."

          }

        ]

      }

    ];


  });



  // ------------------------------------
  // Active Chat
  // ------------------------------------

  const [activeChat,setActiveChat] = useState(()=>{


    const saved =
    localStorage.getItem(
      "omni_active_chat"
    );


    return saved
    ?
    Number(saved)
    :
    0;


  });



  // ------------------------------------
  // Active PDF
  // ------------------------------------

  const [activePDF,setActivePDF] = useState("");



  // ------------------------------------
  // Loading
  // ------------------------------------

  const [loading,setLoading] =
  useState(false);



  // ------------------------------------
  // Refresh PDFs
  // ------------------------------------

  const [refreshPDFs,setRefreshPDFs] =
  useState(0);




  // ------------------------------------
  // Save Chats
  // ------------------------------------

  useEffect(()=>{


    localStorage.setItem(

      "omni_chats",

      JSON.stringify(chats)

    );


  },[chats]);




  useEffect(()=>{


    localStorage.setItem(

      "omni_active_chat",

      activeChat

    );


  },[activeChat]);




  // ------------------------------------
  // Current Messages
  // ------------------------------------

  const currentMessages =
  chats[activeChat]?.messages || [];




  // ------------------------------------
  // New Chat
  // ------------------------------------

  const createNewChat = ()=>{


    const newChat={


      title:"New Chat",


      messages:[

        {

          role:"assistant",

          content:
          "👋 Welcome to OmniAssistAI!\n\nStart a new conversation."

        }

      ]

    };


    setChats(prev=>[

      ...prev,

      newChat

    ]);


    setActiveChat(
      chats.length
    );


  };





  // ------------------------------------
  // Send Message
  // ------------------------------------

  const handleSend = async(question)=>{


    if(!question.trim())
      return;




    setChats(prev=>{


      const updated=[...prev];


      updated[activeChat]={

        ...updated[activeChat],


        title:

        updated[activeChat].title==="New Chat"

        ?

        question.slice(0,30)

        :

        updated[activeChat].title,



        messages:[


          ...updated[activeChat].messages,


          {

            role:"user",

            content:question

          }


        ]


      };



      return updated;


    });




    setLoading(true);



    try{


      const answer = await sendMessage(

        question,

        activePDF

      );



      setChats(prev=>{


        const updated=[...prev];


        updated[activeChat]={


          ...updated[activeChat],


          messages:[


            ...updated[activeChat].messages,


            {


              role:"assistant",

              content:answer


            }


          ]

        };



        return updated;


      });



    }

    catch(err){


      console.error(err);



      setChats(prev=>{


        const updated=[...prev];


        updated[activeChat]={


          ...updated[activeChat],


          messages:[


            ...updated[activeChat].messages,


            {


              role:"assistant",

              content:
              "❌ Unable to connect to backend."


            }


          ]


        };



        return updated;


      });


    }



    setLoading(false);


  };





return (

<div className="flex h-screen bg-gray-950 text-white">


<Sidebar

  chats={chats}

  activeChat={activeChat}

  setActiveChat={setActiveChat}

  createNewChat={createNewChat}


  activePDF={activePDF}

  setActivePDFState={setActivePDF}

  refreshPDFs={refreshPDFs}

/>



<div className="flex flex-1 flex-col">



<Navbar

onUploadSuccess={()=>

setRefreshPDFs(
prev=>prev+1
)

}

/>



<ChatWindow

messages={currentMessages}

loading={loading}

activePDF={activePDF}

/>



<ChatInput

onSend={handleSend}

activePDF={activePDF}

/>



</div>


</div>

);


}


export default Home;
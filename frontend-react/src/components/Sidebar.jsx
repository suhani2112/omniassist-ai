import { useEffect, useState } from "react";

import {
  getPDFs,
  setActivePDF,
  deletePDF,
} from "../services/api";


function Sidebar({
  chats,
  activeChat,
  setActiveChat,
  createNewChat,
  activePDF,
  setActivePDFState,
  refreshPDFs
}) {


  const [pdfs,setPdfs] = useState([]);



  const loadPDFs = async()=>{

    try{

      const data = await getPDFs();

      setPdfs(data.pdfs || []);

    }
    catch(err){

      console.error(err);

    }

  };



  useEffect(()=>{

    loadPDFs();

  },[refreshPDFs]);



  const handleSelectPDF = async(filename)=>{

    try{

      await setActivePDF(filename);

      setActivePDFState(filename);

    }
    catch(err){

      console.error(err);

      alert("Unable to select PDF.");

    }

  };




  const handleDeletePDF = async(filename)=>{


    const ok = window.confirm(
      `Delete ${filename}?`
    );


    if(!ok)
      return;



    try{

      await deletePDF(filename);


      if(activePDF===filename){

        setActivePDFState("");

      }


      loadPDFs();


    }
    catch(err){

      console.error(err);

      alert(
        "Unable to delete PDF."
      );

    }

  };





  return (

    <aside
      className="
      h-full
      w-72
      bg-gray-900
      border-r
      border-gray-700
      p-5
      flex
      flex-col
      "
    >



      {/* New Chat Button */}

      <button

        onClick={createNewChat}

        className="
        flex
        items-center
        justify-center
        gap-2
        rounded-xl
        bg-blue-600
        py-3
        font-medium
        text-white
        transition
        hover:bg-blue-700
        hover:scale-[1.02]
        shadow-lg
        shadow-blue-600/20
        "
      >

        ＋ New Chat

      </button>





      {/* PDFs */}


      <div className="mt-7">


        <h2
          className="
          mb-3
          text-xs
          font-semibold
          uppercase
          tracking-wider
          text-gray-400
          "
        >

          Documents

        </h2>



        <div
          className="
          space-y-2
          max-h-52
          overflow-y-auto
          "
        >



        {
          pdfs.length===0 &&

          <p
            className="
            text-sm
            text-gray-500
            "
          >
            No PDFs uploaded
          </p>

        }




        {
          pdfs.map((pdf)=>(


            <div

              key={pdf}

              className={`
              group
              flex
              items-center
              justify-between
              rounded-xl
              px-3
              py-3
              cursor-pointer
              transition

              ${
                activePDF===pdf
                ?
                "bg-blue-600/20 border border-blue-500/40"
                :
                "hover:bg-gray-800"
              }

              `}


              onClick={()=>handleSelectPDF(pdf)}

            >



              <div
                className="
                flex
                items-center
                gap-2
                text-sm
                text-gray-200
                truncate
                "
              >

                {
                  activePDF===pdf
                  ?
                  "🟢"
                  :
                  "📄"
                }


                <span className="truncate">
                  {pdf}
                </span>


              </div>





              <button

                onClick={(e)=>{

                  e.stopPropagation();

                  handleDeletePDF(pdf);

                }}


                className="
                opacity-0
                group-hover:opacity-100
                text-red-400
                hover:text-red-300
                transition
                "

              >

                🗑

              </button>



            </div>


          ))

        }


        </div>


      </div>







      {/* Chat History */}



      <div
        className="
        mt-8
        flex-1
        overflow-y-auto
        "
      >


        <h2

          className="
          mb-3
          text-xs
          font-semibold
          uppercase
          tracking-wider
          text-gray-400
          "

        >

          Chats

        </h2>




        <div className="space-y-2">


        {
          chats.map((chat,index)=>(


            <button

              key={index}


              onClick={()=>setActiveChat(index)}


              className={`

              w-full
              rounded-xl
              p-3
              text-left
              text-sm
              transition


              ${
                activeChat===index

                ?

                "bg-gray-700 text-white"

                :

                "text-gray-300 hover:bg-gray-800"

              }

              `}

            >

              💬 {chat.title}


            </button>


          ))

        }


        </div>


      </div>



    </aside>

  );

}


export default Sidebar;
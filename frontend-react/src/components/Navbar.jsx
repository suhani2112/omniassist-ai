import { useRef } from "react";
import { uploadPDF } from "../services/api";

function Navbar({ onUploadSuccess }) {
  const fileInputRef = useRef(null);

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };


  const handleFileChange = async (e) => {
    const file = e.target.files[0];

    if (!file) return;

    try {
      const response = await uploadPDF(file);

      alert(response.message);

      if (onUploadSuccess) {
        onUploadSuccess();
      }

    } catch (error) {

      console.error(error);

      if (error.response) {
        alert(
          error.response.data.detail ||
          "PDF upload failed."
        );
      } 
      else {
        alert("Unable to connect to backend.");
      }

    }

    e.target.value = "";
  };


  return (

    <header
      className="
      h-20
      flex
      items-center
      justify-between
      px-8
      border-b
      border-gray-700
      bg-gray-900/80
      backdrop-blur-xl
      "
    >


      {/* Brand */}

      <div className="flex items-center gap-4">


        <div
          className="
          flex
          h-12
          w-12
          items-center
          justify-center
          rounded-2xl
          bg-blue-600
          text-2xl
          shadow-lg
          shadow-blue-600/30
          "
        >
          🤖
        </div>


        <div>

          <h1
            className="
            text-xl
            font-bold
            tracking-wide
            text-white
            "
          >
            OmniAssistAI
          </h1>


          <p
            className="
            text-sm
            text-gray-400
            "
          >
            AI Assistant with Memory & RAG
          </p>


        </div>


      </div>



      {/* Actions */}


      <div className="flex items-center gap-5">


        <button

          onClick={handleButtonClick}

          className="
          flex
          items-center
          gap-2
          rounded-xl
          bg-blue-600
          px-5
          py-3
          font-medium
          text-white
          transition
          duration-300
          hover:bg-blue-700
          hover:scale-105
          shadow-lg
          shadow-blue-600/20
          "
        >

          📄
          Upload PDF

        </button>



        <div
          className="
          flex
          items-center
          gap-2
          rounded-full
          bg-green-500/10
          px-4
          py-2
          text-sm
          text-green-400
          border
          border-green-500/20
          "
        >

          <span
            className="
            h-2
            w-2
            rounded-full
            bg-green-400
            animate-pulse
            "
          >
          </span>

          Online

        </div>



        <input

          ref={fileInputRef}

          type="file"

          accept=".pdf"

          className="hidden"

          onChange={handleFileChange}

        />


      </div>


    </header>

  );
}


export default Navbar;
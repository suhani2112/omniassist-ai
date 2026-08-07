import axios from "axios";


const api = axios.create({

    baseURL: "http://127.0.0.1:8000",

});



// ----------------------------------------------------
// Chat
// ----------------------------------------------------

export const sendMessage = async (
    question,
    activePDF = null
) => {


    const response = await api.post(
        "/chat",
        {

            user_id: "default_user",

            question: question,

            active_pdf: activePDF

        }
    );


    return response.data.answer;

};



// ----------------------------------------------------
// Upload PDF
// ----------------------------------------------------

export const uploadPDF = async(file)=>{


    const formData = new FormData();


    formData.append(
        "file",
        file
    );



    const response = await api.post(

        "/upload-pdf",

        formData,

        {

            headers:{

                "Content-Type":
                "multipart/form-data"

            }

        }

    );


    return response.data;


};



// ----------------------------------------------------
// Get All PDFs
// ----------------------------------------------------

export const getPDFs = async()=>{


    const response = await api.get(
        "/pdfs"
    );


    return response.data;


};



// ----------------------------------------------------
// Set Active PDF
// ----------------------------------------------------

export const setActivePDF = async(filename)=>{


    const response = await api.post(

        `/set-active-pdf/${encodeURIComponent(filename)}`

    );


    return response.data;


};



// ----------------------------------------------------
// Delete PDF
// ----------------------------------------------------

export const deletePDF = async(filename)=>{


    const response = await api.delete(

        `/pdf/${encodeURIComponent(filename)}`

    );


    return response.data;


};



export default api;
import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});


export const sendMessage = async (question) => {

  const response = await api.post("/chat", {
    user_id: "default_user",
    question: question,
  });

  return response.data.answer;

};


export default api;
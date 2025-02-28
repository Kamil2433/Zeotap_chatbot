import { useState } from "react";
import { Send } from "lucide-react";
import "./App.css";
import axios from "axios";


const BASE_URL = "http://localhost:8000"; // Your FastAPI backend URL

export default function App() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hello! How can I assist you today?" }
  ]);
  const [input, setInput] = useState("");


  const fetchChatbotResponse = async (question) => {
    try {
      // Push user message to messages state
      setMessages((prevMessages) => [
        ...prevMessages,
        { sender: "user", text: question }
      ]);
  
      const response = await axios.get(`${BASE_URL}/query/`, {
        params: { question },
        headers: { "Content-Type": "application/json" },
      });
  
      if (response.data?.response) {
        // Push chatbot response to messages state
        setMessages((prevMessages) => [
          ...prevMessages,
          { sender: "bot", text: response.data.response }
        ]);
      }
  
      setInput(""); // Reset input field
      console.log("Chatbot Response:", response.data);
      
      return response.data;
  
    } catch (error) {
      console.error("Error fetching chatbot response:", error);
      
      // Push error message
      setMessages((prevMessages) => [
        ...prevMessages,
        { sender: "bot", text: "Failed to get response from chatbot" }
      ]);
  
      return {
        error: error.response?.data?.error || "Failed to get response from chatbot",
      };
    }
  };
  




  return (
    <div className="chat-container">
      {/* Header with Logo */}
      <div className="chat-header">
        {/* <img src="/logo.png" alt="Chat Logo" className="chat-logo" /> */}
        <h2>Zeotap Support Chat</h2>
      </div>

      {/* Chat Messages */}
      <div className="chat-messages"  style={{overflow:"scroll",height:"80vw"}}>
        {messages.map((msg, index) => (
          <div key={index} className={`chat-bubble ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>

      {/* Input Box */}
      <div className="chat-input-container">
        <input
          type="text"
          className="chat-input"
          placeholder="Type a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && fetchChatbotResponse()}
        />
        <button  className="chat-send-btn" onClick={()=>fetchChatbotResponse(input)}>
          <Send size={20} />
        </button>
      </div>
    </div>
  );
}

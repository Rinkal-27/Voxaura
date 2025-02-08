# **Voxaura – AI Voice Chatbot 🎙️🤖
**
## **🚀 Overview**

Voxaura is an AI-powered voice-based chatbot built using Streamlit, SpeechRecognition, Google Text-to-Speech (gTTS), and Groq’s Mixtral AI. It allows users to talk naturally with an AI assistant, which responds in both text and audio.


## **✨ Features**

✅ **Real-time Speech Recognition** – Converts spoken words into text using SpeechRecognition.
✅ **AI-Powered Responses** – Uses Groq Llama-3.3-70b-versatile for intelligent and conversational responses.
✅ **Natural Text-to-Speech (TTS)** – Converts AI responses into lifelike speech using gTTS.
✅ **Contextual Chat History** – Maintains session-based conversations in Streamlit.
✅ **Optimized Performance** – Fast response times with efficient API calls.


## **🛠️ Tech Stack**

**Python** (Core logic)
**Streamlit** (UI Framework)
**SpeechRecognition** (Voice input processing)
**Google TTS** (gTTS) (Text-to-speech conversion)
**Groq API** (LLM-based responses)
**NumPy & io** (Optimizations and audio handling)


## **🎤 How It Works**

1. Click "🎤 Start Talking" to begin.
2. Speak naturally, and your speech is converted to text.
3. AI processes your query and generates a response.
4. The bot speaks back and displays the response in text format.
5. Previous conversations are stored in Chat History.


##** 🔧 Installation & Setup**

1️⃣ **Clone the Repository**

git clone https://github.com/Rinkal-27/Voxaura.git
cd Voxaura

2️⃣ **Install Dependencies**

pip install -r requirements.txt

3️⃣ **Set Up API Keys**

Create a .env file and add your Groq API Key:
GROQ_API_KEY=your_api_key_here

4️⃣ **Run the Chatbot**

streamlit run app.py


## **💡 Future Enhancements**

**🔥 Multi-Language Support** (Expand speech recognition and TTS to multiple languages.)
**🧠 Memory & Context Awareness** (Allow chatbot to remember previous interactions.)
**📡 Cloud Integration** (Store chat logs and user preferences in the cloud.)
**🎭 Voice Customization** (Select different AI voices.)


## **🎉 Contributing**
We welcome contributions! Feel free to fork the repository, make changes, and submit a pull request.


## **📜 License**
This project is licensed under the MIT License.

import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import datetime
import os
import numpy as np
import groq
import io
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = groq.Client(api_key=GROQ_API_KEY)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Speech to text function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        st.write("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(mic, duration=0.4)
        recognizer.pause_threshold = 0.3
        recognizer.dynamic_energy_threshold = True
        
        audio = recognizer.listen(mic, timeout=4)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "❌ Could not understand the audio."
    except sr.RequestError as e:
        return f"⚠️ Speech Recognition error: {e}"

# Chat with Groq
def chat_with_groq(user_input):
    try:
        start_time = time.time()  
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=520,
            temperature=0.5
        )
        end_time = time.time()  
        response_time = round(end_time - start_time, 2)  
        return response.choices[0].message.content.strip(), response_time
    except Exception as e:
        return f"❌ Error with Groq API: {e}", None

# Text to speech function
def text_to_speech(text):
    tts = gTTS(text=text, lang="en", slow=False, tld="co.uk")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# Save and return audio file path
def save_audio(audio_bytes, filename):
    with open(filename, "wb") as f:
        f.write(audio_bytes.getbuffer())
    return filename

# Streamlit application
st.title("🗣️ Voxaura – AI Voice Chatbot")
st.markdown(
    """
    Welcome to the **Voxaura**! 🤖 Speak to the bot, and it will respond with text and speech.
    - Click **'🎤 Start Talking'** to begin.
    - The bot will generate both a **text and an audio response**.
    """
)

# Start Talking Button
if st.button("🎤 Start Talking"):
    user_text = speech_to_text()
    if user_text:
        st.session_state.chat_history.append({"role": "user", "content": user_text})

# Process User Input
if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "user":
    user_input = st.session_state.chat_history[-1]["content"].lower()

    # Handle special cases
    if "time" in user_input:
        bot_response = datetime.datetime.now().strftime('It is currently %H:%M')
        response_time = 0  
    elif any(word in user_input for word in ["thank", "thanks", "thank you", "i appreciate it"]):
        bot_response = np.random.choice([
            "You're welcome!", "Anytime!", "No problem!", "Absolutely!", "No worries!", "If you need anything else, just ask!"
        ])
        response_time = 0  # No processing time for predefined responses
    else:
        bot_response, response_time = chat_with_groq(user_input)

    # Convert response to speech
    audio_bytes = text_to_speech(bot_response)

    # Save audio file
    audio_filename = f"response_{len(st.session_state.chat_history)}.mp3"
    audio_path = save_audio(audio_bytes, audio_filename)

    # Append bot response
    st.session_state.chat_history.append({
        "role": "bot", "content": bot_response, "audio": audio_path, "response_time": response_time
    })

# Display Chat History
st.subheader("💬 Chat History")

for message in st.session_state.chat_history:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"**🗣️ You:** {message['content']}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"**🤖 Bot:** {message['content']}")
            st.audio(message["audio"], format="audio/mp3")
            if "response_time" in message:
                st.markdown(f"⏳ **Response Time:** {message['response_time']} sec")

import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="AI Video Studio", page_icon="🎬")

# Professional Dark Neon Styling
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%); color: #ffffff; }
    .header-container { text-align: center; padding: 20px; background: rgba(255, 255, 255, 0.05); border-radius: 20px; }
    .stButton > button { width: 100%; background: linear-gradient(90deg, #ec4899 0%, #8b5cf6 100%); color: white; font-size: 18px; font-weight: bold; border-radius: 12px; border: none; padding: 12px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1>✨ 🎬 AI Video Studio</h1>
        <p>Type your topic and generate professional AI voiceover!</p>
    </div>
""", unsafe_allow_html=True)

# English Input Field
user_prompt = st.text_input("🎯 Enter your video topic:", placeholder="e.g., Journey into space...")

if st.button("🚀 Generate AI Voice"):
    if user_prompt:
        st.info("Generating voiceover, please wait...")
        # Using English language code 'en'
        tts = gTTS(text=user_prompt, lang='en')
        audio_path = "voiceover.mp3"
        tts.save(audio_path)
        st.audio(audio_path)
        st.success("Voiceover generated successfully!")
    else:
        st.warning("Please enter a topic first!")
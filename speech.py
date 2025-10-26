import streamlit as st
import numpy as np
import os
import speech_recognition as sr
from Speech_Visualization.Speech import export_all_plots
from DiffusionModel.stable import generate_blueprint
import cv2

# ---------------------- PAGE CONFIG ---------------------- #
st.set_page_config(page_title="Speech to Blueprint", layout="wide")

st.title("Speech to Blueprint Generator")
st.markdown("""
**How it works:**
1. Speak out what you want to build or design.  
2. It will analyze your speech.  
3. And finally, it will *draw what it heard!* 
""")

# ---------------------- SESSION STATE ---------------------- #
if "audio_data_np" not in st.session_state:
    st.session_state.audio_data_np = None
if "text" not in st.session_state:
    st.session_state.text = ""
if "session_id" not in st.session_state:
    st.session_state.session_id = None

# ---------------------- FUNCTION: SHOW GRAPHS ---------------------- #
def display_graphs(output_dir, session_id):
    st.subheader("Speech Signal Analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(os.path.join(output_dir, f"waveform_{session_id}.png"), caption="Time Domain Waveform", use_container_width=True)
    with col2:
        st.image(os.path.join(output_dir, f"frequency_spectrum_{session_id}.png"), caption="Frequency Spectrum (FFT)", use_container_width=True)
    with col3:
        st.image(os.path.join(output_dir, f"spectrogram_{session_id}.png"), caption="Spectrogram", use_container_width=True)

# ---------------------- MAIN APP ---------------------- #
if st.button("Tap to Speak"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now!")
        audio_data = recognizer.listen(source)  # sr.AudioData object

    # Step 1: Recognize speech
    try:
        recognized_text = recognizer.recognize_google(audio_data)
        st.session_state.text = recognized_text
        st.success(f"Recognized Text: {recognized_text}")
    except Exception as e:
        st.error(f"Speech recognition failed: {e}")
        recognized_text = None

    # Step 2: Convert sr.AudioData to numpy array for graph plotting
    audio_bytes = audio_data.get_raw_data()
    audio_np = np.frombuffer(audio_bytes, dtype=np.int16)
    st.session_state.audio_data_np = audio_np

    # Step 3: Generate graphs
    if st.session_state.audio_data_np is not None:
        session_id = export_all_plots(st.session_state.audio_data_np, output_dir="Speech_Visualization/output")
        st.session_state.session_id = session_id
        display_graphs("Speech_Visualization/output", session_id)

# ---------------------- GENERATE BLUEPRINT ---------------------- #
if st.session_state.text:
    st.subheader("Generating Engineering Blueprint...")
    with st.spinner("Generating image..."):
        generate_blueprint(st.session_state.text)

    blueprint_path = "generated_blueprint.png"
    if os.path.exists(blueprint_path):
        img = cv2.imread(blueprint_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(img, caption="Generated Blueprint", use_container_width=True)
        st.success("Blueprint generated successfully!")
    else:
        st.error("Failed to generate image.")

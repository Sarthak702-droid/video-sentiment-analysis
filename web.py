import os
import tempfile
import seaborn as sns
import streamlit as st
import cv2
import matplotlib.pyplot as plt
import pandas as pd
from deepface import DeepFace

st.set_page_config(page_title="Video Sentiment Analysis", layout="wide")

st.title("🎥 Video Sentiment Analysis")
st.write("Upload a video to analyze the emotions over time.")

uploaded_file = st.file_uploader("Choose a video file...", type=["mp4", "avi", "mov", "mkv", "mpeg4"])

if uploaded_file is not None:
    st.success(f"File uploaded successfully! Analyzing `{uploaded_file.name}` ...")

    # Save uploaded video
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.read())

    cap = cv2.VideoCapture("temp_video.mp4")
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    results = []  # will hold dicts of all emotions per timestamp
    frame_number = 0

    with st.spinner("Analyzing video... please wait ⏳"):
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Analyze every 2 seconds
            if frame_number % (fps * 2) == 0:
                try:
                    analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                    emotions_dict = analysis[0]['emotion']
                    emotions_dict['time'] = frame_number // fps
                    results.append(emotions_dict)
                except Exception as e:
                    results.append({"time": frame_number // fps})

            frame_number += 1

    cap.release()

    # Convert to DataFrame
    if results:
        df = pd.DataFrame(results).fillna(0)

        st.subheader("📊 Emotion Timeline (Dominant Emotion)")

        # Plot each emotion as a line
        fig, ax = plt.subplots(figsize=(10, 5))
        for emotion in ['angry','disgust','fear','happy','sad','surprise','neutral']:
            if emotion in df.columns:
                ax.plot(df['time'], df[emotion], label=emotion)

        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Confidence (%)")
        ax.set_title("Emotions over Time")
        ax.legend()
        st.pyplot(fig)

        # Show dataset
        st.subheader("📂 Dataset Preview")
        st.dataframe(df)

        # Download button
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Dataset as CSV",
            data=csv,
            file_name="video_sentiment_analysis.csv",
            mime="text/csv",
        )
    else:
        st.error("No emotions detected. Try another video or check your setup.")

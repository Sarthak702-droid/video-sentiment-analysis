# 🎥 Video Sentiment Analysis

This project is a **Streamlit-based web application** that performs **video sentiment analysis** using **DeepFace** and **OpenCV**.  
It extracts frames from a video, detects facial emotions, and visualizes the emotional changes over time.  
The app also generates a structured dataset (CSV) for further analysis.

---

## 🚀 Features

- 📂 Upload video files (`.mp4, .avi, .mov, .mkv, .mpeg4`)
- 🧠 Detects **7 emotions**: `angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`, `neutral`
- 📊 Interactive **timeline chart** showing emotion confidence scores
- 📂 Automatic **dataset creation (CSV)** with time-based emotion scores
- ⬇️ One-click **download** of processed results

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web app framework
- [DeepFace](https://github.com/serengil/deepface) – Emotion detection
- [OpenCV](https://opencv.org/) – Video processing
- [Matplotlib](https://matplotlib.org/) – Visualization
- [Pandas](https://pandas.pydata.org/) – Dataset handling

---

## 🖼️ Screenshots  

### 🔹 Upload & Analysis Page  
![App Upload](assets/app_upload.png)  

### 🔹 Dataset Preview  
![Dataset Preview](assets/dataset_preview.png)  

---

## 📂 Dataset Output Example
| angry | disgust | fear | happy | sad | surprise | neutral | time |
|-------|---------|------|-------|-----|----------|---------|------|
| 0.0026 | 0.0000000002 | 0.00001 | 50.97 | 0.0048 | 0.5642 | 0.0169 | 48.4414 |
| 0.3199 | 0.0014 | 0.00007 | 86.06 | 0.00002 | 8.6831 | 0.000005 | 4.9303 |
| 4.7662 | 18.6247 | 35.4322 | 0.0952 | 5.5022 | 0.0516 | 35.5278 | 35.5278 |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/video-sentiment-analysis.git
cd video-sentiment-analysis

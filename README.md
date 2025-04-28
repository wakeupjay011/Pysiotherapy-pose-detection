Here’s a **professional and precise `README.md`** you can directly upload to GitHub:

---

# Physiotherapy Pose Detection Using Machine Learning

## Overview
This project is a **Physiotherapy Pose Detection** system built using **Python**, **Tkinter**, **OpenCV**, **Mediapipe**, and **Machine Learning** techniques.  
It helps in recognizing and classifying various physiotherapy and yoga poses from webcam input to assist users in physical rehabilitation.

## Features
- **Pose Detection** using Mediapipe Holistic Model.
- **Pose Classification** using Machine Learning models (Logistic Regression, Ridge Classifier, Random Forest, Gradient Boosting).
- **User Registration and Login System** using SQLite database (`evaluation.db`).
- **Graphical User Interface (GUI)** for user-friendly interactions.
- **Real-time Webcam Feed** with pose detection overlays.
- **Audio Output** of detected poses using text-to-speech (gTTS).
- **Training Custom Models** with user-collected data.
- **Pose Guidance** displaying sample exercise poses.

## Project Structure
| File | Description |
|:-----|:------------|
| `coordinate_in_CSV.py` | Captures pose and face landmarks and stores them in CSV for model training. |
| `GUI_main.py` | Main GUI window with Login, Register, and Exit options. |
| `GUI_Master1.py` | Real-time pose detection and classification after login. |
| `Home.py` | Dashboard displaying pose types and access to detection system. |
| `human_skeleten.py` | Displays detected human skeleton landmarks live. |
| `login.py` | User login functionality. |
| `registration.py` | New user registration form with validations. |
| `training.py` | Model training script on captured pose dataset. |
| `evaluation.db` | SQLite database storing user credentials. |

## Requirements
- Python 3.x
- Libraries: 
  - `opencv-python`
  - `mediapipe`
  - `tkinter`
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `Pillow`
  - `gTTS`
  - `playsound`
  - `matplotlib`
  - `speechrecognition`

Install them via:
```bash
pip install opencv-python mediapipe numpy pandas scikit-learn Pillow gTTS playsound matplotlib SpeechRecognition
```

## How to Run
1. Clone the repository.
2. Ensure all image and dataset paths in the scripts are correctly set.
3. Run:
   ```bash
   python GUI_main.py
   ```
4. Register or Login to access the main functionalities.

## Notes
- Ensure the camera permissions are enabled.
- Dataset CSVs and model `.pkl` files must be correctly generated for full functionality.
- Paths to icons and images must exist for GUI icons and backgrounds to load.





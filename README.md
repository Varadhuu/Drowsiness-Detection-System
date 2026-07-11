# 💤 Driver Drowsiness Detection System

## Overview

The Driver Drowsiness Detection System is a Computer Vision application developed using Python, OpenCV, and Dlib. It continuously monitors the driver's eyes through a webcam and detects prolonged eye closure using the Eye Aspect Ratio (EAR) algorithm. When drowsiness is detected, the system displays a warning message and plays an alarm to alert the driver.

---

## Features

* Real-time face detection
* Eye landmark detection using Dlib's 68 facial landmark model
* Eye Aspect Ratio (EAR) calculation
* Drowsiness detection based on consecutive eye closure
* Audible alert using Windows Beep
* Visual warning displayed on the webcam feed
* Lightweight and easy to run

---

## Technologies Used

* Python
* OpenCV
* Dlib
* SciPy
* Imutils
* NumPy
* Winsound (Windows)

---

## Project Structure

```
Drowsiness-Detection-System/
│
├── main.py
├── requirements.txt
├── README.md
├── shape_predictor_68_face_landmarks.dat
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Drowsiness-Detection-System.git
```

Move into the project folder:

```bash
cd Drowsiness-Detection-System
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Download the Landmark Model

Download the `shape_predictor_68_face_landmarks.dat` file and place it inside the project folder.

Official Dlib Model:

http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

Extract the downloaded `.bz2` file before running the project.

---

## Run the Project

```bash
python main.py
```

Press **Q** to exit the application.

---

## How It Works

1. Opens the webcam.
2. Detects the user's face.
3. Identifies the eye landmarks using Dlib.
4. Calculates the Eye Aspect Ratio (EAR).
5. Checks whether the EAR falls below the threshold.
6. Counts consecutive frames with closed eyes.
7. Displays a warning and plays an alarm when drowsiness is detected.

---

## Eye Aspect Ratio Formula

```
EAR = (A + B) / (2 × C)
```

Where:

* **A** = Vertical eye distance
* **B** = Vertical eye distance
* **C** = Horizontal eye distance

A lower EAR indicates that the eyes are closed.

---

## Future Improvements

* Yawn detection
* Head pose estimation
* Blink rate analysis
* Email/SMS alerts
* Mobile application support
* Deep Learning-based facial landmark detection
* Driver monitoring dashboard
* Raspberry Pi deployment

---

## Author

**Varadha Rajan S**


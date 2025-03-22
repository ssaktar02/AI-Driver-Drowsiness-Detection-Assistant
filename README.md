# AI Driver Drowsiness Detection Assistant

A real-time system to detect driver drowsiness assistant using OpenCV, dlib, and an Arduino-based alert mechanism.

## Features
- **Drowsiness Detection**: Utilizes eye aspect ratio (EAR) to detect signs of drowsiness.
- **Real-Time Alerts**: Sends alerts to the driver via an Arduino-connected buzzer.
- **Hardware Integration**: Combines Python-based detection with Arduino for real-time feedback.

## Requirements
- Python 3.x
- Libraries: OpenCV, dlib, scipy, imutils, pyserial
- Hardware: Webcam and Arduino with a buzzer module

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Driver-Drowsiness-Detection.git
   cd Driver-Drowsiness-Detection
   
**## Install dependencies**

pip install -r requirements.txt

**## Usage**
Run the Python script:
python project_final.py


Upload Nandy_Project.ino to your Arduino using the Arduino IDE.

**## Notes**
Ensure the webcam and Arduino are connected properly.
Adjust the threshold values in the Python script (thresh, alert_time_threshold) based on your setup.

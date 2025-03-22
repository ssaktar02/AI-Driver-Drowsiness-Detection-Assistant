from scipy.spatial import distance 
from imutils import face_utils 
import imutils 
import dlib 
import cv2 
import serial
import time


ser = serial.Serial('COM5', 9600)  

def eye_aspect_ratio(eye): 
    A = distance.euclidean(eye[1], eye[5]) 
    B = distance.euclidean(eye[2], eye[4]) 
    C = distance.euclidean(eye[0], eye[3]) 
    ear = (A + B) / (2.0 * C) 
    return ear 

thresh = 0.25 
frame_check = 20 
alert_time_threshold = 1.0  # Time threshold for triggering continuous alert
alert_start_time = 0  # Initialize alert start time
alert_sent = False  # Flag to track if alert has been sent
alert_active = False  # Flag to track if alert is currently active
frame_width = 650  # Adjust frame width as needed
detect = dlib.get_frontal_face_detector() 
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"] 
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"] 
cap=cv2.VideoCapture(0) 

while True: 
    ret, frame=cap.read() 
    frame = imutils.resize(frame, width=frame_width) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    subjects = detect(gray, 0) 
    
    for subject in subjects: 
        shape = predict(gray, subject) 
        shape = face_utils.shape_to_np(shape) 
        leftEye = shape[lStart:lEnd] 
        rightEye = shape[rStart:rEnd] 
        leftEAR = eye_aspect_ratio(leftEye) 
        rightEAR = eye_aspect_ratio(rightEye) 
        ear = (leftEAR + rightEAR) / 2.0 
        leftEyeHull = cv2.convexHull(leftEye) 
        rightEyeHull = cv2.convexHull(rightEye) 
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1) 
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1) 
        
        if ear < thresh: 
            if not alert_sent:
                current_time = time.time()
                if alert_start_time == 0:
                    alert_start_time = current_time
                if current_time - alert_start_time >= alert_time_threshold:
                    alert_active = True
                    alert_sent = True
                    ser.write(b'1')
        else:
            alert_start_time = 0
            alert_sent = False
            alert_active = False
            ser.write(b'0')

    if alert_active:
        cv2.putText(frame, "*ALERT!*", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.putText(frame, "*ALERT!*", (10, 325), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Frame", frame) 
    key = cv2.waitKey(1) & 0xFF 
    if key == ord("q"): 
        break 
    elif key == 27:  # Press ESC to quit
        break

ser.close()
cv2.destroyAllWindows() 
cap.release()

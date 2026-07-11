from scipy.spatial import distance as sict
from imutils import face_utils
import imutils
import cv2
import dlib
import winsound

freq = 3000
duration = 1000

def eye_aspect_ration(eye):
    A = sict.euclidean(eye[1], eye[5])
    B = sict.euclidean(eye[2], eye[4])
    C = sict.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

cnt = 0
earthresh = 0.3
earframes = 45


cam = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(lstart,lend) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rstart,rend) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

while True:
    _,frame = cam.read()
    frame = imutils.resize(frame,width=450)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    r = detector(gray,0)
    for i in r:
        shape = predictor(gray,i)
        shape = face_utils.shape_to_np(shape)
        lefteye = shape[lstart:lend]
        righteye = shape[rstart:rend]

        leftEAR = eye_aspect_ration(lefteye)
        rightEAR = eye_aspect_ration(righteye)

        ear = (leftEAR + rightEAR) / 2.0

        lefteyehull = cv2.convexHull(lefteye)
        righteyehull = cv2.convexHull(righteye)

        cv2.drawContours(frame,[lefteyehull],-1,(0,0,255),1)
        cv2.drawContours(frame,[righteyehull],-1,(0,0,255),1)

        if ear < earthresh:
            cnt+=1
            if cnt >= earframes:
                cv2.putText(frame,"DROWSINESS ALERT!",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
                winsound.Beep(freq,duration)
        else:
            cnt = 0
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) 
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
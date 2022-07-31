import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('image/danc.mp4')

pTime = 0
cTime = 0

while True:
    success, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(frame,(cx,cy),5,(255,0,0),cv2.FILLED)
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)

    cv2.imshow("Output", frame)
    if cv2.waitKey(10) & 0xFF == ord("e"):
        break 

cap.release()
cv2.destroyAllWindows()
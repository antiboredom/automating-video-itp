import numpy as np
import cv2
import ipcamera
import time

# download haar cascades from: https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(ipcamera.MJPG_URL)

# get the current time in seconds
last_moved = time.time()

recording = 0

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # find the biggest face and center the camera on it
    current_time = time.time()
    if len(faces) > 0 and current_time - last_moved > 4:
        biggest_face = sorted(faces, key=lambda x: x[2])[0]
        ipcamera.record(str(recording) + '.mp4', duration='00:00:03')
        ipcamera.center(biggest_face[0] + biggest_face[2]/2, biggest_face[1] + biggest_face[3]/2)
        last_moved = time.time()
        recording += 1


    # comment out these lines if you don't want to see a preview window
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

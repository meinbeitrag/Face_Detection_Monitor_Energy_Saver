import cv2
import time
import subprocess
import datetime


def detect_face(frame, face_cascade):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    return faces


def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    display_sleep_time = 10  # in seconds
    check_interval = 10  # time interval betw een webcam activations, in seconds
    num_frames = 5  # number of frames to capture

    while True:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Webcam not found.")
            return

        for i in range(num_frames):
            ret, frame = cap.read()
            if not ret:
                break

            faces = detect_face(frame, face_cascade)

            if len(faces) > 0:
                subprocess.Popen(['caffeinate', '-u', f'-t{display_sleep_time}'])
                break

        cap.release()
        current_time = datetime.datetime.now()
        print("Checked at: ", current_time)

        time.sleep(check_interval - 1)  # Sleep for the remaining time of the interval


if __name__ == '__main__':
    main()


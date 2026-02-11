import cv2
import face_recognition
import pickle
import os
from src.attendance import mark_attendance

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENC_PATH = os.path.join(BASE_DIR, "encodings", "face_encodings.pkl")

with open(ENC_PATH, "rb") as f:
    known_encodings, known_names = pickle.load(f)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for enc, face in zip(encodings, faces):
        distances = face_recognition.face_distance(known_encodings, enc)
        best_match = distances.argmin()

        if distances[best_match] < 0.45:
            student = known_names[best_match]
            mark_attendance(student)

            top, right, bottom, left = face
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
            cv2.putText(frame, student, (left, top-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

import cv2
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
print("click S to capture the image")

path = os.path.join(DATASET_DIR, f"{roll}_{name}")
os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Capture Face", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(path, f"{count}.jpg"), frame)
        count += 1
        print(f"Saved image {count}")

    if count == 30:
        break

cam.release()
cv2.destroyAllWindows()

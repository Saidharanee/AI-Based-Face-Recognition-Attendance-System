import face_recognition
import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
ENCODINGS_DIR = os.path.join(BASE_DIR, "encodings")

os.makedirs(ENCODINGS_DIR, exist_ok=True)

known_encodings = []
known_names = []

for folder in os.listdir(DATASET_DIR):
    folder_path = os.path.join(DATASET_DIR, folder)
    if not os.path.isdir(folder_path):
        continue

    for image in os.listdir(folder_path):
        img_path = os.path.join(folder_path, image)
        img = face_recognition.load_image_file(img_path)
        enc = face_recognition.face_encodings(img)

        if enc:
            known_encodings.append(enc[0])
            known_names.append(folder)

with open(os.path.join(ENCODINGS_DIR, "face_encodings.pkl"), "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print("Training Completed")

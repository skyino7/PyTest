import cv2
import face_recognition
import numpy as np
import time
import requests

video_capture = cv2.VideoCapture(1)

# Load known face encodings and names
known_face_encodings = [...]  # Replace with your known face encodings
known_face_names = [...]  # Replace with your known face names

# Initialize process_this_frame variable
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    face_names = []  # Initialize face_names here

    if process_this_frame:
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        json_to_export = {}

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding)

            name = "Unknown"

            face_distances = face_recognition.face_distance(
                known_face_encodings)

            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                json_to_export['name'] = name

                json_to_export['hour'] = f'{time.localtime().tm_hour}:{time.localtime().tm_min}'

                json_to_export['date'] = f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}'

                json_to_export['picture_array'] = frame.tolist()

                r = requests.post(
                    url='http://127.0.0.1:5000/receive_data', json=json_to_export)

                print("Status: ", r.status_code)

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

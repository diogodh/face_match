import os
import face_recognition

# Load your face image
your_face_path = ""
your_face_image = face_recognition.load_image_file(your_face_path)
your_face_encoding = face_recognition.face_encodings(your_face_image)[0]

# Replace 'path_to_your_folder' with the actual path to your image folder
folder_path = ""

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):  # Adjust the file extension as needed
        # Construct the full path to the image
        img_path = os.path.join(folder_path, filename)

        # Load the image
        unknown_image = face_recognition.load_image_file(img_path)

        # Find all face locations in the image
        face_locations = face_recognition.face_locations(unknown_image)

        # If faces are found, check if your face is present
        if face_locations:
            # Encode the faces in the image
            unknown_face_encoding = face_recognition.face_encodings(unknown_image, face_locations)

            # Compare with your face encoding
            results = face_recognition.compare_faces([your_face_encoding], unknown_face_encoding[0])

            # If your face is found, print the filename
            if results[0]:
                print(f"Your face found in {filename}")

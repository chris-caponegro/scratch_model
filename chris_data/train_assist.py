import cv2
import os
import time

def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

print("TEST")
# Define folders for image storage
SCRATCHED_FOLDER = "scratched"
NOT_SCRATCHED_FOLDER = "not_scratched"
create_folder_if_not_exists(SCRATCHED_FOLDER)
create_folder_if_not_exists(NOT_SCRATCHED_FOLDER)

# Initialize camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'a' to save as scratched, 'b' to save as not scratched, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    cv2.imshow("Camera Feed", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('a'):
        filename = os.path.join(SCRATCHED_FOLDER, f"scratched_{int(time.time())}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved to {filename}")

    elif key == ord('b'):
        filename = os.path.join(NOT_SCRATCHED_FOLDER, f"not_scratched_{int(time.time())}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved to {filename}")

    elif key == ord('q'):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()

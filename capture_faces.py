import cv2 # Import the OpenCV library for computer vision tasks
import os  # Import the os library for file and directory operations

# Ask for the student's name
student_name = input("Enter student's name: ").strip() 

# Create folder if it doesn't exist
save_folder = "images"
os.makedirs(save_folder, exist_ok=True)

# Open webcam
camera = cv2.VideoCapture(0)

count = 0

print("\nPress 's' to save an image.")
print("Press 'q' to quit.\n")

while True:
    success, frame = camera.read()

    if not success:
        print("Failed to open webcam.")
        break

    cv2.imshow("Capture Student Face", frame)

    key = cv2.waitKey(1)

    # Save image when 's' is pressed
    if key == ord('s'):
        filename = f"{student_name}_{count}.jpg"
        filepath = os.path.join(save_folder, filename)

        cv2.imwrite(filepath, frame)

        count += 1
        print(f"Saved {filename}")

    # Exit
    if key == ord('q') or count >= 20:
        break

camera.release()
cv2.destroyAllWindows()

print(f"\nCaptured {count} images successfully!")
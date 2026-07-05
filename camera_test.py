import cv2 # Import the OpenCV library for computer vision tasks

# Open the default webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam started successfully.")
print("Press 'q' to quit.")

while True:
    success, frame = camera.read() 

    if not success:
        print("Failed to capture frame.")
        break

    # Display the video
    cv2.imshow("Smart Attendance - Webcam Test", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
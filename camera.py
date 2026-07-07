import cv2

def start_camera():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Cannot open webcam.")
        return

    print("Press Q to quit.")

    while True:

        success, frame = camera.read()

        if not success:
            break

        cv2.imshow("Smart Attendance System", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_camera()
import cv2
from insightface.app import FaceAnalysis

print("Loading InsightFace...")

app = FaceAnalysis(
    name="buffalo_s",
    allowed_modules=["detection"],
    providers=["CPUExecutionProvider"]
)

app.prepare(ctx_id=-1, det_size=(320, 320))

print("Model loaded successfully!")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open webcam.")
    exit()

print("Press Q to quit.")

while True:
    success, frame = camera.read()

    if not success:
        print("Failed to read frame.")
        break

    print("Before detection")

    faces = app.get(frame)

    print("After detection")

    for face in faces:
        x1, y1, x2, y2 = face.bbox.astype(int)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
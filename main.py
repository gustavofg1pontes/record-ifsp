import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (1280, 720))
recording = False

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('video', frame)
        if recording:
            out.write(frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('r'):
        recording = not recording
        print('recording:', recording)

cap.release()
out.release()
cv2.destroyAllWindows()
import cv2
import os
from Cronometer import Cronometer
from Recorder import Recorder, cut_and_save_video


def main():
    cronometer = Cronometer()
    cronometer.start()
    cameraFPS = 10
    recorder = Recorder(1280, 720, cameraFPS)
    highlights_amount = 0
    while True:
        if not recorder.isRecording:
            recorder.isRecording = True
        if not recorder.out.isOpened():
            recorder.startRecording()
        ret, frame = recorder.cap.read()
        if ret:
            cv2.imshow('video', frame)
            if recorder.isRecording:
                recorder.out.write(frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            recorder.isRecording = False
            recorder.out.release()
            if cronometer.seconds < 30:
                cut_and_save_video(f"outputHighlight{highlights_amount}.mp4", 0, cronometer.seconds)
            else:
                cut_and_save_video(f"outputHighlight{highlights_amount}.mp4", cronometer.seconds - 30, cronometer.seconds)
            cronometer.seconds = 0
            highlights_amount += 1
            if os.path.exists('output.mp4'):
                os.remove('output.mp4')

    cronometer.stop()
    recorder.out.release()
    recorder.cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

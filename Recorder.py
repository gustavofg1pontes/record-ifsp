import threading
import time
import os
import cv2
from moviepy.editor import VideoFileClip


def cut_and_save_video(output_file, start_time, end_time):
    clip = VideoFileClip('output.mp4')
    clipped = clip.subclip(start_time, end_time)
    clipped.write_videofile(output_file, codec='libx264')


class Recorder:
    def __init__(self, width, height, cameraFPS):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        self.cameraFPS = cameraFPS
        self.out = cv2.VideoWriter('output.mp4', self.fourcc, cameraFPS, (width, height))
        self.isRecording = False

    def startRecording(self):
        self.out.open('output.mp4', self.fourcc, self.cameraFPS, (1280, 720))


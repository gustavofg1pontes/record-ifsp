import threading
import time


class Cronometer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()  # Event for stopping the thread
        self.seconds = 0
        self.target = self.seconds_counter

    def run(self):
        while not self._stop_event.is_set():
            self.target()

    def stop(self):
        self._stop_event.set()  # Set the event to stop the thread

    def seconds_counter(self):
        try:
            while not self._stop_event.is_set():
                print(f"Seconds elapsed: {self.seconds}")
                self.seconds += 1
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nTimer stopped.")

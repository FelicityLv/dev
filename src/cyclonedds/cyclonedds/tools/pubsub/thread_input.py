from threading import Thread, Event
import time

from cyclonedds.tools.pubsub import command


class Worker:
    def __init__(self):
        self.txt = None
        self.quit_e = Event()
        self.read_e = Event()
        self.work = Thread(target=self._work)
        self.work.start()
        self.pubsub = Thread(target=command, args=(self._work(),))
        self.pubsub.start()
        # self.pubsub.start()

    def _work(self):
        while not self.quit_e.is_set():
            time.sleep(1)
            txt = self.get_input()
            if txt:
                print(txt)
                return txt

    def get_input(self):
        if self.txt is not None:
            txt = self.txt
            self.txt = None
            self.read_e.set()
            return txt
        return None

    def put_input(self, txt):
        self.read_e.clear()
        self.txt = txt
        self.read_e.wait()

    def stop(self):
        self.quit_e.set()
        self.work.join()


worker = Worker()
try:
    while True:
        txt = input("")
        worker.put_input(txt)
except (KeyboardInterrupt, IOError, ValueError):
    pass
finally:
    worker.stop()
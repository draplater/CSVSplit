import os
import threading
from io import StringIO

import sys
from queue import Queue, Empty


class BufferedReader:
    """
    Speed up file reading with an buffer.
    """

    progressbar_width = 50

    def __init__(self, f, queue_size=256):
        self.f = f
        self.total_size = os.fstat(f.fileno()).st_size
        self.reading_thread = threading.Thread(target=self.__read)
        self.lines = Queue(queue_size)
        self.progress = 0
        self.eof = False
        self.reading_thread.start()

    def __read(self):
        counter = 0
        while True:
            line = self.f.readline()
            if not line:
                self.eof = True
                self.__progressbar()
                break
            self.lines.put(line.strip("\n"))
            if counter % 100 == 0:
                self.__progressbar()
            counter += 1

    def __progressbar(self):
        progress = int(self.f.tell() / self.total_size * 100)
        if progress == self.progress:
            return
        self.progress = progress
        # setup toolbar
        sys.stdout.write("\b" * (BufferedReader.progressbar_width+5)) # return to start of line, after '['
        sys.stdout.write("[{}]{}%".format("-" * (progress // 2) +
                                   " " * (BufferedReader.progressbar_width - progress // 2 ), progress))
        if progress == 100:
            print('\n')
        sys.stdout.flush()

    def readline(self):
        if not self.reading_thread.is_alive():
            if self.lines.empty():
                return ""
        try:
            return self.lines.get(timeout=1)
        except Empty:
            return self.readline()
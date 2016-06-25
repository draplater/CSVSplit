import os
from io import StringIO
from collections import deque

import sys


class BufferedReader:
    """
    Speed up file reading with an buffer.
    """

    progressbar_width = 50

    def __init__(self, f, buf_size=256 * 1024):
        self.f = f
        self.total_size = os.fstat(f.fileno()).st_size
        self.buf_size = buf_size
        self.lines = deque()
        self.progress = 0
        self.eof = False

    def __read(self):
        for i in range(200):
            line = self.f.readline()
            if not line:
                self.eof = True
                break
            self.lines.append(line.strip("\n"))
        self.__progressbar()

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
        if not self.lines:
            if self.eof:
                return ""
            self.__read()
        return self.lines.popleft()


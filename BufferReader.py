import os
from io import StringIO
from collections import deque

import sys


class BufferedReader:
    """
    Speed up file reading with an buffer.
    """

    progressbar_width = 50

    def __init__(self, f, buf_size=4096):
        self.f = f
        self.total_size = os.fstat(f.fileno()).st_size
        self.buf_size = buf_size
        self.residue_buffer = StringIO()
        self.lines = deque()
        self.progress = 0
        self.eof = False

    def __read(self):
        def extract_buffer():
            self.lines.append(self.residue_buffer.getvalue())
            self.residue_buffer.truncate(0)
            self.residue_buffer.seek(0)

        buf = self.f.read(self.buf_size)
        self.__progressbar()
        if len(buf) != self.buf_size:
            self.eof = True
        for i in buf:
            if i == "\n":
                extract_buffer()
            else:
                self.residue_buffer.write(i)
        if self.eof:
            extract_buffer()

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
                assert len(self.residue_buffer) == 0
                return ""
            self.__read()
        return self.lines.popleft()


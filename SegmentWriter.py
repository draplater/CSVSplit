class SegmentWriter:
    """
    write file segment.
    """

    def __init__(self, prefix, segment_length, suffix="",
                 encoding=None, default_counter=0,
                 counter_style=".part{}", header="", newline="\r\n"):
        """
        create a new file segment with new
        :param prefix:
        :param segment_length:
        :param suffix:
        :param encoding:
        :param default_counter:
        :param counter_style:
        :param header:
        :param newline:
        """
        self.prefix = prefix
        self.segment_length = segment_length
        self.suffix = suffix
        self.file_counter = default_counter
        self.size_counter = 0
        self.counter_style = counter_style
        self.header = header
        self.encoding = encoding
        self.newline = newline
        self.__next_file()

    def __next_file(self):
        filename = self.prefix + self.counter_style.format(self.file_counter) + self.suffix
        self.f = open(filename, "w", encoding=self.encoding, newline=self.newline)
        self.file_counter += 1
        self.size_counter = 0
        if self.header:
            assert len(self.header) + len(self.newline) < self.segment_length
            self.f.write(self.header + "\n")
            self.size_counter += len(self.header) + len(self.newline)

    def write_line(self, line):
        assert len(self.header) + len(self.newline) + len(line) + len(self.newline) < self.segment_length
        if self.size_counter + len(line) + len(self.newline) > self.segment_length:
            self.__next_file()
        self.f.write(line + "\n")
        self.size_counter += len(line) + len(self.newline)
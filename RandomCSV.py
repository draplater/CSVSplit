#!/usr/bin/python3
"""
Randomly generate large CSV file.
"""
import random
import string
import sys
import re

from utils import read_size

FILENAME_LENGTH = 10


def show_usage():
    print("Usage: {} column-number size".format(sys.argv[0]))


def random_string(length):
    """
    generate ascii-letter string of specific length
    :param length: string length
    :return: random ascii-letter string
    """
    return ''.join([random.choice(string.ascii_letters) for i in range(length)])


def random_length_string(length):
    """
    generate ascii-letter string shorter then specific length
    :param length:  string length
    :return: random ascii-letter string
    """
    return random_string(random.randint(1, length))


if len(sys.argv) != 3:
    show_usage()
    exit(2)

n = sys.argv[1]
size = sys.argv[2]


if re.match(r"^\d+$", n) and re.match(r"^\d+[kmgKMG]?$", size):
    n = int(n)
    size = read_size(size)
else:
    show_usage()
    exit(2)


filename = random_string(FILENAME_LENGTH) + ".csv"
f = open(filename, "w")
counter = 0
print("Writing to {}...".format(filename))
while True:
    line = ",".join([random_length_string(100) for i in range(1, n)]) + "\n"
    if counter + len(line) > size:
        break
    f.write(line)
    counter += len(line)
f.close()
print("Done!")
import re

unit_map = {"K": 1024, "M": 1024 * 1024, "G": 1024 * 1024 * 1024}


def read_size(size_string):
    """
    convert human readable size string like "30G" to integer.
    :param size_string: size string
    :return: integer representation of size
    """
    if re.match(r"^\d+$", size_string):
        return int(size_string)
    size_number = int(size_string[:-1])
    size_unit = size_string[-1].upper()
    return size_number * unit_map[size_unit]

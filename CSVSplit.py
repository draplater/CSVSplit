#!/usr/bin/python3

import logging
import argparse
import sys
import re

from RowFilter import RowFilter
from SegmentWriter import SegmentWriter
from utils import read_size


def column_choose(line, columns_filter):
    """
    split and filter column.
    :param line:
    :param columns_filter:
    :return:
    """
    columns = line.split(',')
    return ','.join([columns[i] for i in columns_filter])


def main():
    columns = []
    logging_level = logging.INFO

    # parse args
    examples = "Example: {0} -s 1M -c 1,3,5,10-20 -e gbk -f \'#1 == \"male\"\' filename.csv\n" \
               "Example: {0} -s 1048576 -t -c name,gender -f \'int(#:age:) <= 20\' -n filename.csv".format(sys.argv[0])
    parser = argparse.ArgumentParser(prog=sys.argv[0],
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=examples)
    parser.add_argument('filename', metavar='filename',
                        help='File to split.')
    parser.add_argument('-s', "--size", help='Max split size. Can be an integer like "10240", '
                                             'or human readable format like "10K".')
    parser.add_argument('-c', "--column", action="store",
                        help='select column by number. '
                             'Example: "1-3,5" means select the 1st to the 3rd, and the 5th column.')
    parser.add_argument('-f', '--filter', action="store",
                        help="Filter row with specific condition. Use python expression. "
                             "\"#n\" means using the string value of n-th column. "
                             "When using -t, \"#:name:\" means using the string value of the column "
                             "whose title is \"name\". "
                             "Example: \'#1 == \"male\"\'")
    parser.add_argument('-n', "--column-name", action="store_true",
                        help='select column by title instead of id. Should be used with -t.')
    parser.add_argument('-t', "--title", action="store_true",
                        help="use the first line as title and add it to each file.")
    parser.add_argument('-e', "--encoding", action="store",
                        help="encoding of input file. Default: system encoding")
    parser.add_argument('-o', "--output-encoding", action="store",
                        help="encoding of output file. "
                             "If not set, system encoding or input encoding will be used.")
    parser.add_argument('-d', "--debug", action="store_true",
                        help="debugging.")
    args = parser.parse_args()
    if args.column_name and not args.title:
        parser.error("-n should be used with -t.")
    if not re.match(r"^\d+[kmgKMG]?$", args.size):
        parser.error("Invalid size.")
    size = read_size(args.size)
    if size == 0:
        parser.error("size too small.")

    # handle logging and debugging
    if args.debug:
        logging_level = logging.DEBUG
    logging.basicConfig(level=logging_level,
                        stream=sys.stdout,
                        format='%(asctime)s %(filename)s[%(lineno)d] '
                               '%(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug(args)

    # parse column filter
    if args.column:
        # handle columns by id
        if not args.column_name:
            if not re.match(r"^(([\d-]+),)*([\d-]+)$", args.column):  # like 1-2,4-5,7
                parser.error("Wrong column format.")
            for i in args.column.split(","):
                start, end = re.match("^(\d+)(?:-(\d+))?$", i).groups()  # start(-end)
                if end:
                    columns.extend(range(int(start) - 1, int(end)))  # start from 0
                else:
                    columns.append(int(start) - 1)
        # handle columns by title
        else:  # split it into list and process it later
            columns = args.column.split(",")

    # handle output encoding
    if args.output_encoding:
        output_encoding = args.output_encoding
    elif args.encoding:
        output_encoding = args.encoding
    else:
        output_encoding = None

    # open file
    f = open(args.filename, encoding=args.encoding)

    # extract title from the first line
    if args.title:
        title_string = f.readline().strip("\n")
        # process column name selector
        if args.column_name:
            columns_ids = []
            # map: title -> subscript
            idmap = {i[1]: i[0] for i in enumerate(title_string.split(","))}
            # convert title representation of columns to id representation
            for i in columns:
                try:
                    columns_ids.append(idmap[i])
                except KeyError:
                    raise Exception("Unknown column name {}.".format(i))
            columns = columns_ids
        # filter columns of title
        if columns:
            title_string = column_choose(title_string, columns)
    else:
        title_string = ""

    # initiate row filter
    if args.filter:
        if args.column_name:
            rf = RowFilter(args.filter.strip("\n"), title_string.split(","))
        else:
            rf = RowFilter(args.filter.strip("\n"))

    # create segment writer
    try:
        filename_base, filename_extension = args.filename.rsplit(".", 1)
    except ValueError:  # no extension name
        filename_base = args.filename
        filename_extension = ""
    sw = SegmentWriter(filename_base, size,
                       encoding=output_encoding,
                       suffix=("." + filename_extension) if filename_extension else "",
                       header=title_string)

    # split the CSV file
    for i in f:
        line = i.strip("\n")
        if not args.filter or rf.filter(line):
            if columns:
                line = column_choose(line, columns)
            sw.write_line(line)


if __name__ == "__main__":
    main()

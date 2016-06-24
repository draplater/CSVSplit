# CSVSplit
```
usage: CSVSplit.py [-h] [-s SIZE] [-c COLUMN] [-n] [-t] [-e ENCODING]
                   [-o OUTPUT_ENCODING] [-d]
                   filename

positional arguments:
  filename              File to split.

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  Max split size. Can be an integer like "10240", or
                        human readable format like "10K".
  -c COLUMN, --column COLUMN
                        select column
  -n, --column-name     select column by title instead of id. Should be used
                        with -t
  -t, --title           use the first line as title and add it to each file.
  -e ENCODING, --encoding ENCODING
                        encoding of input file. Default: system encoding
  -o OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                        encoding of output file. If not set, system encoding
                        or input encoding will be used.
  -d, --debug           debugging.
```

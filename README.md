# CSVSplit
## 简介
本程序可以将CSV文件分割为指定大小的多个文件，并支持列选择、行过滤的功能。

## 特点
- 选择列时可以使用列的编号。包括单个列编号和列的编号范围。如“1-5,7”表示选择第1至5列、第7列。
- 可以使用条件表达式满足指定要求的行，如找出第二列值为"male"的行、标题为"age"的相应列数值小于等于20的的行。
- 支持将文件第一行当作标题行，并写入分割后每个文件的开头。
- 有标题行时，可以使用列名作为关键字选择列。
- 输入文件大小时不仅可以输入整数，还可以输入带单位的格式，如"10K"、"1G"等。
- 支持手动指定输入文件的编码来处理不同编码的文件，如GBK、UTF-8等。
- 处理过程中，程序可以在命令行中显示读取文件的进度条。
- 尝试了多种方式进行读取。并给出测试结果。

## 不同读取方式的测试
本程序尝试了多种方式来读取输入文件：
1. 使用Python文件对象的迭代器来逐行读入(for i in f)；
2. 构造一个输入文件缓存，每次读取时重复使用f.readline()读取多行到缓存，再从缓存中输出；
3. 和2类似，但是读取时使用一个独立的线程读取。
将一个523M大小的文件分割成100M的片段。测试三种功能：仅分割(split)、分割+选择列(split+choose)、分割+过滤行(split+filter)。三种方法用时如下（单位为 分钟:秒）：

| 读取方式/测试功能 | split   | split+choose | split+filter |
|-------------------|---------|--------------|--------------|
| 1                 | 0:39.45 | 0:58.66      | 3:22.43      |
| 2                 | 0:36.29 | 0:56.71      | 3:14.22      |
| 3                 | 2:28.77 | 2:48.10      | 5:47.45      |

由测试结果可见，使用缓存输入后，读取速度的提升并不显著。使用线程之后，读取速度反而大幅下降了。可能是因为线程同步的开销过大。

## 使用示例
将文件分割成100M的片段
```
./CSVSplit.py -s 100M history.csv
```

将文件分割成100M的片段，提取标题写入每个片段中，且只输出标题为code,、close的两列。
```
./CSVSplit.py -s 100M -t -n -c code,close history.csv
```

将文件分割成50K的片段，提取标题写入每个片段中，且只输出开盘价小于等于17000的行。
```
./CSVSplit.py -s 50k -f "int(#:开盘价(元):) <= 17000" -n -t cu1607.csv
```

将文件分割成50K的片段，提取标题写入每个片段中，只输出第1列、第3至5列、第7列，只输出第二列数值小于等于17000的行。
./CSVSplit.py -s 50k -c 1,3-5,7 -f 'int(#2) <= 17000' -t cu1607.csv


## 文件
```
.
├── BufferReader.py 带有缓存的文件行读取器
├── CSVSplit.py 主程序，用于分割CSV文件
├── RandomCSV.py 一个可以生成csv文件的测试工具
├── RowFilter.py 行过滤模块
├── SegmentWriter.py 片段输出模块
└── utils.py 实用工具函数
```

## 用法
```
用法: CSVSplit.py [-h] [-s 分割大小] [-c 列标识符] [-n] [-t] [-e 输入文件编码]
                   [-o 输出文件编码] [-d]
                   文件名

位置参数:
  文件名                要分割的文件

可选参数:
  -h, --help            显示帮助信息并退出
  -s SIZE, --size SIZE  分割大小。可以是整数，如“10240”，或者带单位格式，如“10K”
  -c COLUMN, --column COLUMN
                        只输出指定编号的列。例: "1-3,5"表示输出第1至3列、第5列
  -f FILTER, --filter FILTER
                        选出满足条件的行。使用python表达式作为条件来过滤。
                        其中 “#n” 表示使用第n列的字符串值。若使用了 -n 参数，
                        则 “#:name:” 表示使用标题为"name"的列的字符串值。
                        例：'#1 == "male"' 表示选出第一列值为 male 的行。
  -n, --column-name     使用列的标题（而非编号）作为 -c 参数的值。应与 -t 一起用。
  -t, --title           将第一行作为标题，并添加到每个分割文件中
  -e ENCODING, --encoding ENCODING
                        输入文件的编码。默认使用系统编码
  -o OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                        输出文件的编码。默认使用输入文件的编码（如果有 -e 参数），
                        或者系统编码
  -d, --debug           调试模式

例：CSVSplit.py -s 1M -c 1,3,5,10-20 -e gbk filename.csv
例：CSVSplit.py -s 1048576 -t -c name,gender -n filename.csv
```
```
Usage: CSVSplit.py [-h] [-s SIZE] [-c COLUMN] [-n] [-t] [-e ENCODING]
                   [-o OUTPUT_ENCODING] [-d]
                   filename

positional arguments:
  filename              File to split.

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  Max split size. Can be an integer like "10240", or
                        human readable format like "10K".
  -c COLUMN, --column COLUMN
                        select column by number. Example: "1-3,5" means select
                        the 1st to the 3rd, and the 5th column.
  -f FILTER, --filter FILTER
                        Filter row with specific condition. Use python
                        expression. "#n" means using the string value of n-th
                        column. When using -n, "#:name:" means using the
                        string value of the column whose title is "name".
                        Example: '#1 == "male"'
  -n, --column-name     select column by title instead of id. Should be used
                        with -t.
  -t, --title           use the first line as title and add it to each file.
  -e ENCODING, --encoding ENCODING
                        encoding of input file. Default: system encoding
  -o OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                        encoding of output file. If not set, system encoding
                        or input encoding will be used.
  -d, --debug           debugging.

Example: CSVSplit.py -s 1M -c 1,3,5,10-20 -e gbk filename.csv
Example: CSVSplit.py -s 1048576 -t -c name,gender -n filename.csv
```

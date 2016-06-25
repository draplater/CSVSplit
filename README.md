# CSVSplit
## ���
��������Խ�CSV�ļ��ָ�Ϊָ����С�Ķ���ļ�����֧����ѡ���й��˵Ĺ��ܡ�

## �ص�
- ѡ����ʱ����ʹ���еı�š����������б�ź��еı�ŷ�Χ���硰1-5,7����ʾѡ���1��5�С���7�С�
- ����ʹ���������ʽ����ָ��Ҫ����У����ҳ��ڶ���ֵΪ"male"���С�����Ϊ"age"����Ӧ����ֵС�ڵ���20�ĵ��С�
- ֧�ֽ��ļ���һ�е��������У���д��ָ��ÿ���ļ��Ŀ�ͷ��
- �б�����ʱ������ʹ��������Ϊ�ؼ���ѡ���С�
- �����ļ���Сʱ�������������������������������λ�ĸ�ʽ����"10K"��"1G"�ȡ�
- ֧���ֶ�ָ�������ļ��ı���������ͬ������ļ�����GBK��UTF-8�ȡ�
- ��������У��������������������ʾ��ȡ�ļ��Ľ�������
- �����˶��ַ�ʽ���ж�ȡ�����������Խ����

## ��ͬ��ȡ��ʽ�Ĳ���
���������˶��ַ�ʽ����ȡ�����ļ���
1. ʹ��Python�ļ�����ĵ����������ж���(for i in f)��
2. ����һ�������ļ����棬ÿ�ζ�ȡʱ�ظ�ʹ��f.readline()��ȡ���е����棬�ٴӻ����������
3. ��2���ƣ����Ƕ�ȡʱʹ��һ���������̶߳�ȡ��
��һ��523M��С���ļ��ָ��100M��Ƭ�Ρ��������ֹ��ܣ����ָ�(split)���ָ�+ѡ����(split+choose)���ָ�+������(split+filter)�����ַ�����ʱ���£�
| ��ȡ��ʽ/���Թ��� | split   | split+choose | split+filter |   |
|-------------------|---------|--------------|--------------|---|
| 1                 | 0:39.45 | 0:58.66      | 3:22.43      |   |
| 2                 | 0:36.29 | 0:56.71      | 3:14.22      |   |
| 3                 | 2:28.77 | 2:48.10      | 5:47.45      |   |

�ɲ��Խ���ɼ���ʹ�û�������󣬶�ȡ�ٶȵ���������������ʹ���߳�֮�󣬶�ȡ�ٶȷ�������½��ˡ���������Ϊ�߳�ͬ���Ŀ�������

## ʹ��ʾ��
���ļ��ָ��100M��Ƭ��
```
./CSVSplit.py -s 100M history.csv
```

���ļ��ָ��100M��Ƭ�Σ���ȡ����д��ÿ��Ƭ���У���ֻ�������Ϊcode,��close�����С�
```
./CSVSplit.py -s 100M -t -n -c code,close history.csv
```

���ļ��ָ��50K��Ƭ�Σ���ȡ����д��ÿ��Ƭ���У���ֻ������̼�С�ڵ���17000���С�
```
./CSVSplit.py -s 50k -f "int(#:���̼�(Ԫ):) <= 17000" -n -t cu1607.csv
```

���ļ��ָ��50K��Ƭ�Σ���ȡ����д��ÿ��Ƭ���У�ֻ�����1�С���3��5�С���7�У�ֻ����ڶ�����ֵС�ڵ���17000���С�
./CSVSplit.py -s 50k -c 1,3-5,7 -f 'int(#2) <= 17000' -t cu1607.csv


## �ļ�
.
������ BufferReader.py ���л�����ļ��ж�ȡ��
������ CSVSplit.py ���������ڷָ�CSV�ļ�
������ RandomCSV.py һ����������csv�ļ��Ĳ��Թ���
������ RowFilter.py �й���ģ��
������ SegmentWriter.py Ƭ�����ģ��
������ utils.py ʵ�ù��ߺ���

## �÷�
```
�÷�: CSVSplit.py [-h] [-s �ָ��С] [-c �б�ʶ��] [-n] [-t] [-e �����ļ�����]
                   [-o ����ļ�����] [-d]
                   �ļ���

λ�ò���:
  �ļ���                Ҫ�ָ���ļ�

��ѡ����:
  -h, --help            ��ʾ������Ϣ���˳�
  -s SIZE, --size SIZE  �ָ��С���������������硰10240�������ߴ���λ��ʽ���硰10K��
  -c COLUMN, --column COLUMN
                        ֻ���ָ����ŵ��С���: "1-3,5"��ʾ�����1��3�С���5��
  -f FILTER, --filter FILTER
                        ѡ�������������С�ʹ��python���ʽ��Ϊ���������ˡ�
                        ���� ��#n�� ��ʾʹ�õ�n�е��ַ���ֵ����ʹ���� -n ������
                        �� ��#:name:�� ��ʾʹ�ñ���Ϊ"name"���е��ַ���ֵ��
                        ����'#1 == "male"' ��ʾѡ����һ��ֵΪ male ���С�
  -n, --column-name     ʹ���еı��⣨���Ǳ�ţ���Ϊ -c ������ֵ��Ӧ�� -t һ���á�
  -t, --title           ����һ����Ϊ���⣬����ӵ�ÿ���ָ��ļ���
  -e ENCODING, --encoding ENCODING
                        �����ļ��ı��롣Ĭ��ʹ��ϵͳ����
  -o OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                        ����ļ��ı��롣Ĭ��ʹ�������ļ��ı��루����� -e ��������
                        ����ϵͳ����
  -d, --debug           ����ģʽ

����CSVSplit.py -s 1M -c 1,3,5,10-20 -e gbk filename.csv
����CSVSplit.py -s 1048576 -t -c name,gender -n filename.csv
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

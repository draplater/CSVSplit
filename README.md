# CSVSplit
## ���
��������Խ�CSV�ļ��ָ�Ϊָ����С�Ķ���ļ�����֧����ѡ��Ĺ��ܡ�
## �ص�
- ѡ����ʱ����ʹ���еı�š����������б�ź��еı�ŷ�Χ���硰1-5,7����ʾѡ���1��5�С���7�С�
- ����ʹ���������ʽ����ָ��Ҫ����У����ҳ��ڶ���ֵΪ"male"���С�����Ϊ"age"����Ӧ����ֵС�ڵ���20�ĵ��С�
- ֧�ֽ��ļ���һ�е��������У���д��ָ��ÿ���ļ��Ŀ�ͷ��
- �б�����ʱ������ʹ��������Ϊ�ؼ���ѡ���С�
- �����ļ���Сʱ�������������������������������λ�ĸ�ʽ����"10K"��"1G"�ȡ�
- ֧���ֶ�ָ�������ļ��ı���������ͬ������ļ�����GBK��UTF-8�ȡ�
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
                        ���� ��#n�� ��ʾʹ�õ�n�е��ַ���ֵ����ʹ���� -t ������
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
                        column. When using -t, "#:name:" means using the
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

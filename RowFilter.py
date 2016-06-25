import re


class RowFilter:
    """
    filter rows in csv file
    """
    def __init__(self, expression, row_names=None):
        """
        create a new RowFilter.
        :param expression:  Use python
                        expression. "#n" means using the string value of n-th
                        column. When using -t, "#:name:" means using the
                        string value of the column whose title is "name".
        :param row_names: the name list of each column.
        """
        # $1 == 5 -> data[1] == 5
        self.expression = re.sub(r"#(\d+)(?=[^\d])", r"data[\1]", expression)
        self.row_names = row_names
        if self.row_names:
            # #:name: == 5 -> named_data["name"] == 5
            self.expression = re.sub(r"#:(.+):", r'named_data["\1"]',
                                     self.expression)

    def filter(self, line):
        """
        :param line: csv data line
        :return: a Bool represent whether this line show be kept.
        """
        data = [None] + line.split(",")  # make it start from 1 instead of 0
        if self.row_names:
            named_data = {self.row_names[i]: data[i+1] for i in range(len(self.row_names))}
        return eval(self.expression)
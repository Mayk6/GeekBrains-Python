from statistics import mean


class AverageStat:

    def __init__(self):
        self.numbers = None

    def add_number(self, number):
        if self.numbers is None:
            self.numbers = []
        self.numbers.append(number)

    def result(self):
        if type(self.numbers) is list:
            return float(mean(self.numbers))
        return self.numbers


class MinStat:

    def __init__(self):
        self.numbers = None

    def add_number(self, number):
        if self.numbers is None:
            self.numbers = []
        self.numbers.append(number)

    def result(self):
        if type(self.numbers) is list:
            return min(self.numbers)
        return self.numbers


class MaxStat:

    def __init__(self):
        self.numbers = None

    def add_number(self, number):
        if self.numbers is None:
            self.numbers = []
        self.numbers.append(number)

    def result(self):
        if type(self.numbers) is list:
            return max(self.numbers)
        return self.numbers


class Table:

    def __init__(self, rows, cols):
        self.table = [[0] * cols for i in range(rows)]

    def get_value(self, row, col):
        try:
            if col < 0 or row < 0:
                return None
            return self.table[row][col]
        except IndexError:
            return None

    def set_value(self, row, col, value):
        if self.get_value(row, col) is not None:
            self.table[row][col] = value

    def n_cols(self):
        return len(self.table[0])

    def n_rows(self):
        return len(self.table)

    def delete_row(self, row):
        del self.table[row]

    def delete_col(self, col):
        for index_col in range(self.n_cols()):
            del self.table[i][col]

    def add_row(self, row):
        self.table.insert(row, [0] * self.n_cols())

    def add_col(self, col):
        index_col = 0
        while index_col < self.n_cols():
            self.table[index_col].insert(col, 0)
            index_col += 1

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        f'Sum of cell is: {self.nums + other.nums}'

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Error'

    def __mul__(self, other):
        return f'Multiply of cell is: {self.nums * other.nums}'

    def __floordiv__(self, other):
        return f'Truediv of cell is: {self.nums // other.nums}'


cell_1 = Cell(11)
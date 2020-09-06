a = [[2, 4, 1, 7], [3, 3, 3, 7], [9, 0, 5, 0]]
b = [[1, 3, 2, 6], [2, 2, 2, 2], [8, 1, 4, 1]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists)):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: ' '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda  r_1, r_2: map(lambda x, y: x+y, r_1, r_2), self.matrix, other.matrix))

m1 = Matrix([[1, 2, 3], [3, 4, 5], [1, 2]])
m2 = Matrix([[9, 8, 7], [7, 6, 5]])

print(m1)
print(m2)

s = m1 + m2
print(s)

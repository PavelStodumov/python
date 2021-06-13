class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return '\n'.join(list(map(lambda x: ' '.join(list(map(lambda y: str(y), x))), self.matrix_list)))

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix_list)):
            _result = []
            for j in range(len(self.matrix_list[0])):
                _result.append(self.matrix_list[i][j] + other.matrix_list[i][j])
            result.append(_result)
        return Matrix(result)


mat1 = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 5], [5, 4, 3, 2, 6]])
mat2 = Matrix([[4, 2, 2, 4, 6], [3, 4, 6, 7, 9], [1, 3, 2, 7, 8]])
mat3 = mat1 + mat2
print(mat3)

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_n = matrix.copy()
    for i in range(len(matrix)):
        matrix_n[i] = list(map(lambda x: x**2, matrix[i]))
        return (matrix_n)

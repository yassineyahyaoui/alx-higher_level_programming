#!/usr/bin/python3
def matrix_divided(matrix, div):
    s = 'matrix must be a matrix (list of lists) of\
 integers/floats'
    if not matrix or type(matrix) is not list:
        raise TypeError(s)
    for row in matrix:
        if type(row) is list and row:
            for ele in row:
                if type(ele) is not int and type(ele) is not float:
                    raise TypeError(s)
        else:
            raise TypeError(s)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    matrix2 = list(map(list, matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix2[row][col] = round(matrix[row][col] / div, 2)

    return matrix2

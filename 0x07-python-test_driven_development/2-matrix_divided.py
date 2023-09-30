#!/usr/bin/python3
"""matrix division madule"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    args:
        matrix: givin matrix
        div: the number that the matrix is divided by

    raises:
        TypeError: if matrix is not a list of lists containing int or float
        TypeError: if each row of the matrix doesn't have the same size
        TypeError: if div is not int or float
        ZeroDivisionError: if div is zero

        return:
            new_list: new matrix with the result
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) of len(matix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]

    if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")


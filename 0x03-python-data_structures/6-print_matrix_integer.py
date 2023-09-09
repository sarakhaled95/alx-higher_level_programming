#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for s in matrix:
        if len(s) == 0:
            print()
        for i in range(len(s)):
            print("{:d}".format(s[i]), end="\n" if i is len(s) - 1 else " ")

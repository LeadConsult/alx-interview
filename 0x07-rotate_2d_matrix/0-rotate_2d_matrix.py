#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    R0tate 2D square matrix by 90 degrees
    Args:
        matrix (list): 2D square
    Return:
        None
    """
    n = len(matrix)
    for x in range(n):
        for y in range(x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = temp

    for x in range(n):
        for y in range(int(n / 2)):
            temp = matrix[x][y]
            matrix[x][y] = matrix[x][n-1-y]
            matrix[x][n-1-y] = temp

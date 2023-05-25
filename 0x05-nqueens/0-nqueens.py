#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_queen = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_queen < 4:
    print('N must be at least 4')
    exit(1)


def solve_n_queen(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n == 0:
        return [[]]
    inner_solution = solve_n_queen(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_queen)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def queen_attack(square, queen):
    """_summary_

    Args:
        square (_type_): _description_
        queen (_type_): _description_

    Returns:
        _type_: _description_
    """
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    """_summary_

    Args:
        sqr (_type_): _description_
        queens (_type_): _description_

    Returns:
        _type_: _description_
    """
    for each in queens:
        if queen_attack(sqr, each):
            return False
    return True


for solution in reversed(solve_n_queen(n_queen)):
    result = []
    for p in [list(p) for p in solution]:
        result.append([i - 1 for i in p])
    print(result)
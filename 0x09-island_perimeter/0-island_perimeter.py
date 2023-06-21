#!/usr/bin/python3
"""
0x09. Island Perimeter
"""


def island_perimeter(grid):
    """a function def island_perimeter(grid): that returns the perimeter
    of the island described in grid
    """

    perimeter = 0

    # Check if the input is a list
    if type(grid) != list:
        return 0

    n = len(grid)

    # Iterate over each row in the grid
    for i, row in enumerate(grid):
        m = len(row)

        # Iterate over each cell in the row
        for j, cell in enumerate(row):
            if cell == 0:
                continue

            # Check the neighboring cells to determine the edges
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )

            # Add the number of edges to the perimeter
            perimeter += sum(edges)

    return perimeter

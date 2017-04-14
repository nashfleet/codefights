"""
Sudoku is a number-placement puzzle. The objective is to fill a
    9 × 9 grid with digits so that each column, each row, and
    each of the nine 3 × 3 sub-grids that compose the grid
    contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers
    represents a correct solution to Sudoku.
"""


def sudoku(grid):
    for i in range(9):
        # Horizontal rows
        if sorted(grid[i]) != list(range(1, 10)):
            return False

        # Vertical Rows
        b = []
        for j in range(9):
            b.append(grid[j][i])
        if sorted(b) != list(range(1, 10)):
            return False
    # 3x3 cubes
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            c = []
            c.extend((grid[k][l],   grid[k + 1][l],   grid[k + 2][l]))
            c.extend((grid[k][l + 1], grid[k + 1][l + 1], grid[k + 2][l + 1]))
            c.extend((grid[k][l + 2], grid[k + 1][l + 2], grid[k + 2][l + 2]))
            if sorted(c) != list(range(1, 10):
                return False
    return True

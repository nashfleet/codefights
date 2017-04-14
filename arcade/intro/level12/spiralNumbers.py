"""
Construct a square matrix with a size N × N containing integers
from 1 to N * N in a spiral order, starting from top-left and
in clockwise direction.
"""


def spiralNumbers(n):
    a = [[0 for x in range(n)] for y in range(n)]
    b = 0
    position = (0, 0)
    dir = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    for i in range(1, n * n + 1):
        a[position[0]][position[1]] = i
        next = position[0] + dir[b][0], position[1] + dir[b][1]
        if not (0 <= next[0] < n and 0 <= next[1] < n and a[next[0]][next[1]] == 0):
            b = (b + 1) % 4
            next = position[0] + dir[b][0], position[1] + dir[b][1]
        position = next
    return a

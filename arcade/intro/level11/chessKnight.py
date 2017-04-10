"""
Given a position of a knight on the standard chessboard, find
    the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally
    and one square vertically, or two squares vertically and one
    square horizontally away from it. The complete move
    therefore looks like the letter L.
"""


def chessKnight(cell):
    r = ord(cell[0]) - 96
    c = int(cell[1])

    if 3 <= r <= 6 and 3 <= c <= 6:
        return 8
    elif ((r == 2 or r == 7) and (c == 1 or c == 8)) or ((r == 1 or r == 8) and (c == 2 or c == 7)):
        return 3
    elif (r == 1 or r == 8) and (c == 1 or c == 8):
        return 2
    elif (r == 1 or r == 8 or c == 1 or c == 8):
        return 4
    elif (r == 2 or r == 7) and (c == 2 or c == 7):
        return 4
    elif (r == 2 or r == 7 or c == 2 or c == 7):
        return 6

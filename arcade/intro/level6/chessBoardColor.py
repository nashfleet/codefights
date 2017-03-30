"""
Given two cells on the standard chess board, determine whether they
    have the same color or not. Example (A1, C3).
"""
def chessBoardCellColor(x, y):
    a = ord(x[0]) + int(x[1])
    b = ord(y[0]) + int(y[1])
    
    return a % 2 == b % 2
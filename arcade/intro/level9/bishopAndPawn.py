"""
Given the positions of a white bishop and a black pawn on the
  standard chess board, determine whether the bishop can capture
  the pawn in one move.

The bishop has no restrictions in distance for each move, but is
  limited to diagonal movement.
"""


def bishopAndPawn(bishop, pawn):
    return (bishop[0] != pawn[0]) and (abs(ord(bishop[0]) - ord(pawn[0])) == abs(int(bishop[1]) - int(pawn[1])))

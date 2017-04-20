"""
Presented with the integer n, find the 0-based position of the second
  rightmost zero bit in its binary representation (it is guaranteed
  that such a bit exists), counting from right to left.

Return the value of 2position_of_the_found_bit.
"""


def secondRightmostZeroBit(n):
    return 2**(len(bin(n)[2:]) - 1 - bin(n)[2:].rfind('0', 0, len(bin(n)[2:]) - (len(bin(n)[2:]) - bin(n)[2:].rfind('0'))))

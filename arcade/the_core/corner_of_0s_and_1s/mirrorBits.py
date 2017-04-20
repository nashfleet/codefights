"""
Reverse the order of the bits in a given integer.
"""


def mirrorBits(a):
    return int(str(bin(a))[:1:-1], 2)

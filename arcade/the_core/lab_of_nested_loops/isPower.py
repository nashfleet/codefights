"""
Determine if the given number is a power of some non-negative integer.
"""


def isPower(n):
    if n == 1:
        return True
    for i in range(0, n // 2):
        for j in range(2, n // 2):
            if i**j == n:
                return True
    return False

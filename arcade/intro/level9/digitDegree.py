"""
Let's define digit degree of some positive integer as the number
  of times we need to replace this number with the sum of its
  digits until we get to a one digit number.

Given an integer, find its digit degree.
"""


def digitDegree(n):
    a = 0
    while len(str(n)) > 1:
        a += 1
        n = sum(map(int, str(n)))
    return a

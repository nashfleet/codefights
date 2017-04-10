"""
Given some integer, find the maximal number you can obtain by
  deleting exactly one digit of the given number.
"""


def deleteDigit(n):
    return (max([int(str(n)[:i] + str(n)[i + 1:]) for i in range(len(str(n)))]))

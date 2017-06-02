"""
Your friend has been doodling during the lecture and wrote down several
  digits in a circle. You're wondering if these digits might form the
  password to your friend's computer. You're planning to prank him
  some time in the future, and hacking into his computer will
  definitely help. If the digits written in the clockwise order indeed
  form a password, all you need to do is figure out which digit comes
  in it first.

Given a list of digits as they are written in the clockwise order,
  find all other combinations the password could possibly have.
"""
from collections import deque


def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda d: res[d].rotate(-d), range(n)), 0)
    return [list(d) for d in res]

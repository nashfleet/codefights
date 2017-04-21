"""
A little boy is studying arithmetics. He has just learned how to
  add two integers, written one below another, column by column.
  But he always forgets about the important part - carrying.

Given two integers, find the result which the little boy will get.
"""


def additionWithoutCarrying(param1, param2):
    s = 0
    t = 1
    while param1 > 0 or param2 > 0:
        s += t * ((param1 + param2) % 10)
        param1 //= 10
        param2 //= 10
        t *= 10
    return s

"""
Consider a sequence of numbers a0, a1, ..., an, in which an element is
  equal to the sum of squared digits of the previous element. The
  sequence ends once an element that has already been in the sequence
  appears again.

Given the first element a0, find the length of the sequence.
"""


def squareDigitsSequence(a0):
    l = []
    while a0 not in l:
        l.append(a0)
        b = 0
        for i in str(a0):
            b += int(i)**2
        a0 = b
    return len(l) + 1

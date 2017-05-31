"""
A pair of numbers is considered to be cool if their product is
  divisible by their sum. More formally, a pair (i, j) is cool
  if and only if (i * j) % (i + j) = 0.

Given two lists a and b, find cool pairs with the first number
  in the pair from a, and the second one from b. Return the number
  of different sums of elements in such pairs.
"""


def coolPairs(a, b):
    uniqueSums = {(i + j) for i in a for j in b if (((i * j) % (i + j)) == 0)}
    return len(uniqueSums)

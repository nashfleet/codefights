"""
Define an integer's roundness as the number of trailing zeroes in it.

Given an integer n, check if it's possible to increase n's roundness
  by swapping some pair of its digits.
"""


def increaseNumberRoundness(n):
    return "0" in str(n).rstrip("0")

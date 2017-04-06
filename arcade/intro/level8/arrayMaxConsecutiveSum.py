"""
Given array of integers, find the maximal possible sum of some
  of its k consecutive elements.
"""


def arrayMaxConsecutiveSum(inputArray, k):
    return max([sum(inputArray[x:x + k]) for x in range(0, len(inputArray) - k + 1)])

"""
Determine whether the given string can be obtained by one
  concatenation of some string to itself.
"""


def isTandemRepeat(inputString):
    return inputString[len(inputString) // 2:] == inputString[:len(inputString) // 2]

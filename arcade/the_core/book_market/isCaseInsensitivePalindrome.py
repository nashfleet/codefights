"""
Given a string, check if it can become a palindrome through a
  case change of some (possibly, none) letters.
"""


def isCaseInsensitivePalindrome(inputString):
    return inputString.lower() == inputString.lower()[::-1]

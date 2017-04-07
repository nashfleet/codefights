"""
Given a string, find the shortest possible string which can be
  achieved by adding characters to the end of initial string to
  make it a palindrome.
"""


def buildPalindrome(st):
    a = st
    for i in range(10):
        if a == a[::-1]:
            return a
        a = st
        a += a[i::-1]
    return a

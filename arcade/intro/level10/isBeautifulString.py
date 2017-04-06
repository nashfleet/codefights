"""
A string is said to be beautiful if b occurs in it no more times
  than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.
"""


def isBeautifulString(inputString):
    for c in string.ascii_lowercase:
        if inputString.count(c) < inputString.count(chr(ord(c) + 1)):
            return False
    return True

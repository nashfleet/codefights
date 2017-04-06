"""
Find the leftmost digit that occurs in a given string.
"""


def firstDigit(i):
    return i[re.search("\d", i).start()]

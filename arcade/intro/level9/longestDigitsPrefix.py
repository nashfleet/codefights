"""
Given a string, output its longest prefix which contains
  only digits.
"""


def longestDigitsPrefix(inputString):
    return re.findall('^\d*', inputString)[0]

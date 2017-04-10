"""
Define a word as a sequence of consecutive letters. Find the
  longest word from the given string.
"""


def longestWord(text):
    return max(re.findall("[a-zA-Z]+", text), key=len).split()[0]

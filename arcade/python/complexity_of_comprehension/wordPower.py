"""
You've heard somewhere that a word is more powerful than an action.
  You decided to put this statement at a test by assigning a power
  value to each action and each word. To begin somewhere, you defined
  a power of a word as the sum of powers of its characters, where
  power of a character is equal to its 1-based index in the plaintext
  alphabet.

Given a word, calculate its power.
"""


def wordPower(word):
    num = {chr(i + 96): i for i in range(1, 27)}
    return sum([num[ch] for ch in word])

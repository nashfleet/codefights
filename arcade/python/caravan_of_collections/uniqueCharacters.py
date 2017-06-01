"""
You need to compress a large document that consists of a small
  number of different characters. To choose the best encoding
  algorithm, you would like to look closely at the characters
  that comprise this document.

Given a document, return an array of all unique characters that
  appear in it sorted by their ASCII codes.
"""


def uniqueCharacters(document):
    return sorted(set(document))

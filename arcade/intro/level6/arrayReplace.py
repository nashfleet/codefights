"""
Given an array of integers (a), replace all the 
  occurrences of r with s.
"""
def arrayReplace(a, r, s):
    return [x if x != r else s for x in a]
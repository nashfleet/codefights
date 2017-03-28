"""
Given a string (s), replace each its character by the next one in the English 
  alphabet (z would be replaced by a).
"""
def alphabeticShift(s):
     return ''.join(chr(ord(i)+1) for i in s).replace("{","a")

    
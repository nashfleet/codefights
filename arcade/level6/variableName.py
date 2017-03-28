"""
Correct variable names consist only of Latin letters, digits and underscores 
  and they can't start with a digit.

Check if the given string is a correct variable name (n).
"""
import re
def variableName(n):
    return (re.match("^[A-Za-z_]{1}[\w_]*$", n) != None)

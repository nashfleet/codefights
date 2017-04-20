"""
You are given an array of up to four non-negative integers,
  each less than 256.

Your task is to pack these integers into one number M in the
  following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.
"""


def arrayPacking(a):
    return sum(a[i] << 8 * i for i in range(len(a)))

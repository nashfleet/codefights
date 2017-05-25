"""
Given a number num in its binary representation, your task is to sum all the numbers in base 10 formed by the prefixes of num. More formally, sum up int(num[0, i]) for all possible i.

Since the answer can be very big, return it modulo 109 + 7.
"""


def totalBinSum(n):
    n = int(n, 2)
    x = 0
    while n:
        x += n
        n >>= 1
    return x % (10**9 + 7)

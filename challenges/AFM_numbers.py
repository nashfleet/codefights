"""
Reverse challenge
"""


def AFM_numbers(b):
    a = int((-1)**b + 2**(1 + b) - 3) / 6
    return [a, a * 2 + b % 2]

"""
Reverse challenge
"""


def AFM_numbers(b):
    a = int((1 / 6) * (-3 + (-1)**b + 2**(1 + b)))
    return [a, a * 2 + b % 2]

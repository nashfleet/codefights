"""
Given an integer product, find the smallest positive integer the
    product of whose digits is equal to product. If there is no
    such integer, return -1 instead.
"""


def digitsProduct(product):
    a = 0
    b = []

    if product == 0:
        return 10
    elif product == 1:
        return 1

    for c in range(9, 1, -1):
        while product % c == 0:
            product /= c
            b.append(c)
        print(b)

    if product > 1:
        return -1

    for i in range(len(b) - 1, -1, -1):
        a = 10 * a + b[i]
    return a

"""
Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.

How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [L, R], and each number feels comfortable with the other?
"""


def comfortableNumbers(L, R):
    a = []
    e = {}

    for z in range(L, R + 1):
        e[z] = sum(int(l) for l in str(z))

    for i in range(L, R + 1):
        for j in range(i, R + 1):
            if i == j:
                continue
            if ((j - e[j]) <= i <= (j + e[j])) and ((i - e[i]) <= j <= (i + e[i])):
                d = sorted([i, j])
                if d not in a:
                    a.append(d)
    return len(a)

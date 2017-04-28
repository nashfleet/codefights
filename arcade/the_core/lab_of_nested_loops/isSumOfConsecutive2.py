"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

"""


def isSumOfConsecutive2(n):
    a = 0
    for i in range(1, n):
        for j in range(1, n):
            if sum(range(i, i + j)) == n:
                a += 1
    return a

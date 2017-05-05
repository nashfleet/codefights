"""
We define the weakness of number x as the number of positive integers
    smaller than x that have more divisors than x.

It follows that the weaker the number, the greater overall weakness
    it has. For the given integer n, you need to answer two questions:

what is the weakness of the weakest numbers in the range [1, n]?
how many numbers in the range [1, n] have this weakness?
Return the answer as an array of two elements, where the first element
    is the answer to the first question, and the second element is the
    answer to the second question.
"""


def weakNumbers(n):
    weakest = 0
    weakCount = 0
    i = 0
    div = 0
    divisors = []

    for i in range(1, n + 1):
        div = numberOfDivisors(i)
        divisors.append(div)
        k = 0
        for j in range(i, 0, -1):
            if divisors[j - 1] > div:
                k += 1
        if k > weakest:
            weakest = k
            weakCount = 1
        elif k == weakest:
            weakCount += 1
    return [weakest, weakCount]


def numberOfDivisors(x):
    a = 0
    for i in range(1, x + 1):
        if x % i == 0:
            a += 1
    return a

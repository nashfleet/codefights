"""
Reverse challenge
"""


def orezRoEno(k):
    c = bin(k).count
    return c('1') | c('0') - 1

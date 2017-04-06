"""
Given an array of equal-length strings, check if it is possible to
    rearrange the strings in such a way that after the rearrangement
    the strings at consecutive positions would differ by exactly one
    character.
"""


def stringsRearrangement(a):
    def recurse(deep, a):
        if deep == len(a):
            for i in range(0, len(a) - 1):
                diff = 0
                for j in range(len(a[i])):
                    if a[i][j] != a[i + 1][j]:
                        diff += 1
                if diff != 1:
                    return False
            return True
        for i in range(deep, len(a)):
            a[deep], a[i] = a[i], a[deep]
            if(recurse(deep + 1, a)):
                return True
            a[deep], a[i] = a[i], a[deep]
        return False
    return recurse(0, a)


"""
You've been trying to crack the password from your friend's laptop
  (just to prank him, malicious intent!), but with no luck. However,
  looks like you're finally up to something: you checked the keyboard
  with the "little detective" game set and determined that the password
  consists of a limited set of digits.

You've seen your friend typing the password quite a few times, and are
  now sure that it consists of k digits. You also know that he is very
  superstitious and believes in the power of number d, so the password
  is apt to be divisible by it.

Given the digits that comprise the password, its length k and the number
d by which it is divisible, return a sorted list of strings that should
be tried as passwords.
"""
from itertools import combinations_with_replacement, permutations, product


def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return [i for i in sorted([createNumber(i) for i in set(
        list(product(createNumber(digits), repeat=k)))]) if (
        (int(i) % d == 0) or (int(i.lstrip("0")) % d == 0)
    )]

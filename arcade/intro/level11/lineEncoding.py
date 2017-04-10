"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of
    disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced
    with a concatenation of its length and the repeating
    character

for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the
    same order and a new string is returned.
"""


def lineEncoding(s):
    b = ""
    c = 1
    for i in range(0, len(s)):
        if len(s) - 1 == i or s[i] != s[i + 1]:
            if c > 1:
                b += str(c)
            c = 1
            b += s[i]
        else:
            c += 1
    return b

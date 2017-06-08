"""
https://codefights.com/challenge/CBiayArRfZEyDDGX8
"""


Nav = lambda d: [d.count(i) - d.count(j) for i, j in zip("v>+", "^<-")]

"""
https://codefights.com/challenge/CBiayArRfZEyDDGX8
"""


Nav = lambda d: [d.count('v') - d.count('^'), d.count('>') -
                 d.count('<'), d.count('+') - d.count('-')]

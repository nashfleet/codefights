"""
Check if the given string is a correct time representation of
  the 24-hour clock.
"""


def validTime(time):
    return (0 <= int(time[:2]) <= 23 and 0 <= int(time[3:]) <= 59)

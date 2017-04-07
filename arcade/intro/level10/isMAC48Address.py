"""
A media access control address (MAC address) is a unique
  identifier assigned to network interfaces for communications
  on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in
  human-friendly form is six groups of two hexadecimal digits (0
  to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it
  corresponds to MAC-48 address or not.
"""


def isMAC48Address(inputString):
    return bool(re.compile('^([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2})$').match(inputString))

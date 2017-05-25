"""
A rectangle with sides equal to even integers a and b is drawn on the
  Cartesian plane. Its center (the intersection point of its diagonals)
  coincides with the point (0, 0), but the sides of the rectangle are
  not parallel to the axes; instead, they are forming 45 degree angles
  with the axes.

How many points with integer coordinates are located inside the given
  rectangle (including on its sides)?
"""


def rectangleRotation(a, b):
    c = 1.414
    a = int(a / c)
    b = int(b / c)
    c = ~(a ^ b) & 1
    return 2 * a * b + a + b + c
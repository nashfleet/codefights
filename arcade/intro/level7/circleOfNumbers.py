"""
Consider integer numbers from 0 to n - 1 written down along the circle
  in such a way that the distance between any two neighbouring numbers 
  is equal (note that 0 and n - 1 are neighbouring, too).

Given n and firstNumber, find the number which is written in the radially 
  opposite position to firstNumber (f).
"""
def circleOfNumbers(n, f):
    return (f + n//2) % n

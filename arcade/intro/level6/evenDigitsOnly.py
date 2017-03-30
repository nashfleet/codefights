"""
Check if all digits of the given integer are even.
"""
def evenDigitsOnly(n):
    return all([int(x)%2 == 0 for x in str(n)])
        

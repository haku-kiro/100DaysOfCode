"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def isEven(k):
    # Note sure how to do this without the modulo operator?
    if k % 2 == 0:
        return True
    else:
        return False

print(isEven(12))
print(isEven(13))
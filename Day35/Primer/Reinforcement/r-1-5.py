"""
Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
"""

def KindOfPointLess(n):
    elSum = sum([(k * k) for k in range(n+1)], 0)
    print(elSum)
    # this needs to square the numbers before summing?

KindOfPointLess(100) # looks right
    
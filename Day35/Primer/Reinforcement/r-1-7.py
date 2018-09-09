"""
Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.
"""
def theOddOnes(n):
    # stil have to do the positive check...
    if n <=0: return
    
    # Might be able to modify this to have the less than zero check
    elSum = sum([k for k in range(n + 1) if k % 2 != 0], 0)
    return elSum

print(theOddOnes(10)) # should be 25
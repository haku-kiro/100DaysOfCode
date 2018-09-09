"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
# two to the power of the index ... you silly, silly man...
theOneListToRuleThemAll = [2**k for k in range(0, 9)]
print(theOneListToRuleThemAll)
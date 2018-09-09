"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""

# My pseudo code:
"""
iterate over a list from the last element to the first, add the that element a collection to create a reversed collection
"""

data = [1,2,42,87,9,12,10,11]

# method:
print("Correct:")
for x in reversed(data):
    print(x) # This is what we want to replicate, going to use a generator

# working generator
def rev(col):
    for item in range(len(col)-1, -1, -1): # this is hard to look at
        yield col[item]

print("\nMy solution:")
for x in rev(data):
    print(x)
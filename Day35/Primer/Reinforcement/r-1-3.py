"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(data):
    min = data[0]
    max = data[0]
    for item in data:
        if item < min:
            min = item
        if item > max:
            max = item
    return (min,max)

list = [1,23,2,12,42,53,1,341234,123]

min,max = minmax(list)

print("The min value was: ", min)
print("The max value was: ", max)
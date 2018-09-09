"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def squares(n):
    if n <= 0:
        return # trying the blank return with a generator
    else:
        for num in range(n + 1):
            yield num * num

for num in squares(100):
    print(num) # accessing the generator without the next() method

# Lol I misread - need to return the sum:

def sumMeThen(n):
    sum = 0
    for x in squares(n):
        sum += x
    return sum

print(sumMeThen(100))
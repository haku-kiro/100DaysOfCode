"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

def sumTheOddOnes(n):
    if n <=0: return
    elSum = 0
    for num in range(n + 1):
        if num % 2 != 0:
            elSum += num
    return elSum

print(sumTheOddOnes(10)) 
# This file will demo a way of evaluating the run time of something

from time import time
start_time = time() # recording the starting time

# run something
something_random = 1 
for x in range(100000):
    something_random *= x

end_time = time()  # the ending time

elapsed = end_time - start_time # the elapsed time
print(f'Took {elapsed} seconds to run')

# kind of nice for basic testing
def runTimer(method, data, iter):
    start_time = time()

    for x in range(iter):
        method(data)
    
    end_time = time()
    elapsed = end_time - start_time
    return f"{method} ran for {iter} iterations and took: {elapsed} seconds"


"""
When analyzing the run time of an algorithm, take the following primative pseudo code actions into account
Checking to see how many of the following your alg use can help you asses the complexity as well 
as the runtime

• Assigning an identifier to an object
• Determining the object associated with an identifier
• Performing an arithmetic operation (for example, adding two numbers)
• Comparing two numbers
• Accessing a single element of a Python list by index
• Calling a function (excluding operations executed within the function)
• Returning from a function.


NOTE: Page 115 contains a list of the functions that are used in the book
"""

# some algs grow proportionally based on the value of n, such as finding the max value of a list:

def find_max(data):
    """
    Finds the max value in data
    """
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest

# as the size of data increases the run time increases
# this alg runs at O(n) 


testList = [12,31,23,1,23,1,2,31,23,1,23,1,3,1,12,535,2,31,23,235,1234,126]

# quadratic time alg (version 1)
def prefix_average(s):
    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
    """
    n = len(s)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += s[i]
        A[j] = total / (j + 1)
    return A


theValueOfA = prefix_average(testList)
print(theValueOfA)


# quadratic time alg (version 2)
def prefix_average2(s):
    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
    """
    n = len(s)
    A = [0] * n
    for j in range(n):
        A[j] = sum(s[0:j+1]) / (j + 1)
    return A

secondValueOfA = prefix_average2(testList)
print(secondValueOfA)

# quadratic time alg (version 3)

def prefix_average3(s):
    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
    """
    # supposedly the faster version
    n = len(s)
    A = [0] * n
    total = 0
    for j in range(n):
        total+= s[j]
        A[j] = total / (j + 1)
    return A

"""
In algorithm
prefix average3, we maintain the current prefix sum dynamically, effectively
computing S[0]+S[1]+· · ·+S[ j] as total + S[j],
"""


theThirdValueOfA = prefix_average3(testList)
print(theThirdValueOfA)

iterations = 1000000 # at this amount of iterations, the results are very surprising.

# having a pre-calc'd value stored takes a lot from the processing time

method1 = runTimer(prefix_average, testList, iterations)
method2 = runTimer(prefix_average2, testList, iterations)
method3 = runTimer(prefix_average3, testList, iterations)

print(method1)
print(method2)
print(method3)

# you can see that method 3 runs the quickest, bec the total is no recalced each time?

# Learnt about generators:
# They are used to define elements of a sequence

# you can create a method that returns this sequence, instead of a generic method.
# Say you wanted a method that returns the factors of a number

# You could do this:
def getFactors(n):
    results = []
    for num in range(1, n+1):
        if n % num == 0:
            results.append(num)
    return results

# to implement a generator, you would use the yield kw - without a result set
def factorGenerator(n):
    for num in range(1, n+1):
        if n % num == 0:
            yield num # meaning it would be added to the returning sequence - note, you can't use the return kw and the yield kw in the same method
                    # The exception to this would be the zero result `return` statement to break out of a method/iteration

print(getFactors(100))

# This is not how you would call a generator (The nice thing is that it doesn't keep the entire sequence in memory - it computes it as a result)
print(factorGenerator(100))

# To call it:
sequenceOfFactors = factorGenerator(100)

for factor in sequenceOfFactors:
    print(factor)

# if not iterating - you could use the next() method

# Page 49 - Has some Existing modules that are quite useful for data structures

import random 

# to make a random list:
list = [x for x in range(1,100)]
random.shuffle(list)

for x in list:
    print(x) # TODO: do the reinforcement exercises. Page 51
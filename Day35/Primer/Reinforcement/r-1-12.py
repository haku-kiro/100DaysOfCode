"""
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""

import random

# the choice method:

def MyChoice(data):
    # not really a choice ... ah c'est la vie mon ami
    dataLen = len(data)
    randomIndex = random.randrange(0, dataLen) # assuming wont return the final index? Should test. Correct - doesnt return the stop parm (Unless you're  really lucky/unlucky.. read the docs you lazy bugger... This is a long - and unnecessary comment...)
    return data[randomIndex]

# testing:
list = [1,2,3,4,5,6,7,8,9]
print(MyChoice(list))


# TODO: there are creativity questions as well as project questions - should look into this as practise at some point


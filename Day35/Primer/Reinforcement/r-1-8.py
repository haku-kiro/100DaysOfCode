"""
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
the same element?
"""

# nice one - making me thing and stuff...
testString = "This is a value" 
# where 
print(testString[0]) # is T
print(testString[-1]) # is e

# what would the negative value need to be to return the same char?
print(testString[len(testString)-1]) # would be the last char
print(len(testString)) 

print(testString[-len(testString)]) # so the negative value of the length would return the first char, then plus one to return the second last char etc ?

# Lets test:
def Test(s):
    for index in range(len(s) + 1): # up to and including 
        print(s[-index], -index) # first to next char

Test("Value") # prints the string backwards - can't help but feel as if I've gone down an incorrect tangent... 



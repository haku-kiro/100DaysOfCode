# This covers the sorting section of <https://developers.google.com/edu/python/sorting>

# The easist way to sort; And often, the best way to sort is the sort function (on a list)

aList = [1,54,42,12,90]
aList.sort() # sorts the list in place
print(aList)

# to sort a collection, you can use the sorted method, this returns a sorted collection
aDict = {1: 123, 4: 42, 2: 12}
print(sorted(aDict)) # returns the keys, sorted
aTuple = (12,235,123,64,2134,635,13)
print(sorted(aTuple,reverse=True)) # note that you can also reverse the order that it is printed (instead of sorting and using the reverse method/writing your own)

# Custom sorting with key= (This can be used for the exercise in the list1.py file that you took forever to do)

# key transforms each element before comparison, takes in a single value and returns a single value, that returned value is the value used in the sort (a 'proxy' value)

stringList = ["Test", "Not a test", "short", "A much longer string", "a", "few", "short ones"]
print(sorted(stringList, key=len))

# This is how you should have done the exercise (Wow, I'm kind of mad at myself...)
def GetLast(tuple):
    return tuple[-1] # returns the last element in the tuple

tupleList = [(1,3,2), (23,12,3), (42,42,1)]
print(sorted(tupleList, key=GetLast))

# another use of the key param is to use the .lower method to make sure each element is treated case-insensitive

print(sorted(stringList, key=str.lower)) # Keep in mind that you have to spec the type here (has to be of type string (len can be used with out type, lower cannot))
# I get weird results with the above though

# They give the answer to one of the questions ...

# Tuples
# 
# Are a fixed sized grouping of elements
# such as x,y cords (A vector etc)
# 
# they are immutable and do not change size
# You can use them as a sort of struct like data type, returning a list of them if required etc

tupleTest = (1,2,3,4, "Test")
print(len(tupleTest))
print(tupleTest[2]) 
#tupleTest[1] = "Another value" # throws an error, cant change the value- immutable  
# can change the definition of the tuple though
tupleTest = ("New", "values")
print(tupleTest)

# to create a tuple that is one in length, you have to use a comma still. This is to differentiate between bracket syntax and tuples
singleTuple = ("One value",)

# assigning a tuple to another tuple sets the values, this works for lists too - you have to set the same length to one another though - or it would throw an error
(x,y,z) = ("thing 1", "thing 2", "thing 3")
print(x)
print(y)
print(z)

# for lists:
[thing1, thing2, thing3] = [1,2,3]
print(thing1)
print(thing2)
print(thing3)

# LIST COMPREHENSIONS:
# Is a compact way to write an expression that expands to a whole list

# to write square values:
nums = [1,2,3,4]
squares = [n * n for n in nums]
print(squares)

# the syntax is [expr for var in list]
# Another example, setting a string to upper case and appending  "!!!" to the end
strings = ["Some", "Test", "Values"]
wow = [s.upper() + "!!!" for s in strings]
print(wow) # many

# you can add an if statement to the right of the for to narrow down the results
nums = [12,321,12,3321,123,21]
biggerNums = [n for n in nums if n > 300]
print(biggerNums)

# having an expr and a check
someFruit = ["Apple", "Pear", "Banana", "Peach", "Mango", "Orange", "Watermelon", "Lemon", "Cherry"]
# fruit in upper, and if they have a
fruitUpperA = [s.upper() for s in someFruit if 'A' in s.upper()] # the last upper just in case the list contains an upper case A
print(fruitUpperA)
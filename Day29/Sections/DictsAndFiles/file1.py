# dicts and files 

# to define a dict, you use curly braces
aDict = {}

# to set a value, use the key syntax:
aDict["Key1"] = "Value"
aDict["key3"] = "Another value"
aDict["key4"] = "Another value"
aDict["key5"] = "Another value"
# to access a value: 
print(aDict["Key1"])

# you can use the key syntax to check if a value is in the dict, but if it doesn't exist, throws an error
# use 'in' instead to check for exists

if "Key1" in aDict:
    print(aDict["Key1"])

# if you want to return a value from a dict without throwing an error:
print(aDict.get("Key1"))
print(aDict.get("Key2")) # returns None, takes a second param - where you can specify the return message/type/value

# a for loop over a dict, by default, goes over the keys
# note, the keys are returned in a random order
for key in aDict:
    print(key) 
    print(aDict[key])

# This means, this is exactly the same:
for key in aDict.keys():
    print(key)

# You can return a list of the keys, and the values:
print(aDict.keys())
print(aDict.values())

# you can loop over a dict, where the keys are sorted:
for key in sorted(aDict.keys()):
    print(key, aDict[key])

# you can return the '.items' of a dict, which is a tuple with the key value pair
for item in aDict.items():
    print(item)


# And bec you can use a tuple to assign multiple values, you can use the items method to loop over both the key and the value at the same time
for x,y in aDict.items():
    print(f"{x}>{y}") # you can now work with the dict key and value 

# Note that the key in a dict has to be unique. Make sure to always check for the key before adding one. dicts are good for lookups

# Dict formatting:
# The '%' operator is useful for formatting a dict, as you can use it to sub the value of a dict in a string
s = "The value of aDict, at Key1 is : %(Key1)s" % aDict
print(s)  # note, that d is for ints, and s is for strings - the suffix

# Del kw
# you can delete things, such as variables, it can be used in slices to delete a range, it can delete an element from a list; dict;
var = "thin"
del var # var is no longer there

aList = [1,2,3,4,5,6]
del aList[0] # deletes the first element
del aList[-2:] # deletes the last two elements
print(aList)

anotherDict = {1:42, 2:"fourty-two", 3: "101010"}
del anotherDict[1]
print(anotherDict)


# Working with files:
# You can use the open() method to open a file for reading/writing/creating/appending etc

# you can write to a file with w (if the file doesn't exist it is created) 
f = open("ANewFile.txt", "w") # this overwrites the text in a file though
f.write("This is a line\n")
f.write("This is another line\n")
# Note, you can write lines with a list as well (Like readlines returns a list (that you can use to write to a file:))
data = ["This is a line\n", "This is another line\n", "Would you look at that, another line\n"]
f.writelines(data) # would need the new line char for each though ?
f.close();

# You can open a file for reading with r
f = open("ANewFile.txt", "r")
for line in f:
    print(line)
f.close()

# Note, a better syntax for doing this (that disposes of itself) it to use the with clause

with open("ANewFile.txt", "r") as f:
    for line in f:
        print(line)
        # no need to close

# The rU option is the universal option where it is smart about the line endings and converts them to \n
with open("ANewFile.txt", 'rU') as f: # this mode is deprecated in python 3 though
    for line in f:
        print(line)    
# The above method of reading a file takes each line individually - which is nice when reading a large file. To read all the lines in a file though (care memory here)
# You would use file.readlines()

with open("ANewFile.txt", "r") as f:
    s = f.readlines()
    print(s) # returns a list of the lines (nice for a collection that you might want to work with)

# the codecs module provides support for reading unicode files:
# import codecs

# with open("ANewFile.txt", "rU", 'utf-8') as f:
#     print(f.readlines())
# I can't get this to work ? Python 3 problems, or am I just not seeing the issue clearly
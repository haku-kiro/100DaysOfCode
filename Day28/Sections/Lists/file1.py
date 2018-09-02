# working with python lists

colors = ['red', 'green', 'blue']
print(colors[0]) # red
print(colors[1]) # green
print(colors[2]) # blue
print(len(colors)) # 3

# assigning a list to a var doesn't create a copy, it just creates a ref to the original list
b = colors
# test
colors.append("purple")
print(len(b)) # now has the length of 4 (Lists are ref type)

# You can append two lists with '+'
print (b + colors) # which you can store to create a new list

# The 'for' kw in python is useful for iteration, rem when iterating over a collection to not change the index by adding or removing from the collection
for x in b:
    print(x) # prints all the colors in the list

sum = 0
for x in [1,2,3,4,5]:
    sum += x # sums the list
print(sum)

sum = 0
for x in range(1,6): 
    sum += x # sums the range
print(sum)

# You can use the 'in' kw to check for existance:
if 'green' in colors:
    print("Green is there")

# while loops
i = 0
while i < 10:
    print(f"The value of i: {i}")
    i += 1

# list methods:

# append: Adds an element onto the end of a list
colors.append("yellow")

# insert: inserts an element into a list, shifting other elments to the right
colors.insert(1, "pink")

# extend: same as adding two lists together
colors.extend(b) # what happens here though, it's ref type? Just writes the list onto the end of itself - makes sense
print(colors)

# index: finds the index of the param, throws ValueError if the element is not found (use 'in' to not throw an error)
redIndex = colors.index("red")
print(redIndex)

# remove: finds the first instance of the param and removes that element, throws a ValueError if the element is not present
colors.remove("red")

# sort: sorts the list in place (ie, doesn't return a list)
colors.sort()
print(colors) # also not that there is only one red in the list now

# reverse: reverses the list in place
colors.reverse()
print(colors)

# pop: removes and returns the element at the passed param/index
colors.pop(2)

# note that some methods don't return a list, they change them in place, for example
print(colors.sort()) # returns none


# building up a list:
aList = []
aList.append("Element one")
aList.append("Element two")
aList.append("Element three");

# splicing a string

print(aList[0:1]) # from 0 index to the first pos
print(aList[1:2])
print(aList[2:3])

# you can replace a range with one element (or a single element) with splicing

aList[0:1] = "Elem 1"
print(aList) # adds the char values to the list

print(aList[0:1])
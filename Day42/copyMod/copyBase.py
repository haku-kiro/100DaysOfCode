# to show the diff between shallow and deep copy of an object

# there is a python module called copy that can create both a shallow and deep copy, we'll use a list
# as our object

import copy

aList = [1,2,3,4,5,6,7,8,9,42]
print(aList)

shallow = copy.copy(aList) # shallow copy 
deep = copy.deepcopy(aList) # a deep copy

print(shallow)
print(deep)

aList.append("Something")
shallow.append("Another thing") # as far as I understand, a shallow copy is a like a deep copy, but not ? :D
print(aList)
print(shallow)
print(deep) # a deep copy is a completely new instance of the object ?
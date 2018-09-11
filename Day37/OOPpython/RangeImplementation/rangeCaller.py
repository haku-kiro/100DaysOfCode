# logic is the same as range - it is in the RangeClass py file

from RangeClass import Range

for x in Range(10):
    print(x)

for y in Range(10,101, 2): # exactly the same as the standard range class
    print(y)
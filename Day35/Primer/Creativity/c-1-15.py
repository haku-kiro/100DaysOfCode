"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

# Why reinvent the wheel
def isOnlyDistinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

testDataFalse = [1,2,3,123,1,2]
testDataTrue = [1,2,3,4,5,6]
if not isOnlyDistinct(testDataFalse):
    print("Test 1 worked")

if isOnlyDistinct(testDataTrue):
    print("Test 2 worked")

# if you aren't allowed to use the set datastructure
def isOnlyDistinctHardVersion(data):
    dataCheck = {} 
    for num in data:
        if num in dataCheck:
            dataCheck[num] += 1
        else:
            dataCheck[num] = 1
    for x in dataCheck:
        if dataCheck[x] > 1:
            return False
        else:
            return True

if not isOnlyDistinctHardVersion(testDataFalse):
    print("Test 3 worked")
if isOnlyDistinctHardVersion(testDataTrue):
    print("Test 4 worked")
def WordCount(path):
    dictOfWordCounts = {}
    with open(path, "r") as f:
        for line in f:
            for word in line.split(): # splitting all whitespace (I think newlines count as whitespace - probably)
                if word.lower() in dictOfWordCounts:
                    dictOfWordCounts[word.lower()] += 1
                else:
                    dictOfWordCounts[word.lower()] = 1
    return dictOfWordCounts


# data = WordCount(r"C:\Users\mdjco\Desktop\100DaysOfCode\Day29\Sections\DictsAndFiles\Challanges\small.txt")
# for key in data.keys():
#     print(f"{key} > {data[key]}")
# print(sorted(data))    



# The most awful sorting algorithm, in the world
# 
# The point of this is just for shits and giggles, really
# Need a method that takes a list and puts the elements in a random order:

import random

def RandomiseList(theList):
    newList = []
    for elem in range(len(theList)):
        choice = random.choice(theList) # takes a random element
        newList.append(choice)
        # Handles the duplicate values thing quite elegantly
        theList.remove(choice)
    return newList

def SortedEh(listToSort):
    tries = 0
    notSorted = True
    # buble the list
    while (notSorted): 
        if (all(listToSort[i] <= listToSort[i+1] for i in range(len(listToSort)-1))):
            print(listToSort, " Took this many tries: " ,str(tries))
            notSorted = False
        else:
            listToSort = RandomiseList(listToSort)
            tries += 1
            
listTest = [1,2,3,1,21,123,3,7,42] # about the limit for a reasonable time
SortedEh(listTest)

# Testing random
#print(RandomiseList([1,2,3,4,5]))

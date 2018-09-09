"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

def CheckOddProdct(data):
    # Data has to be a list of ints
    for x in data:
        for y in data:
            if x == y:
                continue
            else:
                sum = data[x] + data[y]
                if  sum % 2 != 0:
                        print(f"The value: {data[x]}, and {data[y]} make the odd number: {sum}")
    print("End of method")

someData = [1,2,3,4,5,6,7,8,9]
CheckOddProdct(someData) # Kind of works, but it shows the same thing so many times ... - Also, need to debug this as there is an out of range error
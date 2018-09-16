"""
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""

class Flower:
    """
    This class will contain metadata on a flower, and allow changes to each instance var
    """

    def __init__(self, name, petalcount, price):
        """
        Ctor to create an instance of the flower class

        petalcount   The number of petals the flower has, int.
        price        The cost of the flower, float
        name         The name of the flower
        """
        # should probably do type checking here as well
        self._name = name
        self._petalcount = petalcount
        self._price = price

    def getName(self):
        """
        Return the name of the flower
        """
        return self._name

    def setName(self, newName):
        """
        Sets a new name of the flower
        """
        if type(newName) is str:
            self._name = newName
        else:
            raise ValueError("Please make sure to pass the correct type")

    def getPetalCount(self):
        """
        Returns the amount of petals
        """
        return self._petalcount

    def setPetalCount(self, newCount):
        """
        Sets the petal count
        """
        if type(newCount) is int:
            self._petalcount = newCount
        else:
            raise ValueError("Please make sure to pass the correct type")

    def getPrice(self):
        """
        Returns the price
        """
        return self._price

    def setPrice(self, newPrice):
        """
        Sets the new price of the flower
        """
        if type(newPrice) is float:
            self._price = newPrice
        else:
            raise ValueError("Please make sure to pass the correct type")

    def __str__(self):
        """
        Overload for str to return the information of the flower
        """
        return f"{self._name} has {self._petalcount} petals and the price of {self._price}"

# not going to create a caller class, just going to run here

def tests():
    """
    Method to test the flower class
    """
    rose = Flower("Rose", 42, 12.42)
    print(rose) # calls the str method, just like c#, nice


    rose.setName("ROSE")
    try:
        rose.setName(42) # can't set the wrong type
    except Exception as e: # just to get the message that is created in the class (the inner exception)
        print("An error occured")
        print(e)

    print(rose.getName())
    print(rose.getPetalCount())
    print(rose.getPrice())

# being extra
if __name__ == '__main__':
    tests()
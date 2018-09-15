# the abc namespace/module is in the base python modules and contains abstract classes?
from abc import ABCMeta, abstractmethod # the second one is a decorator ? These are like atrribs ?

class Sequence(metaclass=ABCMeta):
    """
    Our own version of collections.Sequence abstract base class
    """

    @abstractmethod
    def __len__(self):
        """
        Returns the len of the sequence
        """
        # contains no logic - this is more like an interface ?

    @abstractmethod
    def __getitem__(self, j):
        """
        Return the element at index j of the sequence
        """

    def __contains__(self, val):
        """
        Return True if val found in the sequence, False otherwise.
        """
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """
        Return leftmost index at which val is found (or raise ValueError)
        """
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("Value not in sequence.")

    def count(self, val):
        """
        Return the number of elements equal to given value
        """
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
    


# okay, so the above defines a meta class (can have implementation). Acts like an interface
# also, if you try to create an instance of a MetaClass an error is raised
# the decorator is the reason that there is no implementation for the method
# you can have nested classes

# take note of the __slots__ lookup that can be used to sreamline datastorage in a class? 
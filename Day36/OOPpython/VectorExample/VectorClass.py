## This class will serve as an example for overloading methods 

class Vector:
    """
    Represents a vector in a multidimensional space
    """

    def __init__(self, d):
        """
        create d-dimensional vector of zeros
        """
        self._coords = [0] * d

    # overload for length
    def __len__(self):
        """
        Returns the dimensions of the vector
        """
        return len(self._coords)
    
    def __getitem__(self, j):
        """
        Returns the jth coord of the vector
        """
        return self._coords[j]

    def __setitem__(self, j, val):
        """
        Sets the jth element of coords to the passed val
        """
        self._coords[j] = val

    def __add__(self, other):
        """
        Returns the sum of two vectors
        """
        if len(self) != len(other): # this relies on the __len__ method in this class (the `other` will be of type vector ?)
            raise ValueError("The dimensions have to be the same for addition")
        result = Vector(len(self)) # create an empty vector, just zeros - so that you can store the result of both vectors
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """
        Returns true if the vector has the same coords as another
        """
        return self._coords == other._coords # assuming the type is the same?

    def __ne__(self, other):
        """
        Returns true if vectors are not equal
        """
        return not self == other
    
    def __str__(self):
        """
        Produces the string representation of the vector
        """
        return f'<{str(self._coords)[1:-1]}>' # adapt list representation
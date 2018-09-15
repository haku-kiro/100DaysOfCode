# importing to use in new class
from progressionClass import Progression

class ArithmeticProgression(Progression): # inherit from
    """
    Iterator producing an arithmetic progression
    """
    def __init__(self, increment=1, start=0):
        """
        Create a new arithmetic progression

        increment  the fixed constant to add to each term (Default 1)
        start      the first term of the progression (Default 0)
        """

        super().__init__(start) # init the base class
        self._increment = increment

    def _advance(self): # override the inherited version
        """
        Update current value by adding the fixed increment
        """
        self._current += self._increment

# adding the classes here multiple classes here bec - well, easier

# Geometric progression class
class GeometricProgression(Progression):
    """
    Iterator producing a geometric progression
    """
    def __init__(self, base=2, start=1):
        """
        Create a new geometric progression

        base  the fixed constant multiplied to each term(default 2)
        start the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self): # override inherited version
        """
        Update the current value by multiplying it by the base value
        """
        self._current *= self._base


# Fibonacci Progression class
class FibonacciProgression(Progression):
    """
    Iterator producing a generalized Fibonacci progression
    """

    def __init__(self, first=0, second=1):
        """
        Create a new fibonacci progression

        second   the second term of the progression (default 1)
        first    the first term of the progression  (default 0)
        """
        super().__init__(first)  # start the progression at first
        self._prev = second - first # fictious value proceding the first

    def _advance(self):
        """
        Update current value by taking sum of previous two
        """
        self._prev, self._current = self._current, self._prev + self._current

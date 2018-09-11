# The point of this implementation is to show lazy evaluation, a technique to avoid generating a whole list (like range in py2)

class Range:
    """
    A class that mimics the built-in range class (py3)
    """

    def __init__(self, start, stop=None, step=1):
        """
        Init the range instance, note the optional params 
        """
        if step == 0:
            raise ValueError("Step cannot be 0") # to avoid infinite loop, so to speak
        
        if stop is None:
            start, stop = 0, start # Sepcial case of Range(n)
                                   # Should be treated as if range (0, n)
        
        self._length = max(0,(stop -start + step -1) // step) # calc the length taking the step into account

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """
        Returns the length of the 'list'
        """
        return self._length

    def __getitem__(self, k):
        """
        Returns entry at index k (using standard interpretation if negative - this was one of the questions of chapter 1)
        """
        if k < 0:
            k += len(self) # attempt to convert negative index (also, we're using the len - which we defined above this)
        
        if not 0 <= k < self._length:                    # take time to understand the chaining here
            raise IndexError("Index out of range")
        
        return self._start + k * self._step
## With python, to create a class specific as an iterator - you have to write the overload for the method __next__()
# Fortunately, you can use the generator syntax and yield the result of the collection, also
# Python provides an automatic iterator implementation when a class defines both the __len__ and the __getitem__ method


class SequenceIterator:
    """
    An iterator for any of pythons sequence types
    """

    def __init__(self, sequence):
        """
        Create an iterator for the given sequence
        """
        self._sequence = sequence   # keep a reference to the underlying data
        self._k = -1                # will increment to 0 on first call to next

    def __next__(self):
        """
        Return the next element, or raise the StopInteration error
        """
        self._k += 1 # advance to the next index (first index is 0)
        if self._k < len(self._sequence):
            return(self._sequence[self._k]) # returns the data element
        else:
            raise StopIteration() # Meaning there are no elements (Does this happen with every iterator ? Hmm)

    def __iter__(self):
        """
        By convention, an iterator must return itself as an iterator
        """
        return self


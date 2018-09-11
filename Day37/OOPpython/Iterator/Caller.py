# logic is in the IteratorClass py file

from IteratorClass import SequenceIterator

seq = SequenceIterator([1,2,3,4])
for x in seq:
    print(x)

print(seq)

# the above acts as a traditional sequence (Even the current use is very narrow)
# but our seq can be any class, that we create that implements the len and the getitem overloads
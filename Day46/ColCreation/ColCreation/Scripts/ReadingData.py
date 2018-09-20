class colRow:
    """
    Defines the column being addeds meta data
    """ 
    def __init__(self, name, type, size, caption, nullable):
        """
        Create an instance of the colRow
        """
        self._name = name
        self._type = type
        self._size = size
        self._caption = caption
        self._nullable = nullable

# return me when done
colsToBeCreated = []

# set path in c#
with open(path) as f:
	# TODO: Do error handling and pass the object correctly
    for line in f:
        data = line.split(',')
        item = colRow(data[0], data[1], data[2], data[3], data[4])
        colsToBeCreated.append(item)
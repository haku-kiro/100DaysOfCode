# this py script is for reading csv files and creating an object to work with

import Config

class colRow:
    """
    Defines the column being addeds meta data
    """ 
    def __init__(self, name, type, size, caption, nullable, entity):
        """
        Create an instance of the colRow
        """
        self._name = name
        self._type = type
        self._size = size
        self._caption = caption
        self._nullable = nullable
        self._entity = entity

# Create an instance of me
class ColLoader:
    """
    Returns the column data
    """
    def __init__(self):
        colsToBeCreated = []

        # note that the path is taken from the config file (This is filth - use a df...)
        with open(Config.CSV_PATH, 'r') as f:
            header = f.readline() # pulling the header out ... again, use pandas ...
            for line in f:
                data = line.split(',')
                item = colRow(data[0], data[1], data[2], data[3], data[4], data[5])
                colsToBeCreated.append(item)

        self._cols = colsToBeCreated

# unit tests
if __name__ == '__main__':
    loader = ColLoader()
    print(loader._cols)
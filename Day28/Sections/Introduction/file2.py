# user defined functions
import file1
# if we don't like the above, and would like to import the method for use without their module names we would use the following:
from file1 import main # now we can use main as is

# Some standard lib modules to read about include:
import sys
import os 
import re # regular expressions

def Repeat(s, exclain):
    """
    Returns the string s three times,
    If exclain is true, adds exclamation marks
    """
    if (exclain):
        print((s + " ")*3 + '!')
    else:
        print((s + " ")*3)

## Adding the file1 method to the program is as easy as importing the module
file1.main()

if __name__ == "__main__":
    Repeat("test", False)
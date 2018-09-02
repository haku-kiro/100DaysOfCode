# A simple hello python program

import sys

# Add our code into a main function

def main():
    print(f"Hello there, {sys.argv[1]}") # arg 0 would be the script name itself and can be ignored

# standard boilerplate to call the main method:


# apparently this is like this so that if the module is imported, it is not run 
if __name__ == '__main__': # what is the point of this though? 
    main() 
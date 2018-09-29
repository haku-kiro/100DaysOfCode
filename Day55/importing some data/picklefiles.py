## This example imports a pickle file (Not sure how to create one as of yet)
## This is deserializing/serializing in python

# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d (the type is maintained)
print(type(d))
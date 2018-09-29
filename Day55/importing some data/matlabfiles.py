# This will show how to import matlab files
# is short for 'matrix laboratory'
# saved in .mat files 
# to import matlab files you can use the scipy.io module
# the .mat files are loaded as dicts with the key being the var name in the workspace and the value being the object that is assigned to that variable

# pip install scipy ? 
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat') # showing an error, but works, just don't have the file

# Print the datatype type of mat
print(type(mat))

for key in mat.keys():
    print(key)

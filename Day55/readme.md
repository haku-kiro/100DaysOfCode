# Day 55

## Objectives

Working on datacamp.com

## Resources

- <http://datacamp.com>

### Setup

- webz

### Suggested plan for tomorrow

- Should really go through this content at some point...
- Writing xml files
  - <https://csharp.net-tutorials.com/xml/writing-xml-with-the-xmlwriter-class/>
- Do some more stuff with wcf
  - composite types to service operations
- Cover a few design patterns: Like the proxy pattern (This might not relate, <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-create-a-wcf-client> but check it out (The proxy section that is (Svcutil.exe section)))
- Read up on how to use the Svcutil.exe tool (To create the source and config file)
- wcf service configuration editor (Look at how this tool functions as well. Under tools vs)
- Cover the 'See Also' section under: <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-use-a-wcf-client>
- Do some work with async and await, or some threading - parallel tasks etc
- Cover how IL works, and the implications of compiler theory
- Need to look into how to make a method `Awaitable`
- Still need to finish the edx course on computing with python.

### Random Notes

- Don't have the mnist dataset, but this is pretty cool

```Python 

# Import package
import numpy as np

# Assign filename to variable: file
file = 'digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

```

- A numpy file import example, where
  - The delimeter is a tab
  - Has a header row
  - You only want col 1 and 3

```Python

data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

```

- If you want to import from a file where the columns have different dtypes

```Python

# the genfromtxt method with the dtype=none will auto detect the dtype
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)

```

- The shorthand for getting rows/columns from a numpy narray (Not working on the titanic.csv file, might be limited)
- Working with the titanic csv if you don't use the names=True param

```Python

# rows:
data[0,:] # the first row


# columns
data[:,0] # the first column
data[:,5] # the fourth column, etc

# Side note, if you don't want to use the genfromtxt with the dtype=None param, this would be the same:
np.recfromcsv(file) # the delimiter is set to ',' by default and names=True as well
print(d[:3]) # would print the first three rows

```

```Python

df.head()

df_array = df.values # returns the df as a np array (not a method)

```

- HDF5 files ?
- Pickling files is serializing/deserializing files

#### Look up what codds 12 rules/commandments are
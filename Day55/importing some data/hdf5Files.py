# importing hdf5 files
# Hierarchical data format version 5
# Used for storing large quantities of numerical data
# hdf5 can scale to exabytes

# import the h5py module (pip install if you don't have it)
import h5py 


hdf5_data = h5py.File('file.hdf5')


# Import packages
import numpy as np
import h5py

# Assign filename: file (I don't have this file)
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file (hdf5 files have a key/value type of layout)
for key in data.keys():
    print(key)


# An example of vizing the data:
# Note, I don't have this file, but it is the hdf5 file used by ligo


# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = group['Strain'].value # make sure to use the attrib, value
print(strain)

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
# plt.plot(time, strain[:num_samples])
# plt.xlabel('GPS Time (s)')
# plt.ylabel('strain')
# plt.show()

from datetime import date
from pandas_datareader.data import DataReader
import matplotlib.pyplot as plt

# Set the start date
start = date(1950, 1, 1)

# Define the series codes
series = ['UNRATE', 'CIVPART']

# Import the data
econ_data = DataReader(series, 'fred', start)

# Assign new column labels
econ_data.columns = ['Unemployment Rate','Participation Rate']

# Plot econ_data
econ_data.plot(title='Labor Market') # subplots renders a plot for each dframe

# Show the plot
plt.show()
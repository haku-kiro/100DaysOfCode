from datetime import date
from pandas_datareader.data import DataReader
import matplotlib.pyplot as plt

# Set the start date
start = date(2008, 1, 1)

# Define the series codes
series = ['BAMLHYH0A0HYM2TRIV', 'SP500']

# Import the data
econ_data = DataReader(series, 'fred', start)

# Assign new column labels
econ_data.columns = ['Bond','Stock']

# Plot econ_data
econ_data.plot(title='Performance Comparison', subplots=True) # subplots renders a plot for each dframe

# Show the plot
plt.show()
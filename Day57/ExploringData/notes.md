# Notes

- You've seen how you can use describe to show stats on numerical data
- You can use value_counts to see how many distinct values there are for a column. If you can add dropna=False, you can see if there is any null data

```Python

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

```

- To spot outliers more easily, it is often a good idea to viz your data.
- You can use bar plots and histograms to plot data (When looking for outliers).
  - bar plots for discrete data counts
  - Histograms for continuous data counts


- To create a viz using your dframe (quickly at least). Do the following

```Python

import matplotlib.pyplot as plt

# populate a dataframe
#...
#Create a plot
df.col.plot('hist')

# Add labels etc
plt.show()

```

- If you encounter any issues (spot potential outliers) you can splice your data using bracket notation

```Python

# using the col that has a potential outlier, you can check to see if the data point is vastly off or if it is accurate

df[df.col > 1000000]
# returns the rows that match

```

- You can use box plots to viz basic summary stats (Covered in the stats course)
- To create a box plot:

```Python
# make sure to have matplot

df.boxplot(column='colname', by='another col') # this other col would be the 'group by'
plt.show()

```

- You can use scatter plots to viz the relationship between 2 numeric values

## Vizing single vars with histographs (using df plot method)

```Python

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

```

## Vizing multiple vars with boxplots

```Python

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()


```

## Vizing multiple vars with scatter plots

```Python

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

```
# Try giving, 'Tidy Data' paper by Hadley Wickham, PhD 

## Principles to follow

- 1 - Columns represent seperate variables
- 2 - Rows represent individual observations
- 3 - Observational units form tables

- Some data is better for reporting and some is better for analysis.

- You would use pandas method melt to convert data that does not follow the above principles to follow a better structure for both cleaning and analyzing the data

```Python

# This is following the dframe example from datacamp
pd.melt(frame=df, id_vars='name', value_vars=['treatment a', 'treatment b'])

# The value_vars parameter is the column that will 'melt' and basically merge to create a single column
# If you don't specify the column to melt, it would use all the columns not specified in the id_vars param


# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
# If you specify don't specify a value_vars param, those cols will be melted
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day']) # note, this just proves that it isn't always the best idea to use melt on your data

# Print the head of airquality_melt
print(airquality_melt.head())


# When you melt cols you can rename the value and the vars col:

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())


```

## Pivoting

- The opposite of melting data is to pivot it
  - Can be used to unmelt a dframe
- pivoting turns cols into rows


(To be continued)
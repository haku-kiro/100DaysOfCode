# Notes on cleaning data

Cleaning data that has certain inaccuracies

## Loading and viewing the information of a dataframe

```Python

# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv') # Don't have this file

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())


# Print the info of the dframe
print(df.info()) # returns type info on the fields, etc


# You can do a basic analysis of the columns that have a number like dtype using describe:
print(df.describe())

```
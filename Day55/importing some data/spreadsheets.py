## Listing the names of the sheets in the spreadsheet file

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
# I don't have this file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)


## using the spreadsheet sheets as  dframes

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse('2002')

# Print the head of the DataFrame df2
print(df2.head())


# when customizing your import, make sure that you specify the params as lists!!
# Note, again, I don't have this file (Can download it I guess)

# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[1], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(1, parse_cols=[1], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

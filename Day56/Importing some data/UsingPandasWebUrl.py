### If you want to read the file from the web and not save it locally, you could use the url as the first arg in pd.read_csv

# importing a csv file

# Import packages
import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1]) # use this over: df.iloc[:,0]
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


# importing an excel spreadsheet (without saving it)

# Import package
import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xl
xl = pd.read_excel(url, sheetname=None) # You pass none to sheetname to import all the sheets

# Print the sheetnames to the shell
print(xl.keys()) # imported as a dict, so you can use dict methods...

# Print the head of the first sheet (using its name, NOT its index)
print(xl['1900'].head()) # each dict key has a df in it (the spreadsheet)

## sas files are for statisctical analysis systems
## stata files: 'Statistics' + 'data'


#SAS: business analytics and biostatistics
#Stata: academic social sciences research

#( To read sas files, files with the extension: .sas7bdat)
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas (This would be the important part)
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# # Plot histogram of DataFrame features (pandas and pyplot already imported)
# pd.DataFrame.hist(df_sas[['P']])
# plt.ylabel('count')
# plt.show()


# To read stata files (files with the extension: .dta)
# Import pandas 
import pandas as pd

# store the file in a dframe
df = pd.read_stata('file.dta')
print(df.head())
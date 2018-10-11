import pandas as pd
import numpy as np
import datetime


def DateFix(dateVal):
    return datetime.datetime.strptime(str(dateVal).replace("00:00:00", "").replace(" ", "") , "%Y-%m-%d").strftime("%d/%m/%Y")

path = r"C:\Users\mdjco\Desktop\Work\barak\data\ConsolidatedTransactions.xlsx"
df_all = pd.read_excel(path, parse_dates=True, index_col="ID")

# df_all.set_index("Transaction Date")
print(df_all.info())
print(df_all.head())

# Col to change
col_name = "Transaction Type Code"

# For credit journals
maskCredit = np.logical_and(df_all.Amount < 0,  df_all["Transaction Description"] == "Journal")

# For debit journals
maskDebit = np.logical_and(df_all.Amount > 0,  df_all["Transaction Description"] == "Journal")

df_all.loc[maskCredit, col_name] = 3023
df_all.loc[maskDebit, col_name] = 3024

# Sanity check
# print(df_all[maskCredit][col_name].head())

# Data that is needed by the import
import_data = df_all.loc[:, ["Transaction Date", "Transaction Description", "Transaction Type Code", "Account Number", "Amount"]]
print(import_data.head())
import_data = import_data.assign(Comment = lambda x: "Import Comment") # Change to what the comment might needs be
import_data = import_data.assign(Reference = lambda x: "Import")

# Need to make sure the value is pos
import_data["Amount"] = import_data["Amount"].apply(abs)


# Fix the datetime
import_data["Transaction Date"] = import_data["Transaction Date"].apply(DateFix)

print(import_data.head())
print(import_data.info())

#Stripping accounts that aren't in the system:
dataIn = []
with open(r'c:\Users\mdjco\Desktop\Work\barak\data\accountsToBeImported.txt', 'r') as f:
    for line in f.readlines():
        dataIn.append(line[:-1]) # stripping \n


importThese = import_data[import_data.iloc[:,3].isin(dataIn)]

import_data.to_csv("./WholeFile.csv", index=False)
importThese.to_csv("./ImportData.csv", index=False)
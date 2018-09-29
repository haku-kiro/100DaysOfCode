# point is just draw a histograph with the ages of congress members (Not even sure how to interpret the data right now)
import matplotlib.pyplot as plt
import pandas as pd

file_path = r'C:\Users\mdjco\Documents\datasets\congress-terms.csv'

# fortunately the data has been cleaned for us already
df_congress = pd.read_csv(file_path)
age_dset = df_congress['age']

plt.hist(age_dset)
plt.xlabel('Age (in years)')
plt.ylabel('Count')

plt.show()

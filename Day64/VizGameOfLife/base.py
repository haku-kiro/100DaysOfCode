import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot') # Nice

# Should refactor this into a class

listOfData = []

def GetFiles(path):
    """ Loads a csv file to a df and adds to list """
    df = pd.read_csv(path, header=None) # there is no header in the file
    lifeForms = df.iloc[:,1] # We want the Second col (Contains the life forms)
    lifeForms.columns = ['Count']
    listOfData.append(lifeForms)

def Normalize(data):
    """ 
    Bec not all dsets stabilize at the same point, going to find
    The longest set, make each set that length (With the last value)
    """
    newSeries = []

    maxLen = data[0].count()
    for x in data:
        if x.count() > maxLen:
            maxLen = x.count()
    # Now that you have the max len, make sure each is that len with their last values as the cont
    for x in data:
        # x is a pandas series
        # Get the last value in x
        lastVal = x.iloc[-1]

        # Get the remainding amount
        rem = maxLen - x.count()
        remList = pd.Series([lastVal] * rem) # Have to create a series
        x.append(remList) 
        # annnnd normalized, what is an easier way to do this ?
        newSeries.append(x.append(remList, ignore_index=True)) # Yikes - Filthy
    return newSeries

def PlotAllData(data):
    """ Plots each df in data """
    for x in data:
        x.plot(linewidth=1)

# I have 10 csv files with the conways game of life results
for i in range(1,11):
    filePath = f"C:/Users/mdjco/Documents/datasets/gameOfLife{i}.csv"
    GetFiles(filePath)
data = Normalize(listOfData)
PlotAllData(data)

# Graphs stuffs

plt.title("Conways Game of Life")
plt.xlabel("Iterations")
plt.ylabel("Life forms")

plt.savefig('./test.png', bbox_inches='tight', dpi=650) 
plt.show()
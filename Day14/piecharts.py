import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

# Things you do
sleeping= [7,8,6,7,7,10,9]
eating =  [2,3,2,3,2,3,3]
working = [9,9,9,9,9,0,0]
playing=  [6,4,7,5,6,11,12] # lol should add up to 24 (realistically)

slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working','playing']

# explode is used to pull out something by index
plt.pie(slices,
  labels=activities,
  colors=['r', 'b', 'g', 'c'],
  startangle=90,
  explode=(0,0.1,0,0),
  autopct='%1.1f%%') # last bit is to add percentage to the chart 


plt.title("This would be 'percentages'\nCheck it out!")
# plt.legend()
plt.show()
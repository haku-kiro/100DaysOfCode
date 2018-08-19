import matplotlib.pyplot as plt

# stack plot to show a holistic number, sections that make up that number

days = [1,2,3,4,5,6,7]

# Things you do
sleeping= [7,8,6,7,7,10,9]
eating =  [2,3,2,3,2,3,3]
working = [9,9,9,9,9,0,0]
playing=  [6,4,7,5,6,11,12] # lol should add up to 24 (realistically)

# note that the first var is the x, every other is the y
plt.stackplot(days, sleeping, eating, working, playing, colors=["b", 'r', 'c', 'g'], labels=["sleeping", "eating", "working", "playing"])


# plotting empty plots for when you can't get a legend

plt.title("This is a boring graph,\nCheck it out !")
plt.legend()
plt.show()

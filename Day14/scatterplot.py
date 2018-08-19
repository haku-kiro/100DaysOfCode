import matplotlib.pyplot as plt

# scatter to show correlation, or even distribution between two variables

x = [1,2,3,4,5,6,7,8]
y = [2,4,5,1,6,7,1,7]

plt.scatter(x,y, label="thing", color='b', marker='*')

plt.legend()
plt.show()
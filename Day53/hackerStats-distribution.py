# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(69)

# Simulate random walk 500 times
all_walks = []
iterations = 2000000
for i in range(iterations) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]


# calc change to succeed:

chance_to_suceed = len(ends[ends >=60]) / iterations * 100
print(f"You are {chance_to_suceed}% likely to succeed")

# Plot histogram of ends, display plot
plt.plot(ends)
plt.plot(500, 60)
plt.show()

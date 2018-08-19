import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x1 = [1,3,5,6,7]
y1 = [7,3,5,6,7]


population_ages = [22, 55, 63, 45, 99, 12, 120, 11, 110, 43, 54, 65, 23, 54, 12, 87, 62, 101, 42, 42]
ids = [x for x in range(len(population_ages))] # just to create a list of ints that correspond to our population ages, not needed for histograms

# bar graph for the population
# plt.bar(ids, population_ages, label="Ages of people", color='c')


# bar graph
# plt.bar(x,y, label="bars 1", color="blue")
# plt.bar(x1,y1, label="bars 2", color='red')


# histograph
# to show the distribution

bins = [0, 10, 20 , 30, 40 , 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, label='ages')

plt.xlabel('x label')
plt.ylabel('y label')




plt.legend()
plt.show()
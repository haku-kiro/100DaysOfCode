"""
Simulation:

Calculating the probability that given a dice roll using two dice, where the total ends up being equal to 6,
what is the proabability that one of the dice has a two on them
"""

from random import randint
import matplotlib.pyplot as plt

numbers = {}

def diceRoll():
    """
    Rolls a dice and returns the number
    """
    return randint(1,6)


def generateNumbers(times):
    """
    Rolls the double dice, checks that they equal six and returns the result 
    """
    two_occured = 0
    got_six = 0
    numbers = {}
    for i in range(times):
        roll_one = diceRoll()
        roll_two = diceRoll()
        total = roll_one + roll_two
        if total == 6: # Don't care about others (for now, could use it to check how often you'd roll six I guess ?)
            got_six = got_six + 1
            # Add the numbers to return dict
            if roll_one in numbers:
                numbers[roll_one] = numbers[roll_one] + 1
            else:
                numbers[roll_one] = 1 

            if roll_two in numbers:
                numbers[roll_two] = numbers[roll_two] + 1
            else:
                numbers[roll_two] = 1

            if roll_one == 2 or roll_two == 2:
                two_occured = two_occured + 1

    percent = (two_occured / got_six) * 100
    return (percent, numbers, got_six)


times = 1000000
percent, nums, six = generateNumbers(times)
print(nums)
print(f"The percentage: {percent}%") 
print(f"Ran {times} times, Of which {six} added up to six: {six/times * 100}%")

plt.style.use("ggplot")
plt.bar(nums.keys(), nums.values())
plt.title("Dice Rolls that Add up to 6")
plt.show()
"""
What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""

for num in range(50, 81, 10): # not inclusive of the last index (need to make it larger than the end goal, but less than the stop + step (to avoid carring over))
    print(num)
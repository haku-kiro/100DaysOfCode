"""
This file shall server as a setup/test file for the course
"""

import turtle 

# Create an instance of the turtle class
myTurtle = turtle.Turtle()

#Move your turtle around etc:
# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)

# written better:
x = 0
while (x < 4):
    myTurtle.forward(100)
    myTurtle.right(90)
    x += 1

input("Press enter to continue")

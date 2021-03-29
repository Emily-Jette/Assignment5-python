# setting up variables
import math

pi = math.pi
diameter = 0
radius = 0
area = 0
c = 0

# user inputs diameter and their answer is converted to an integer
print('Enter the diameter of a circle to find the area and circumference:')
diameter = input()
diameter = int(diameter)

# the math
radius = diameter / 2
area = round(pi * (radius * radius), 1)
c = round(2 * (pi * radius), 1)

# final answer is printed
print('The area is ' , area, 'and the circumference is',c)

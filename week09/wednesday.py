#Wednesday: Modules

# import the entire math module

import math

print(math.floor(2.5))
print(math.ceil(2.5))
print(math.pi)

from math import floor, ceil, pi

print(floor(3.5))
print(ceil(3.5))
print(pi)

from math import floor as f

print(f(3.3))

from test import length, width, print_info

print(length)
print(width)
print(print_info("alex", 41))

# Time Module: Import the time module and call the sleep function. Make the 
# cell sleep for 5 seconds, and then print “Time module imported”.

from time import sleep

sleep(2)
print("Time module imported!")

# Calculating Area: Create a module named “calculation.py” that has a single
# function within it. That function should take in two parameters and return the
# product of them. We can imagine that we’re trying to calculate the area of
# a rectangle and it needs to take in the length and width properties

from calculation import calc_area

print(calc_area(5,3))
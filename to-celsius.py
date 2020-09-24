#!/usr/bin/env python

# To make sure that we're not completely tied to the path of our python3 binary, 
# we need to we set up our shebang properly

# Python implementation here

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))
# Works from the inside out,
# the float requirs a number.
# By default, this variable will be a string, 
# so we'll need to cast it to be a float
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")
# The float is rounded off by 2
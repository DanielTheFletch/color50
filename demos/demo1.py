# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# demo1.py
# Demonstration of package functionality (1 of 4)

from color50 import Color, constants
import sys

# Prompt for user input
input_red = input("Enter an integer (0-255) for the color's RED value: ")
input_green = input("Enter an integer (0-255) for the color's GREEN value: ")
input_blue = input("Enter an integer (0-255) for the color's BLUE value: ")

# Validate input type
try:
    input_red = int(input_red)
    input_green = int(input_green)
    input_blue = int(input_blue)
except ValueError:
    sys.exit("Error: Invalid color selection")

# Validate input value
my_color = Color()
try:
    my_color.red = input_red
    my_color.green = input_green
    my_color.blue = input_blue
except ValueError:
    sys.exit("Error: Invalid color selection")

# Print message in user-specified color
print(my_color + "Hello, World!" + constants.RESET)

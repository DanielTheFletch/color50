# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# demo3.py
# Demonstration of package functionality (3 of 4)

from color50 import ColorStr, rgb
import random

# Randomly select foreground color
rand_red = random.randint(0, 255)
rand_green = random.randint(0, 255)
rand_blue = random.randint(0, 255)
fg_color = rgb(rand_red, rand_green, rand_blue)

# Randomly select background color
rand_red = random.randint(0, 255)
rand_green = random.randint(0, 255)
rand_blue = random.randint(0, 255)
bg_color = rgb(rand_red, rand_green, rand_blue)

# Create and print ColorStr object between other strings
my_color_str = ColorStr("What a randomly colorful string!", fg_color, bg_color)
print("===>", my_color_str, "<===")

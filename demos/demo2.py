# Daniel Fletcher
# Harvard CS50P 2024
# Final Project

# demo2.py
# Demonstration of package functionality (2 of 4)

from color50 import constants, css, hexcode
import sys

# Prompt and validate hex code input
input_hex = input("HEX color code: ")
try:
    color1 = hexcode(input_hex)
except (ValueError, TypeError):
    sys.exit("Error: Invalid HEX color code")

# Prompt and validate CSS color input
input_css = input("CSS color name: ")
try:
    color2 = css(input_css)
except (ValueError, TypeError):
    sys.exit("Error: CSS color name not recognized")

# Echo inputs back to user, except in color
print(f"HEX color code: {color1}{input_hex}{constants.RESET}")
print(f"CSS color name: {color2}{input_css}{constants.RESET}")

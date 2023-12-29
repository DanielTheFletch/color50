# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# project.py
# Contains main function for project

# Python library imports
from json import load
from re import fullmatch

# color50 imports
from color import Color
from colorstr import ColorStr
from constants import *


def main():
    print_warning("This is a warning message.")


def rgb(red: int, green: int, blue: int) -> Color:
    color = Color()
    color.red, color.green, color.blue = red, green, blue
    return color


def hexcode(code: str) -> Color:

    # Check that parameter is a string
    if not isinstance(code, str):
        raise TypeError(f"Expected hexadecimal value as string, got object of type {type(code)}")
    
    # Validate string
    regex = r"#?([0-9,A-F,a-f]{2})([0-9,A-F,a-f]{2})([0-9,A-F,a-f]{2})"
    if match := fullmatch(regex, code):
        r, g, b = match.groups()
        return rgb(int(r, base=16), int(g, base=16), int(b, base=16))
    else:
        raise ValueError("Invalid six-digit hexadecimal string format")
    

def css(colorname: str) -> Color:

    # Check that parameter is a string
    if not isinstance(colorname, str):
        raise TypeError(f"Expected CSS color name as string, got object of type {type(colorname)}")
    
    # Extract list of colors from JSON file
    colornames = {}
    with open("csscolors.json", "r") as file:
        colornames = load(file)

    # Validate color choice
    if colorname in colornames:
        return hexcode(colornames[colorname])
    else:
        raise ValueError(f"CSS color name \'{colorname}\' not recognized")
    

def colorize(color: Color | str):
    if isinstance(color, str):
        regex = r"\u001b\[(3|4|9|10)[0-7]m"
        if not fullmatch(regex, color):
            raise ValueError(f"ANSI character sequence \'{color}\' not recognized")
    elif not isinstance(color, Color):
        raise TypeError(f"Expected Color or string, got object of type {type(color)}")
    
    def decorate(func):
        if not callable(func):
            raise TypeError(f"Expected callable object, got object of type {type(func)}")
        
        def wrapper(*args, **kwargs):
            if color: print(color, end="")
            func(*args, **kwargs)
            print(RESET, end="")
        return wrapper
    return decorate


@colorize(5)
def print_warning(message):
    print(message)


if __name__ == "__main__":
    main()

# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# project.py
# Contains main function for project

# Python library imports
from re import fullmatch

# color50 imports
from color import Color, RESET


def main():
    color1 = hexcode("#FF00FF")
    print(color1 + "Testing hexcode function" + RESET)


def rgb(red: int, green: int, blue: int) -> Color:
    color = Color()
    color.red = red
    color.green = green
    color.blue = blue
    return color


def hexcode(code: str) -> Color:

    # Check that parameter is a string
    if not isinstance(code, str):
        raise TypeError(f"Expected hexadecimal string, got value of type {type(code)}")
    
    # Validate string
    regex = r"#([0-9,A-F,a-f]{2})([0-9,A-F,a-f]{2})([0-9,A-F,a-f]{2})"
    if match := fullmatch(regex, code):
        r, g, b = match.groups()
        return rgb(int(r, base=16), int(g, base=16), int(b, base=16))
    else:
        raise ValueError("Expected six-digit hexadecimal string")


if __name__ == "__main__":
    main()

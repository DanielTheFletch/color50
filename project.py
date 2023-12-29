# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# project.py
# Contains main function for project

# Python library imports
from json import load
from re import fullmatch

# color50 imports
from color import Color, RESET
from colorstr import ColorStr


def main():
    message = ColorStr("Testing ColorStr class", rgb(128, 0, 128))
    print(message)
    message.fg = css("goldenrod")
    print(message)
    message.fg = None
    print(message)


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
        raise ValueError("Expected valid six-digit hexadecimal string")
    

def css(colorname: str) -> Color:

    # Check that parameter is a string
    if not isinstance(colorname, str):
        raise TypeError(f"Expected CSS color name as string, got value of type {type(colorname)}")
    
    # Extract list of colors from JSON file
    colornames = {}
    with open("csscolors.json", "r") as file:
        colornames = load(file)

    # Validate color choice
    if colorname in colornames:
        hex_str = colornames[colorname]
        return hexcode(hex_str)
    else:
        raise ValueError("Expected valid CSS color name")


if __name__ == "__main__":
    main()

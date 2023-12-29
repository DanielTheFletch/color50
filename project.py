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
    color1 = rgb(128, 0, 128)
    color2 = css("cyan")
    color3 = hexcode("#FFFF00")
    print(f"{color1}Color 1\n{color2}Color 2\n{color3}Color 3{RESET}")


def rgb(red: int, green: int, blue: int) -> Color:
    color = Color()
    color.red, color.green, color.blue = red, green, blue
    return color


def hexcode(code: str) -> Color:

    # Check that parameter is a string
    if not isinstance(code, str):
        raise TypeError(f"Expected hexadecimal value as string, got object of type {type(code)}")
    
    # Validate string
    regex = r"#([0-9,A-F,a-f]{2})([0-9,A-F,a-f]{2})([0-9,A-F,a-f]{2})"
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
    

def colorize(fg: Color, bg: Color = None):
    def decorate(func):
        if not callable(func):
            raise TypeError(f"Expected callable object, got object of type {type(func)}")
        
        def wrapper(*args, **kwargs):
            if fg: print(fg, end="")
            if bg: print(bg, end="")
            func(*args, **kwargs)
            print(RESET, end="")
        return wrapper
    return decorate


@colorize(css("red"))
def print_warning(message):
    print(message)


if __name__ == "__main__":
    main()

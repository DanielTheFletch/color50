"""Standalone functions designed to streamline color selection and usage.

Although the Color class exists as part of the greater ``color50`` package,
3 of the 4 functions in this module are recommended to generate Color objects
themselves as opposed to explicitly calling the class initializer.

The fourth and final function in the module is a decorator function designed
to change the color of one function's standard output.

"""

# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# core_functions.py
# Four main project functions (rgb, hexcode, css, colorize)
# Same as four functions in required project.py file

# Python library imports
from json import load
from re import fullmatch

# Associated color50 imports
from color import Color
from constants import RESET


def rgb(red: int, green: int, blue: int) -> Color:
    """Return a Color object based on specified RGB values.
    
    One of three recommended methods for creating Color objects. Because the
    Color class stores RGB values internally, this function essentially mirrors
    the behavior of a would-be parameterized ``__init__`` function.

    Args:
        red:
            A numeric value (0-255) representing the color's red levels.
        green:
            A numeric value (0-255) representing the color's green levels.
        blue:
            A numeric value (0-255) representing the color's blue levels.

    Returns:
        A valid Color object.

    Note:
        Because this function sets the Color class properties to the values of
        the specified parameters, it will raise the same exceptions as the
        corresponding property setters.

    Examples::

        color1 = rgb(0, 0, 0)       # black
        color2 = rgb(255, 255, 255) # white
        color3 = rgb(128, 0, 128)   # purple

    """

    color = Color()
    color.red, color.green, color.blue = red, green, blue
    return color


def hexcode(code: str) -> Color:
    """Return a Color object based on a specified HEX color code.
    
    One of three recommended methods for creating Color objects. Designed to
    enable compatibility with colors used in other projects defined with
    six-digit hexadecimal codes.

    Args:
        code:
            A string representation of a HEX color code. Can contain optional
            leading hash sign (``\'#\'``) and can make use of uppercase or
            lowercase letters.

    Returns:
        A valid Color object.

    Raises:
        TypeError:
            If ``code`` is not a string.
        ValueError:
            If ``code`` is not a valid HEX color code or is formatted incorrectly.

    Examples::

        color1 = hexcode(\"#000000\")   # black
        color2 = hexcode(\"FFFFFF\")    # white
        color3 = hexcode(\"#00ffff\")   # cyan

    """

    # Check that parameter is a string
    if not isinstance(code, str):
        raise TypeError(f"Expected hexadecimal value as string, got object of type {type(code)}")
    
    # Validate string
    regex = r"#?([0-9,A-F,a-f]{2})([0-9,A-F,a-f]{2})([0-9,A-F,a-f]{2})"
    if match := fullmatch(regex, code):
        r, g, b = match.groups()
        return rgb(int(r, base=16), int(g, base=16), int(b, base=16))
    else:
        raise ValueError(f"Invalid six-digit hexadecimal string \'{code}\'")
    

def css(colorname: str) -> Color:
    """Return a Color object based on a specified CSS color name.
    
    One of three recommended methods for creating Color objects. Designed to
    enable compatibility with colors specified by name in CSS stylesheets.

    For a full list of named CSS colors, visit 
    https://developer.mozilla.org/en-US/docs/Web/CSS/named-color.

    Args:
        colorname:
            A string literal of a valid CSS color name.

    Returns:
        A valid Color object.

    Raises:
        TypeError:
            If ``colorname`` is not a string.
        ValueError:
            If ``colorname`` is not among the list of recognized CSS color names.

    Examples::

        color1 = css(\"black\")     # black
        color2 = css(\"white\")     # white
        color3 = css(\"seagreen\")  # seagreen

    """

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
    """Alter the color of a given function's standard output.
    
    This function is designed to be used as a decorator as a quick way of
    altering the output of any one function.

    Args:
        color:
            A valid Color object or a constant string literal representing a color.

    Raises:
        TypeError:
            If ``color`` is not a Color or string, or if the decorated object is not callable.
        ValueError:
            If ``color`` is a string representing an invalid ANSI color code character sequence

    Consider this example::

        @colorize(css(\"red\"))
        def print_warning(msg):
            print(msg)

    This would ensure that all contents of ``msg`` are printed to standard output
    with a red coloring, and also that the color of standard output resets to
    default after the function terminates.

    Note that this works with both foreground and background colors, or even both
    at the same time by stacking two decorators on top of one another.

    Consider this example::

        @colorize(constants.RED)
        @colorize(constants.GREEN_BG)
        def holiday_message(msg):
            print(msg)

    This would ensure that all contents of ``msg`` are printed to standard output
    with a red foreground coloring and a green background coloring, and also
    resetting both colors to defaults after termination.
    
    """

    # Validate color choice
    if isinstance(color, str):
        regex = r"\u001b\[(3|4|9|10)[0-7]m"
        if not fullmatch(regex, color):
            raise ValueError(f"ANSI character sequence \'{color}\' not recognized")
    elif not isinstance(color, Color):
        raise TypeError(f"Expected Color or string, got object of type {type(color)}")
    
    def decorate(func):
        # Validate that a callable object is passed
        if not callable(func):
            raise TypeError(f"Expected callable object, got object of type {type(func)}")
        
        # Wrapper function
        def wrapper(*args, **kwargs):
            print(color, end="")
            func(*args, **kwargs)
            print(RESET, end="")
        return wrapper
    return decorate
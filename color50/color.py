"""Contains the **Color** class and its implementation."""

# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# color.py
# Color class and related functionality

from constants import *

class Color:
    """A class for representing colors in RGB format.
    
    Designed to be used in conjunction with strings at the terminal for
    more colorful printing. Also used alongside other components of the
    :doc:`color50 package </color50>`.

    In addition to the properties and methods outlined, the **Color**
    class can be used in other contexts:
    
        - Supports string concatenation (in the form of ``Color + str``)
        - Has a built-in string conversion implemented as ``__str__`` override
        - Has built in == / != operator overloads for comparing two **Color** objects

    Note:
        Make sure to use the ``RESET`` constant when combining strings with **Color**
        objects&mdash;the color settings will not revert unless explicitly specified!

    """

    def __init__(self):
        """Initialize a default `Color` object with values R: ``0``, G: ``0``, B: ``0``.
        
        Note that there are no parameterized ``__init___`` functions for the
        ``Color`` class; instead, it is recommended to use one of the associated
        :ref:`core functions <core-functions-label>` that come with the package.

        """

        self.red = 0
        self.green = 0
        self.blue = 0

    def __str__(self):
        return self.fg()
    
    def __add__(self, string: str) -> str:
        if isinstance(string, str):
            return str(self) + string
        else:
            return NotImplemented
    
    def __eq__(self, other) -> bool:
        return (isinstance(other, Color) 
                and self.red == other.red
                and self.green == other.green
                and self.blue == other.blue)
    
    def __ne__(self, other) -> bool:
        return not (self == other)

    @property
    def red(self):
        """int: Numeric value for amount of red in `Color`, ranging from 0-255."""
        return self._red
    
    @red.setter
    def red(self, red: int):
        if isinstance(red, int):
            if 0 <= red <= 255:
                self._red = red
            else:
                raise ValueError(f"Invalid rgb value, {red} not in range [0, 255]")
        else:
            raise TypeError(f"Expected rgb value as integer, got object of type {type(red)}")

    @property
    def green(self):
        """int: Numeric value for amount of green in `Color`, ranging from 0-255."""
        return self._green
    
    @green.setter
    def green(self, green: int):
        if isinstance(green, int):
            if 0 <= green <= 255:
                self._green = green
            else:
                raise ValueError(f"Invalid rgb value, {green} not in range [0, 255]")
        else:
            raise TypeError(f"Expected rgb value as integer, got object of type {type(green)}")

    @property
    def blue(self):
        """int: Numeric value for amount of red in `Color`, ranging from 0-255."""
        return self._blue
    
    @blue.setter
    def blue(self, blue: int):
        if isinstance(blue, int):
            if 0 <= blue <= 255:
                self._blue = blue
            else:
                raise ValueError(f"Invalid rgb value, {blue} not in range [0, 255]")
        else:
            raise TypeError(f"Expected rgb value as integer, got object of type {type(blue)}")

    def fg(self) -> str:
        """Return string representation of color for use in foreground.

        The return value of this function is the default behavior of converting
        a **Color** object to a string. The option to call ``fg`` explicitly
        has been included for completeness, readability, and consistency.
        
        Returns:
            The ANSI color code sequence representation of the object, specifically
            to use as a foreground color.

        """

        rgb = f"{self.red};{self.green};{self.blue}"
        return f"{ANSI_PREFIX}[38;2;{rgb}m"
    
    def bg(self) -> str:
        """Return string representation of color for use in background.
        
        Returns:
            The ANSI color code sequence representation of the object, specifically
            to use as a background color.
            
        """

        rgb = f"{self.red};{self.green};{self.blue}"
        return f"{ANSI_PREFIX}[48;2;{rgb}m"

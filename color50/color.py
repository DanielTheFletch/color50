# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# color.py
# Color class and related functionality

from constants import *

class Color:
    """Color class"""

    def __init__(self):
        """__init__"""
        self.red = 0
        self.green = 0
        self.blue = 0

    def __str__(self):
        """__str__"""
        return self.fg()
    
    def __add__(self, string: str) -> str:
        """__add__"""
        if isinstance(string, str):
            return str(self) + string
        else:
            return NotImplemented
    
    def __eq__(self, other) -> bool:
        """__eq__"""
        return (isinstance(other, Color) 
                and self.red == other.red
                and self.green == other.green
                and self.blue == other.blue)
    
    def __ne__(self, other) -> bool:
        """__ne__"""
        return not (self == other)

    @property
    def red(self) -> int:
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
    def green(self) -> int:
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
    def blue(self) -> int:
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

    def fg(self):
        """fg function"""
        rgb = f"{self.red};{self.green};{self.blue}"
        return f"{ANSI_PREFIX}[38;2;{rgb}m"
    
    def bg(self):
        """bg function"""
        rgb = f"{self.red};{self.green};{self.blue}"
        return f"{ANSI_PREFIX}[48;2;{rgb}m"

# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# color.py
# Color class and related functionality

class Color:
    """Color class"""

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    @property
    def red(self) -> int:
        return self._red
    
    @red.setter
    def red(self, red: int):
        self._red = red

    @property
    def green(self) -> int:
        return self._green
    
    @green.setter
    def green(self, green: int):
        self._green = green

    @property
    def blue(self) -> int:
        return self._blue
    
    @blue.setter
    def blue(self, blue: int):
        self._blue = blue


def rgb(red: int, green: int, blue: int) -> Color:
    color = Color()
    color.red = red
    color.green = green
    color.blue = blue
    return color
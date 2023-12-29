# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# color.py
# Color class and related functionality

ANSI_PREFIX = "\u001b"
RESET = f"{ANSI_PREFIX}[0m"

class Color:
    """Color class"""

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def __str__(self):
        return self.fg()
    
    def __add__(self, string: str) -> str:
        return f"{self.fg()}{string}"
    
    def __eq__(self, other) -> bool:
        return (isinstance(other, Color) 
                and self.red == other.red
                and self.green == other.green
                and self.blue == other.blue)
    
    def __ne__(self, other) -> bool:
        return not (self == other)

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

    def fg(self):
        rgb = f"{self.red};{self.green};{self.blue}"
        return f"{ANSI_PREFIX}[38;2;{rgb}m"
    
    def bg(self):
        rgb = f"{self.red};{self.green};{self.blue}"
        return f"{ANSI_PREFIX}[48;2;{rgb}m"

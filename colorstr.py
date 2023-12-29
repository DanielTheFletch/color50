# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# color.py
# Color class and related functionality

from color import Color

class ColorStr:
    """ColorStr class"""

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __add__(self, addend):
        pass

    @property
    def content(self) -> str:
        return self._content
    
    @content.setter
    def content(self, content: str):
        self._content = content

    @property
    def fg(self) -> Color:
        return self._fg
    
    @fg.setter
    def fg(self, fg: Color):
        self._fg = fg

    @property
    def bg(self) -> Color:
        return self._bg
    
    @bg.setter
    def bg(self, bg: Color):
        self._bg = bg
# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# color.py
# Color class and related functionality

from color import Color
from constants import *

class ColorStr:
    """ColorStr class"""

    def __init__(self, content: str, fg: Color = None, bg: Color = None):
        """__init__"""
        self.content = content
        self.fg = fg
        self.bg = bg

    def __str__(self):
        """__str__"""
        fg_code = "" if self.fg == None else str(self.fg)
        bg_code = "" if self.bg == None else str(self.bg)
        return f"{fg_code}{bg_code}{self.content}{RESET}"

    def __add__(self, addend) -> str:
        """__add__"""
        if isinstance(addend, ColorStr) or isinstance(addend, str):
            return str(self) + str(addend)
        else:
            return NotImplemented


    @property
    def content(self) -> str:
        return self._content
    
    @content.setter
    def content(self, content: str):
        if isinstance(content, str):
            self._content = content
        else:
            raise TypeError(f"Expected string for ColorStr content, got {type(content)}")

    @property
    def fg(self) -> Color:
        return self._fg
    
    @fg.setter
    def fg(self, fg: Color | None):
        if isinstance(fg, Color) or fg == None:
            self._fg = fg
        else:
            raise TypeError(f"Expected valid Color object for foreground, got {type(fg)}")

    @property
    def bg(self) -> Color:
        return self._bg
    
    @bg.setter
    def bg(self, bg: Color | None):
        if isinstance(bg, Color) or bg == None:
            self._bg = bg
        else:
            raise TypeError(f"Expected valid Color object for background, got {type(bg)}")
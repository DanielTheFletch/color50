"""Contains the **ColorStr** class and its implementation."""

# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# color.py
# Color class and related functionality

from color import Color
from constants import *

class ColorStr:
    """A class for storing and using colorful strings.
    
    Stores string content alongside a foreground color and background color.
    Otherwise treated like standard strings in multiple contexts:
        - Supports string concatenation (both with strings and other **ColorStr**
        objects)
        - Has a built-in string conversion implemented as ``__str__`` override
        - Can be used in conjunction with ``print``, f-strings, and the like

    """

    def __init__(self, content: str, fg: Color = None, bg: Color = None):
        """Initializes a **ColorStr** object with content and optional fg/bg colors
        
        Placeholder text.

        Args:
            content:
                A standard string that will display in the specified color.
            fg:
                (optional) A Color object denoting the desired foreground color.
            bg:
                (optional) A Color object denoting the desired background color.

        Example::

            message = "Hello, World!"
            message_colorful = ColorStr(message, rgb(0, 0, 255))

            print(message)          # Prints message like normal
            print(message_colorful) # Prints same message, but in blue

        """

        self.content = content
        self.fg = fg
        self.bg = bg

    def __str__(self):
        fg_code = "" if self.fg == None else str(self.fg)
        bg_code = "" if self.bg == None else str(self.bg)
        return f"{fg_code}{bg_code}{self.content}{RESET}"

    def __add__(self, addend) -> str:
        if isinstance(addend, ColorStr) or isinstance(addend, str):
            return str(self) + str(addend)
        else:
            return NotImplemented


    @property
    def content(self):
        """str: The text to be displayed in color."""
        return self._content
    
    @content.setter
    def content(self, content: str):
        if isinstance(content, str):
            self._content = content
        else:
            raise TypeError(f"Expected string for ColorStr content, got {type(content)}")

    @property
    def fg(self):
        """Color: A Color object denoting the desired foreground color. If ``None``, uses
        default display color."""
        return self._fg
    
    @fg.setter
    def fg(self, fg: Color | None):
        if isinstance(fg, Color) or fg == None:
            self._fg = fg
        else:
            raise TypeError(f"Expected valid Color object for foreground, got {type(fg)}")

    @property
    def bg(self):
        """Color: A Color object denoting the desired background color. If ``None``, uses
        default display color."""
        return self._bg
    
    @bg.setter
    def bg(self, bg: Color | None):
        if isinstance(bg, Color) or bg == None:
            self._bg = bg
        else:
            raise TypeError(f"Expected valid Color object for background, got {type(bg)}")

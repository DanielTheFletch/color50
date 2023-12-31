"""The **ColorStr** class and its implementation."""

# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# color.py
# Color class and related functionality

from color import Color
from constants import RESET

class ColorStr:
    """A class for representing specialized strings with custom color properties.
    
    Stores string content alongside a foreground color and background color.
    Note that the use of the ``RESET`` constant is not required when working
    with **ColorStr** objects.

    Example::

        msg = \"Warning: An error has occurred.\"
        fg = css(\"red\")
        bg = css(\"darkgray\")

        my_color_str = ColorStr(msg, fg, bg)
        print(my_color_str)     # Prints red text on dark gray background
        
    """

    def __init__(self, content: str, fg: Color | None = None, bg: Color | None = None):
        """Initialize a **ColorStr** object with content and optional fg/bg colors.
        
        Note that **None** is an accepted value for both the ``fg`` and ``bg``
        parameters. When either is set to **None**, any future usage of the
        object for printing will disregard the property and use the default
        configuration. 

        Args:
            content:
                A standard string that will display in the specified color.
            fg:
                (optional) A Color object denoting the desired foreground color.
            bg:
                (optional) A Color object denoting the desired background color.

        Example::

            message = "Hello, World!"
            message_colorful = ColorStr(message, hexcode(\"0000FF\"))

            print(message)          # Prints message like normal
            print(message_colorful) # Prints same message, but in blue

        """

        self.content = content
        self.fg = fg
        self.bg = bg

    def __str__(self):
        """Return a string representation of the **ColorStr** object.

        Converting a **ColorStr** to a pure **str** will retain the
        associated color properties, but such properties will no
        longer be directly editable.
        
        Example 1::

            my_color_str = ColorStr(\"Hello, World!\", None, css(\"crimson\"))
            print(str(my_color_str) + \" ...and goodbye, color.\")

        Example 2::

            my_color_str = str(ColorStr(\"Hello, World!\", None, css(\"crimson\")))
            print(my_color_str)

        """

        fg_code = "" if self.fg == None else str(self.fg)
        bg_code = "" if self.bg == None else str(self.bg)
        return f"{fg_code}{bg_code}{self.content}{RESET}"

    def __add__(self, addend) -> str:
        """Support concatenation of **ColorStr** objects with **str** objects
        and of **ColorStr** objects with other **ColorStr** objects.
        
        Example 1::

            str1 = ColorStr(\"This text is colorful, and... \", rgb(100, 120, 140))
            str2 = \"this text is plain.\"
            print(str1 + str2)

        Example 2::

            str1 = ColorStr(\"This text is colorful, and... \", rgb(100, 120, 140))
            str2 = ColorStr(\"this text is also colorful!\", rgb(140, 120, 100))
            print(str1 + str2)

        """

        if isinstance(addend, ColorStr) or isinstance(addend, str):
            return str(self) + str(addend)
        else:
            return NotImplemented 

    def __eq__(self, other) -> bool:
        """Support equality comparisons of two **ColorStr** objects.
        
        Two objects of type **ColoStrr** are defined to be equal if
        and only if:

            - ``str1.content == str2.content`` is **True** (e.g., string content is identical),
            - ``str1.fg == str2.fg`` is **True**,
            - and ``str1.bg == str2.bg`` is **True**.

        Both equality operators (``==`` and ``!=``) are supported.

        Example::

            str1 = ColorStr(\"Hello, World!\", css(\"red\"), css(\"beige\"))
            str2 = ColorStr(\"Hello, World\", css(\"red\"), css(\"beige\"))
            str3 = ColorStr(\"Hello, World!\", css(\"red\"), css(\"blanchedalmond\"))

            print(str1 == str2)     # False
            print(str2 == str3)     # False
            print(str1 == str3)     # False

            str4 = ColorStr(\"Hello, World!\", css(\"red\"), css(\"beige\"))

            print(str1 == str4)     # True
        
        """

        return (isinstance(other, Color) 
                and self.red == other.red
                and self.green == other.green
                and self.blue == other.blue)
    
    def __ne__(self, other) -> bool:
        return not (self == other)

    @property
    def content(self):
        """str: The string to be displayed in color. Supports both get and set
        operations.

        Raises:
            TypeError:
                If the property is not set to a **str** value.

        """

        return self._content
    
    @content.setter
    def content(self, content: str):
        if isinstance(content, str):
            self._content = content
        else:
            raise TypeError(f"Expected string for ColorStr content, got {type(content)}")

    @property
    def fg(self):
        """Color: A **Color** object denoting the desired foreground color. Supports
        both get and set operations. If set to ``None``, the property will be
        disregarded when the object is displayed.

        Raises:
            TypeError:
                If the property is not set to a valid **Color** object.

        """

        return self._fg
    
    @fg.setter
    def fg(self, fg: Color | None):
        if isinstance(fg, Color) or fg == None:
            self._fg = fg
        else:
            raise TypeError(f"Expected valid Color object for foreground, got {type(fg)}")

    @property
    def bg(self):
        """Color: A **Color** object denoting the desired background color. Supports
        both get and set operations. If set to ``None``, the property will be
        disregarded when the object is displayed.

        Raises:
            TypeError:
                If the property is not set to a valid **Color** object.

        """

        return self._bg
    
    @bg.setter
    def bg(self, bg: Color | None):
        if isinstance(bg, Color) or bg == None:
            self._bg = bg
        else:
            raise TypeError(f"Expected valid Color object for background, got {type(bg)}")

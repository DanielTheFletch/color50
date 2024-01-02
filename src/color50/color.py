"""The **Color** class and its implementation."""

# Daniel Fletcher
# Harvard CS50P 2024
# Final Project

# color.py
# Color class and related functionality

from .constants import ANSI_PREFIX

class Color:
    """A class for representing color in RGB format.

    Represents any given color by storing its RGB values---that is, its
    red level (0-255), green level (0-255), and blue level (0-255). Once
    a **Color** object has its RGB values set, it can be used to add color
    to strings via concatenation.
    
    Also designed to be used in conjunction with other key components of the
    package, like the **ColorStr** class or the ``colorize`` decorator function.

    Example::

        # Normal print statement (behaves as expected)
        print(\"Not in Color.\")

        my_color = rgb(128, 0, 128)

        # Colorized print statement (prints string contents in purple)
        print(my_color + \"Now in Color!\" + constants.RESET)

    Note:
        Make sure to use the ``RESET`` constant when combining strings with **Color**
        objects; the color settings of your terminal environment will not revert to 
        defaults unless explicitly specified!

    """

    def __init__(self):
        """Initialize a **Color** object with red, green, and blue values all set to ``0``.
        
        Note that there are no parameterized ``__init___`` functions for the
        ``Color`` class; instead, it is recommended to use one of the associated
        :ref:`core functions <core-functions-module-label>` that come with the package
        instead of using the class initializer explicitly.

        That said, the default initializer can still be called, and each of the
        object properties (red, green, blue) can be tweaked individually from their
        default ``0`` values.

        Example::
        
            # Normal print statement (behaves as expected)
            print(\"Not in Color.\")

            my_color = Color()
            my_color.red = 128
            my_color.green = 0
            my_color.blue = 128

            # Colorized print statement (prints string contents in purple)
            print(my_color + \"Now in Color!\" + constants.RESET)

        """

        self.red = 0
        self.green = 0
        self.blue = 0

    def __str__(self):
        """Return a string representation of the color; same as calling
        the ``fg`` method.
        
        Example::

            my_color = rgb(0, 0, 255)
            print(f\"{my_color}f-strings make me feel blue.{constants.RESET}\")

        """

        return self.fg()
    
    def __add__(self, string: str) -> str:
        """Support concatenation of **Color** and **str** objects.
        
        Example::

            my_color = rgb(0, 255, 0)
            my_message = \"Hello, Green World!\"
            print(my_color + my_message + constants.RESET)

        """

        if isinstance(string, str):
            return str(self) + string
        else:
            return NotImplemented
    
    def __eq__(self, other) -> bool:
        """Support equality comparisons of two **Color** objects.
        
        Two objects of type **Color** are defined to be equal if
        and only if:

            - ``color1.red == color2.red`` is **True**,
            - ``color1.green == color2.green`` is **True**,
            - and ``color1.blue == color2.blue`` is **True**.

        Both equality operators (``==`` and ``!=``) are supported.

        Example::

            color1 = rgb(255, 255, 0)
            color2 = hexcode(\"#ffff00\")
            color3 = css(\"blue\")

            print(color1 == color2)     # True
            print(color2 == color3)     # False
            print(color1 == color3)     # False
        
        """

        return (isinstance(other, Color) 
                and self.red == other.red
                and self.green == other.green
                and self.blue == other.blue)
    
    def __ne__(self, other) -> bool:
        return not (self == other)

    @property
    def red(self):
        """int: Numeric value for amount of *red* in the color, ranging from 0-255.
        Supports both get and set operations.

        Raises:
            TypeError:
                If the property is set to a non-integer value.
            ValueError:
                If the property is set to an out-of-range integer (e.g., not in range 0-255).

        """
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
        """int: Numeric value for amount of *green* in the color, ranging from 0-255.
        Supports both get and set operations.

        Raises:
            TypeError:
                If the property is set to a non-integer value.
            ValueError:
                If the property is set to an out-of-range integer (e.g., not in range 0-255).

        """
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
        """int: Numeric value for amount of *blue* in the color, ranging from 0-255.
        Supports both get and set operations.

        Raises:
            TypeError:
                If the property is set to a non-integer value.
            ValueError:
                If the property is set to an out-of-range integer (e.g., not in range 0-255).

        """
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
        """Return a string representation of the stored color for foreground use.

        The return value of this function is the default behavior of converting
        a **Color** object to a string. The option to call ``fg`` explicitly
        has been included for completeness, readability, and consistency.
        
        Returns:
            The ANSI color code sequence representation of the object, specifically
            to use as a foreground color.

        Example::

            my_color = rgb(0, 128, 64)
            print(my_color.fg() + "This text is so colorful!" + constants.RESET)

        """

        rgb = f"{self.red};{self.green};{self.blue}"
        return f"{ANSI_PREFIX}[38;2;{rgb}m"
    
    def bg(self) -> str:
        """Return a string representation of the stored color for background use.
        
        Returns:
            The ANSI color code sequence representation of the object, specifically
            to use as a background color.

        Example::

            my_color = rgb(30, 120, 15)
            print(my_color.bg() + "What a gorgeous background!" + constants.RESET)
            
        """

        rgb = f"{self.red};{self.green};{self.blue}"
        return f"{ANSI_PREFIX}[48;2;{rgb}m"

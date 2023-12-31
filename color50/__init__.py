"""A lightweight Python package for more colorful printing at the terminal.

Created as a final project submission for Harvard University's CS50P course,
**color50** is a package designed to add a little extra flavor to standard
output print statements. Who knows, maybe future CS50 students may find this
package useful---or fun!

Modules included:
    - color
        - **Color** class
    - core_functions
        - ``rgb()`` function
        - ``hexcode()`` function
        - ``css()`` function
    - colorstr
        - **ColorStr** class
    - constants

"""

# Daniel Fletcher
# Harvard CS50P 23023
# Final Project

# __init__.py
# Initialization file for color50 package

# Import class modules
from .color import Color
from .colorstr import ColorStr

# Import core functions
from .core_functions import rgb
from .core_functions import hexcode
from .core_functions import css
from .core_functions import colorize

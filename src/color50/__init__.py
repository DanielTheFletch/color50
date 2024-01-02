"""A lightweight Python package for colorful output at the command line.

Created as a final project submission for Harvard University's CS50P course,
**color50** is a package I designed to add a little extra flavor to standard
output print statements. This is my first ever attempt at making a Python
package from scratch, and I'm excited to share it with fellow Python developers
and CS50 students.

Modules included:
    - color
        - **Color** class
    - core_functions
        - ``rgb`` function
        - ``hexcode`` function
        - ``css`` function
    - colorstr
        - **ColorStr** class
    - constants

"""

# Daniel Fletcher
# Harvard CS50P 2024
# Final Project

# __init__.py
# Initialization file for color50 package

# Import classes by name
from .color import Color
from .colorstr import ColorStr

# Import core functions by name
from .core_functions import rgb
from .core_functions import hexcode
from .core_functions import css
from .core_functions import colorize

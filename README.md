# color50

A lightweight Python package for colorful output at the command line.

Created as a final project submission for Harvard University's CS50P course,
**color50** is a package I designed to add a little extra flavor to standard
output print statements. This is my first ever attempt at making a Python
package from scratch, and I'm excited to share it with fellow Python developers
and CS50 students.

## Included modules

- color
    - **Color** class
- core_functions
    - ``rgb`` function
    - ``hexcode`` function
    - ``css`` function
    - ``colorize`` function (decorator)
- colorstr
    - **ColorStr** class
- constants

## Installation

To install **color50**, execute the following command using the `pip` installer:

```
pip install color50
```

## Sample usage

With **color50** installed, the following code would print `"Hello, World!"` to standard output as purple-colored text.

```py
from color50 import rgb, constants

my_color = rgb(128, 0, 128)
print(my_color + "Hello, World!" + constants.RESET)
```

<br>

For more detailed information on using **color50** in your Python projects, please refer to the documentation at [color50.readthedocs.io](https://color50.readthedocs.io/).

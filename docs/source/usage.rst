Usage Guide
===========

Read this guide to learn about the key features of **color50** and how to best
make use of them. For additional code examples, refer to the :doc:`demo files</demo>`
included with the documentation.

----------

Using the **Color** class
-------------------------

Representing colors in Python code is at the heart of **color50**, and the **Color**
class is one way to achieve this goal.

Foundations
***********

The **Color** class represents a color by storing its RGB values. The RGB color model
is a way of representing colors using three values: red, green, and blue. Each of these
values are an integer with a value of 0-255 representing the "amount" of red/green/blue
in the color. (Read `this article`_ for more information on RGB color.)

.. _this article: https://en.wikipedia.org/wiki/RGB_color_model

For example, suppose you want to store the color *red* in an object of type **Color**.
Consider this example program::

    # Import Color class
    from color50 import Color

    # Initialize Color object
    my_color = Color()

    # Set red property to 255 (max value)
    my_color.red = 255

The ``my_color`` object now stores RGB values such that ``R = 255``, ``G = 0``, and
``B = 0``, thus representing the color *red*.

Notice that the *green* and *blue* properties were not specified. According to the
:ref:`Color class documentation<color-module-label>`, each of the three properties
initializes to a value of ``0``. In other words, the default color created by calling
``Color()`` is black (e.g., ``R = 0``, ``G = 0``, and ``B = 0``).

Consider another example program::

    from color50 import Color

    # First color: black
    color1 = Color()

    # Second color: white
    color2 = Color()
    color2.red = 255
    color2.green = 255
    color2.blue = 255

    # Third color: purple
    color3 = Color()
    color3.red = 128
    color3.blue = 128

Notice again how all properties default to ``0``, resulting in some properties not needing
to be changed manually.

Working with strings
********************

With a solid knowledge of the semantics of the **Color** class, we can now put that knowledge
to practical use.

As described in the :ref:`Color class documentation<color-module-label>`, **Color** objects
support concatenation with strings to effectively add color to them. This can be done with string
literals or strings stored as variables. Note that the **Color** object must always come first in
the operation, meaning ``Color + str`` is valid but ``str + Color`` is not.

Example::

    from color50 import Color, constants

    # Variables for warning
    warning_color = Color()
    warning_color.red = 255
    warning_message = "WARNING"

    # Variables for success
    success_color = Color()
    success_color.green = 255

    # Print warning message (in red)
    print(warning_color + warning_message + constants.RESET)

    # Print success message (in green)
    print(success_color + "SUCCESS" + constants.RESET)

Notice the inclusion of the ``constants.RESET`` variable at the end of each print statement. When
using **Color** objects with strings in this fashion, including the ``RESET`` constant after the
colorful string is needed to revert the terminal colors to their defaults. While it does not
necessarily need to follow *every* colorful string, unexpected behaviors may occur if ``RESET``
is never used.

Here's another example using some different formats::

    from color50 import Color, constants

    # Create color blue
    my_color = Color()
    my_color.blue = 255

    # Three identical print statements
    print(my_color + "I've got the blues." + constants.RESET)
    print(f"{my_color}I've got the blues.{constants.RESET}")
    print(my_color, "I've got the blues.", constants.RESET, sep="")

The last three print statements each produce the exact same output. This allows for greater
flexibility when working with **Color** objects in your code.

Using the ``fg`` and ``bg`` methods
***********************************

In addition to changing the color of the terminal text, the **Color** class also allows for
changing the background color that appears behind the text. Use ``fg`` to denote foreground
usage and ``bg`` to denote background usage.

Example::

    from color50 import Color, constants

    # Create color yellow
    my_color = Color()
    my_color.red = 255
    my_color.green = 255

    # Print yellow text on plain background
    print(f"{my_color.fg()}Yellow, is anyone there?{constants.RESET}")

    # Print plain text on yellow background
    print(f"{my_color.bg()}Yellow, is anyone there?{constants.RESET}")

The ``fg`` and ``bg`` methods are used in the same way that **Color** objects have
in the previous examples.

Under the hood, concatenating **Color** objects with strings actually just converts
the **Color** to a string representation of its ANSI color code before performing
standard string concatenation. Effectively, this means that ``str(my_color)`` and
``my_color.fg()`` return the same output.

Another example using foreground/background colors simultaneously::

    from color50 import Color, constants

    # Create earth colors
    earth_green, earth_blue = Color(), Color()
    earth_green.green = 255
    earth_blue.blue = 255

    # Print green text on blue background
    print(
        earth_green + 
        earth_blue.bg() +
        "Hello! It's me, World!" +
        constants.RESET
    )

Notice that the ``earth_green`` foreground color did not need to explicitly call
the ``fg`` method to produce the intended results. (The ``fg`` method is mostly
included for those who want explicit clarity when also working with the ``bg``
method.)

----------

Using ``rgb``, ``hexcode``, and ``css``
---------------------------------------

Now that we've covered the **Color** class and its usage with strings, we can jump
into three of the four functions in the core_functions module. These functions are
designed to streamline the creation of a given **Color** object, removing the need
to manually enter each RGB value after initialization.

The ``rgb`` function
********************

This function allows for setting the **Color** object's properties in the same way as before,
but now in only one line of code.

``rgb`` takes in three parameters (red, green, and blue values, as used before) and returns a
valid **Color** object whose properties have been initialized to the parameter values.

Example program::

    from color50 import constants, rgb

    # Create yellow, magenta, and cyan colors
    color1 = rgb(255, 255, 0)
    color2 = rgb(255, 0, 255)
    color3 = rgb(0, 255, 255)

    # Print colorful text
    print(f"{color1}This text is yellow.{constants.RESET}")
    print(f"{color2}{color3.bg()}This text is magenta with a cyan background.{constants.RESET}")

For more information regarding the function's parameters and usage details, refer to
:ref:`its section of the documentation<core-functions-module-label>`.

The ``hexcode`` function
************************

This function enables using a different color formatting (six-digit hexadecimal codes) to
initialize a **Color** object.

``hexcode`` takes in one parameter (a HEX color code, as a string) and returns a
valid **Color** object whose properties have been initialized to match the color represented
by the specified HEX color code.

Example program::

    from color50 import constants, hexcode

    # Create yellow, magenta, and cyan colors
    color1 = hexcode("#FFFF00")
    color2 = hexcode("#FF00FF")
    color3 = hexcode("#00FFFF")

    # Print colorful text
    print(f"{color1}This text is yellow.{constants.RESET}")
    print(f"{color2}{color3.bg()}This text is magenta with a cyan background.{constants.RESET}")

Note that the HEX color code can use uppercase or lowercase letters, and the leading ``'#'`` symbol
is optional. Let's rewrite a snippet of the previous example to demonstrate::

    # Create yellow, magenta, and cyan colors
    color1 = hexcode("#ffff00")
    color2 = hexcode("FF00FF")
    color3 = hexcode("00ffff")

This version of the code is functionally identical to the previous iteration. While each of these
options are valid, it is recommended to use only one throughout a given file or project for stylistic
consistency.

For more information regarding the function's parameters and usage details, refer to
:ref:`its section of the documentation<core-functions-module-label>`.

The ``css`` function
********************

This function accepts a CSS color name and uses it to initialize a **Color** object. This allows
for the usage of more specific colors without needing to know their RGB value or HEX color code
representations.

``css`` takes in one parameter (a valid CSS color name, as a string) and returns a
valid **Color** object whose properties have been initialized to match the color represented
by the specified color name.

Example program::

    from color50 import constants, css

    # Create yellow, magenta, and cyan colors
    color1 = css("yellow")
    color2 = css("magenta")
    color3 = css("cyan")

    # Print colorful text
    print(f"{color1}This text is yellow.{constants.RESET}")
    print(f"{color2}{color3.bg()}This text is magenta with a cyan background.{constants.RESET}")

For more information regarding the function's parameters and usage details, refer to
:ref:`its section of the documentation<core-functions-module-label>`.

For more information regarding the list of valid color names, refer to `the official listing
from the MDN Web Docs`_.

.. _the official listing from the MDN Web Docs: https://developer.mozilla.org/en-US/docs/Web/CSS/named-color

----------

Using the **ColorStr** class
----------------------------

The **ColorStr** class takes all the building blocks described previously and encapsulates them
into a single, streamlined class.

**ColorStr** objects have three properties:

    - A string containing the soon-to-be-colorful text
    - A foreground color (optional)
    - A background color (optional)

With this design, **ColorStr** objects can be used for similar cases as in previous examples but
with more straightforward syntax.

Example::

    from color50 import ColorStr, css

    # Configure string content and fg/bg colors
    content = "Hello! It's me, World!"
    fg = css("green")
    bg = css("blue")

    # Create and print ColorStr object
    my_color_str = ColorStr(content, fg, bg)
    print(my_color_str)

The print statement in the above example prints the contents ``"Hello! It's me, World!"`` as green
text on a blue background. Notice how many of the smaller details from previous examples are no
longer necessary, like needing to distinguish between ``fg`` and ``bg`` use cases or needing to
include the ``RESET`` constant. All of this logic is handled by the **ColorStr** class!

**ColorStr** also supports concatenation with strings as well as with other **ColorStr** objects.
This concatenation behaves much like the concatenation of two standard strings, with the exception
that color is retained from any included **ColorStr** objects.

Example::

    from color50 import ColorStr, hexcode

    # Configure multiple strings
    str1 = "I love... "
    str2 = ColorStr("blue text", hexcode("0000ff"))
    str3 = ColorStr("blue backgrounds", None, hexcode("0000ff"))

    # Print to screen
    print(str1 + str2 + " and " + str3 + "!")

In the above example, only the contents of ``str2`` and ``str3`` will display their custom colors;
all other content will be printed using default settings.

For more information regarding the properties, methods, and other implementation details of
**ColorStr**, refer to the :ref:`ColorStr class documentation<colorstr-module-label>`.

----------

Using the included constants
----------------------------

The fourth and final module included with **color50** is the **constants** module. It contains
a variety of named constants for working with ANSI color codes on a more granular level.

These constants, however, can also be used like **Color** objects with respect to string
concatenation. They can offer simple, easy-access colors when not much else is needed.

Example::

    from color50 import constants

    # Print a red message to the screen
    print(constants.RED + "This is a red message." + constants.RESET)

    # Print a green message to the screen
    print(f"{constants.GREEN}This is a green message.{constants.RESET}")

    # Print a blue message to the screen
    print(constants.BLUE, "This is a blue message.", constants.RESET, sep="")

Note that the ``RESET`` constant is needed when using these color constants.

The majority of the included constants are variations of the same eight
standard ANSI colors, but two of them are for more specific use cases:

    - The ``ANSI_PREFIX`` constant contains the ANSI escape sequence that all other constants in the module make use of.
    - The ``RESET`` constant contains the ANSI code needed to restore default color settings.

Outside of those two outliers, the included constants represent the ANSI sequences needed to change
the color of any text that follows it.

These constants are much more limited in their usage insofar
as **color50** compatibility (i.e., **ColorStr** objects will not accept these constants as fg or
bg colors), but they can be used to work with and better understand the lower-level implementation
details of ANSI color code sequencing.

For more information regarding the full list of constants included with the module,
refer to the :ref:`its section of the documentation<constants-module-label>`.

----------

Using ``colorize``
------------------
The core_functions module mentioned previously contains one more function that has not yet been
discussed. That is the ``colorize`` function, a function designed to be used as a simple decorator
for coloring function output.

Consider the following example::

    from color50 import colorize, rgb

    @colorize(rgb(255, 0, 0))
    def print_warning(message: str):
        print(message)

With this setup, any calls to ``print_warning`` will produce output with red text. This offers a
very short and simple way to ensure that any and all output from a given function will be the
same color.

Note that the color constants from the constants module can also be used here::

    from color50 import colorize, constants

    @colorize(constants.RED)
    def print_warning(message: str):
        print(message)

For more information regarding the function's parameters and usage details, refer to
:ref:`its section of the documentation<core-functions-module-label>`.

"""A series of string literal constants for both simpler and more granular
color control.

Note:
    Because these constants are not encapsulated in any class or error-checking
    logic, using them may result in unintended side effects if not familiar
    with ANSI color code sequencing. Consult `this Wikipedia article 
    <https://en.wikipedia.org/wiki/ANSI_escape_code#Colors>`_ for more information.

For ANSI escape sequence manipulation:
    Use these constants to directly interface with the lower-level implementation
    of ANSI color code sequencing. ``RESET`` will also be *very* useful when
    working with **Color** objects and not **ColorStr** objects.

    ====================  =====================
    **Constant**          **String value**
    --------------------  ---------------------
    ANSI_PREFIX           ``\"\\u001b\"``
    RESET                 ``\"\\u001b[0m\"``
    ====================  =====================

    Example::

        # Print a message with magenta-colored text
        print(f\"{constants.ANSI_PREFIX}[35mHello, World!{constants.RESET}\")
    

For standard colors (foreground):
    Use these constants as shorthand for the eight standard ANSI color codes,
    specifically those that alter the foreground color. Make sure to use ``RESET``
    after using the desired color to avoid unexpected behavior.

    ====================  =====================
    **Constant**          **String value**
    --------------------  ---------------------
    BLACK                 ``\"\\u001b[30m\"``
    RED                   ``\"\\u001b[31m\"``
    GREEN                 ``\"\\u001b[32m\"``
    YELLOW                ``\"\\u001b[33m\"``
    BLUE                  ``\"\\u001b[34m\"``
    MAGENTA               ``\"\\u001b[35m\"``
    CYAN                  ``\"\\u001b[36m\"``
    WHITE                 ``\"\\u001b[37m\"``
    ====================  =====================

    Example::

        # Print a message with magenta-colored text
        print(f\"{constants.MAGENTA}Hello, World!{constants.RESET}\")

For standard colors (background):
    Use these constants as shorthand for the eight standard ANSI color codes,
    specifically those that alter the background color. Make sure to use ``RESET``
    after using the desired color to avoid unexpected behavior.

    ====================  =====================
    **Constant**          **String value**
    --------------------  ---------------------
    BLACK_BG              ``\"\\u001b[40m\"``
    RED_BG                ``\"\\u001b[41m\"``
    GREEN_BG              ``\"\\u001b[42m\"``
    YELLOW_BG             ``\"\\u001b[43m\"``
    BLUE_BG               ``\"\\u001b[44m\"``
    MAGENTA_BG            ``\"\\u001b[45m\"``
    CYAN_BG               ``\"\\u001b[46m\"``
    WHITE_BG              ``\"\\u001b[47m\"``
    ====================  =====================

    Example::

        # Print a message with a magenta-colored background
        print(constants.MAGENTA_BG + \"Hello, World!\" + constants.RESET)

For bright standard colors (foreground):
    Use these constants as shorthand for the eight standard ANSI *bright* color codes,
    specifically those that alter the foreground color. Make sure to use ``RESET``
    after using the desired color to avoid unexpected behavior.

    ===============================  =====================
    **Constant**                     **String value**
    -------------------------------  ---------------------
    BRIGHT_BLACK (or GRAY or GREY)   ``\"\\u001b[90m\"``
    BRIGHT_RED                       ``\"\\u001b[91m\"``
    BRIGHT_GREEN                     ``\"\\u001b[92m\"``
    BRIGHT_YELLOW                    ``\"\\u001b[93m\"``
    BRIGHT_BLUE                      ``\"\\u001b[94m\"``
    BRIGHT_MAGENTA                   ``\"\\u001b[95m\"``
    BRIGHT_CYAN                      ``\"\\u001b[96m\"``
    BRIGHT_WHITE                     ``\"\\u001b[97m\"``
    ===============================  =====================

    Example::

        # Print a message with bright, magenta-colored text
        print(constants.BRIGHT_MAGENTA + \"Hello, World!\" + constants.RESET)

For bright standard colors (background):
    Use these constants as shorthand for the eight standard ANSI *bright* color codes,
    specifically those that alter the background color. Make sure to use ``RESET``
    after using the desired color to avoid unexpected behavior.

    ========================================  =====================
    **Constant**                              **String value**
    ----------------------------------------  ---------------------
    BRIGHT_BLACK_BG (or GRAY_BG or GREY_BG)   ``\"\\u001b[100m\"``
    BRIGHT_RED_BG                             ``\"\\u001b[101m\"``
    BRIGHT_GREEN_BG                           ``\"\\u001b[102m\"``
    BRIGHT_YELLOW_BG                          ``\"\\u001b[103m\"``
    BRIGHT_BLUE_BG                            ``\"\\u001b[104m\"``
    BRIGHT_MAGENTA_BG                         ``\"\\u001b[105m\"``
    BRIGHT_CYAN_BG                            ``\"\\u001b[106m\"``
    BRIGHT_WHITE_BG                           ``\"\\u001b[107m\"``
    ========================================  =====================

    Example::

        # Print a message with a bright, magenta-colored background
        print(f\"{constants.BRIGHT_MAGENTA_BG}Hello, World!{constants.RESET}\")     

The source code for the module is included below for completeness.
Reference it as you wish::

    # constants.py
    # Constants for use across files

    # ANSI escape sequence manipulation
    ANSI_PREFIX = \"\\u001b\"
    RESET = f\"{ANSI_PREFIX}[0m\"

    # Standard colors (foreground)
    BLACK = f\"{ANSI_PREFIX}[30m\"
    RED = f\"{ANSI_PREFIX}[31m\"
    GREEN = f\"{ANSI_PREFIX}[32m\"
    YELLOW = f\"{ANSI_PREFIX}[33m\"
    BLUE = f\"{ANSI_PREFIX}[34m\"
    MAGENTA = f\"{ANSI_PREFIX}[35m\"
    CYAN = f\"{ANSI_PREFIX}[36m\"
    WHITE = f\"{ANSI_PREFIX}[37m\"

    # Standard colors (background)
    BLACK_BG = f\"{ANSI_PREFIX}[40m\"
    RED_BG = f\"{ANSI_PREFIX}[41m\"
    GREEN_BG = f\"{ANSI_PREFIX}[42m\"
    YELLOW_BG = f\"{ANSI_PREFIX}[43m\"
    BLUE_BG = f\"{ANSI_PREFIX}[44m\"
    MAGENTA_BG = f\"{ANSI_PREFIX}[45m\"
    CYAN_BG = f\"{ANSI_PREFIX}[46m\"
    WHITE_BG = f\"{ANSI_PREFIX}[47m\"

    # Bright standard colors (foreground)
    BRIGHT_BLACK = GREY = GRAY = f\"{ANSI_PREFIX}[90m\"
    BRIGHT_RED = f\"{ANSI_PREFIX}[91m\"
    BRIGHT_GREEN = f\"{ANSI_PREFIX}[92m\"
    BRIGHT_YELLOW = f\"{ANSI_PREFIX}[93m\"
    BRIGHT_BLUE = f\"{ANSI_PREFIX}[94m\"
    BRIGHT_MAGENTA = f\"{ANSI_PREFIX}[95m\"
    BRIGHT_CYAN = f\"{ANSI_PREFIX}[96m\"
    BRIGHT_WHITE = f\"{ANSI_PREFIX}[97m\"

    # Bright standard colors (background)
    BRIGHT_BLACK_BG = GREY_BG = GRAY_BG = f\"{ANSI_PREFIX}[100m\"
    BRIGHT_RED_BG = f\"{ANSI_PREFIX}[101m\"
    BRIGHT_GREEN_BG = f\"{ANSI_PREFIX}[102m\"
    BRIGHT_YELLOW_BG = f\"{ANSI_PREFIX}[103m\"
    BRIGHT_BLUE_BG = f\"{ANSI_PREFIX}[104m\"
    BRIGHT_MAGENTA_BG = f\"{ANSI_PREFIX}[105m\"
    BRIGHT_CYAN_BG = f\"{ANSI_PREFIX}[106m\"
    BRIGHT_WHITE_BG = f\"{ANSI_PREFIX}[107m\"

"""

# Daniel Fletcher
# Harvard CS50P 2024
# Final Project

# constants.py
# Constants for use across files

# ANSI escape sequence manipulation
ANSI_PREFIX = "\u001b"
RESET = f"{ANSI_PREFIX}[0m"

# Standard colors (foreground)
BLACK = f"{ANSI_PREFIX}[30m"
RED = f"{ANSI_PREFIX}[31m"
GREEN = f"{ANSI_PREFIX}[32m"
YELLOW = f"{ANSI_PREFIX}[33m"
BLUE = f"{ANSI_PREFIX}[34m"
MAGENTA = f"{ANSI_PREFIX}[35m"
CYAN = f"{ANSI_PREFIX}[36m"
WHITE = f"{ANSI_PREFIX}[37m"

# Standard colors (background)
BLACK_BG = f"{ANSI_PREFIX}[40m"
RED_BG = f"{ANSI_PREFIX}[41m"
GREEN_BG = f"{ANSI_PREFIX}[42m"
YELLOW_BG = f"{ANSI_PREFIX}[43m"
BLUE_BG = f"{ANSI_PREFIX}[44m"
MAGENTA_BG = f"{ANSI_PREFIX}[45m"
CYAN_BG = f"{ANSI_PREFIX}[46m"
WHITE_BG = f"{ANSI_PREFIX}[47m"

# Bright standard colors (foreground)
BRIGHT_BLACK = GREY = GRAY = f"{ANSI_PREFIX}[90m"
BRIGHT_RED = f"{ANSI_PREFIX}[91m"
BRIGHT_GREEN = f"{ANSI_PREFIX}[92m"
BRIGHT_YELLOW = f"{ANSI_PREFIX}[93m"
BRIGHT_BLUE = f"{ANSI_PREFIX}[94m"
BRIGHT_MAGENTA = f"{ANSI_PREFIX}[95m"
BRIGHT_CYAN = f"{ANSI_PREFIX}[96m"
BRIGHT_WHITE = f"{ANSI_PREFIX}[97m"

# Bright standard colors (background)
BRIGHT_BLACK_BG = GREY_BG = GRAY_BG = f"{ANSI_PREFIX}[100m"
BRIGHT_RED_BG = f"{ANSI_PREFIX}[101m"
BRIGHT_GREEN_BG = f"{ANSI_PREFIX}[102m"
BRIGHT_YELLOW_BG = f"{ANSI_PREFIX}[103m"
BRIGHT_BLUE_BG = f"{ANSI_PREFIX}[104m"
BRIGHT_MAGENTA_BG = f"{ANSI_PREFIX}[105m"
BRIGHT_CYAN_BG = f"{ANSI_PREFIX}[106m"
BRIGHT_WHITE_BG = f"{ANSI_PREFIX}[107m"

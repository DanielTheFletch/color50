Introduction
============

**This is color50!**

Created as a final project submission for Harvard University's CS50P course,
**color50** is a package I designed to add a little extra flavor to standard
output print statements. This is my first ever attempt at making a Python
package from scratch, and I'm excited to share it with fellow Python developers
and CS50 students.

----------

Motivation
----------

Many programming courses focus on building fundamentals by creating projects at
the command line. As such, I have spent a lot of time working in terminal
environments, engaging in all sorts of academic projects and learning pursuits.
Every time I used a new language at the terminal, though, I always wondered why
printing text in color is almost never covered in the learning process.

It seems simple in theory, right? Many modern shells display all sorts of key
features *with colorful text already*, so I knew it was possible---I just didn't
quite know how to do it in an approachable fashion. This train of thought sparked
the idea of what eventually became **color50**: a Python library designed to make
colorful terminal output more approachable.

Ultimately, **color50** is a package designed to address the confusion and cryptic
syntax that occurs when working with ANSI escape sequences and color codes. The main
motivation was to make printing in color more readable, more intuitive to a broader
range of developers, and generally more convenient to use.

----------

Brief Summary
-------------

Below is a brief summary of the four modules contained in the **color50** package,
with key features highlighted accordingly:

    - :ref:`color module<color-module-label>`: Contains the **Color** class and associated logic.

        - **Color** class

    - :ref:`core_functions module<core-functions-module-label>`: Contains four standalone functions designed to streamline color selection and usage.

        - ``rgb`` function
        - ``hexcode`` function
        - ``css`` function
        - ``colorize`` function (decorator)

    - :ref:`colorstr module<colorstr-module-label>`: Contains the **ColorStr** class and associated logic.

        - **ColorStr** class

    - :ref:`constants module<constants-module-label>`: Contains a series of string literal constants for use with ANSI color code semantics.

----------

Installation
------------

To install the **color50** package, use the following ``pip`` command:
``pip install color50``

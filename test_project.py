# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# test_project.py
# Contains test cases for rgb, hexcode, and css functions


from project import rgb, hexcode, css
from color import Color
from colorstr import ColorStr


def test_rgb():
    color = Color()
    color.red = 255
    assert rgb(255, 0, 0) == color


def test_hexcode():
    ...


def test_css():
    ...
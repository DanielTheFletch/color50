# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# test_project.py
# Contains test cases for rgb, hexcode, and css functions

# Python library imports
from math import pi, sqrt

# color50 imports
from project import rgb, hexcode, css
from color import Color
from colorstr import ColorStr

# pytest for more control over testing
import pytest


def test_rgb():
    # Manually initialize colors for testing
    colors = []
    for _ in range(10): colors.append(Color())
    colors[1].red = 255
    colors[2].red, colors[2].blue = 128, 128
    colors[3].red, colors[3].green, colors[3].blue = 255, 255, 255
    colors[4].red, colors[4].green = 128, 255
    colors[5].green, colors[5].blue = 255, 128
    colors[6].red, colors[6].green, colors[6].blue = 64, 32, 16
    colors[7].red, colors[7].green, colors[7].blue = 16, 32, 64
    colors[8].green = 16
    colors[9].red, colors[9].green, colors[9].blue = 16, 16, 16

    # Test valid colors
    assert rgb(0, 0, 0) == colors[0]
    assert rgb(255, 0, 0) == colors[1]
    assert rgb(128, 0, 128) == colors[2]
    assert rgb(255, 255, 255) == colors[3]
    assert rgb(128, 255, 0) == colors[4]
    assert rgb(0, 255, 128) == colors[5]
    assert rgb(64, 32, 16) == colors[6]
    assert rgb(16, 32, 64) == colors[7]
    assert rgb(0, 16, 0) == colors[8]
    assert rgb(16, 16, 16) == colors[9]

    # Test invalid colors: Values out of range
    with pytest.raises(ValueError):
        rgb(0, 0, -1)
        rgb(100, 200, 300)
        rgb(1000, 30, 50)
        rgb(0, -1000, 1000)
        rgb(256, 255, 254)
        rgb(0, 200, 400)
        rgb(-5, 0, 5)
        rgb(-255, -255, -255)
        rgb(0, 1000, 0)
        rgb(-256, 0, 256)

    # Test invalid colors: Invalid parameter type(s)
    with pytest.raises(TypeError):
        rgb(0, 0.5, 0)
        rgb("128", "0", "128")
        rgb("red=255", 0, 0)
        rgb(Color(), Color(), Color())
        rgb([255, 0, 0], None, None)
        rgb(32, 67.75, 128)
        rgb({"red": 255, "green": 0, "blue": 0}, None, None)
        rgb(sqrt(2), sqrt(2) / 2, sqrt(2))
        rgb(pi, pi / 2, pi / 4)
        rgb([], {}, ())


def test_hexcode():
    ...


def test_css():
    ...
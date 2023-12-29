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
    # Manually initialize colors for testing
    colors = []
    for _ in range(10): colors.append(Color())
    colors[1].red, colors[1].green, colors[1].blue = 255, 255, 255
    colors[2].red, colors[2].blue = 128, 128
    colors[3].red, colors[3].green, colors[3].blue = 128, 64, 64
    colors[4].red, colors[4].green = 128, 255
    colors[5].green, colors[5].blue = 255, 240
    colors[6].red, colors[6].green, colors[6].blue = 225, 200, 175
    colors[7].red, colors[7].green, colors[7].blue = 160, 96, 160
    colors[8].green = 77
    colors[9].red, colors[9].green, colors[9].blue = 100, 100, 100

    # Test valid colors
    assert hexcode("#000000") == colors[0]
    assert hexcode("FFFFFF") == colors[1]
    assert hexcode("#800080") == colors[2]
    assert hexcode("804040") == colors[3]
    assert hexcode("#80ff00") == colors[4]
    assert hexcode("00fff0") == colors[5]
    assert hexcode("#E1C8AF") == colors[6]
    assert hexcode("a060a0") == colors[7]
    assert hexcode("#004d00") == colors[8]
    assert hexcode("646464") == colors[9]

    # Test invalid colors: Invalid hexcode strings (value, formatting)
    with pytest.raises(ValueError):
        hexcode("#00000000")
        hexcode("FFF")
        hexcode("#FFGGHH")
        hexcode("##A0A0FF")
        hexcode("light blue")
        hexcode("#A0F0K0")
        hexcode("0")
        hexcode("#E7")
        hexcode("#E7E6 E5")
        hexcode("3C-4C-9D")

    # Test invalid colors: Invalid parameter type (e.g., not str)
    with pytest.raises(TypeError):
        hexcode(0x000000)
        hexcode(0xFFFFFF)
        hexcode([255, 255, 128])
        hexcode(Color())
        hexcode({"green": 30, "blue": 99})
        hexcode(506.77)
        hexcode(sqrt(3))
        hexcode(1 / pi)
        hexcode(0x10 == 0x10)
        hexcode(0x10 == 0x11)


def test_css():
    # Manually initialize colors for testing
    colors = []
    for _ in range(10): colors.append(Color())
    colors[1].red, colors[1].green, colors[1].blue = 138, 43, 226
    colors[2].green, colors[2].blue = 206, 209
    colors[3].red, colors[3].green, colors[3].blue = 178, 34, 34
    colors[4].red, colors[4].green, colors[4].blue = 32, 178, 170
    colors[5].red, colors[5].green = 255, 165
    colors[6].red = 255
    colors[7].red, colors[7].green, colors[7].blue = 135, 206, 235
    colors[8].red, colors[8].green, colors[8].blue = 216, 191, 216
    colors[9].red, colors[9].green, colors[9].blue = 255, 255, 255

    # Test valid colors
    assert css("black") == colors[0]
    assert css("blueviolet") == colors[1]
    assert css("darkturquoise") == colors[2]
    assert css("firebrick") == colors[3]
    assert css("lightseagreen") == colors[4]
    assert css("orange") == colors[5]
    assert css("red") == colors[6]
    assert css("skyblue") == colors[7]
    assert css("thistle") == colors[8]
    assert css("white") == colors[9]

    # Test invalid colors: Invalid CSS color name
    with pytest.raises(ValueError):
        css("rubberducky")
        css("malanshirtblack")
        css("sharknadoblue")
        css("Hello, World!")
        css("When in the course of human events...")
        css("#000000")
        css("FFFFFF")
        css("color: blue;")
        css("background-color: red;")
        css("LIME GREEN!!!!!!")

    # Test invalid colors: Invalid parameter type (e.g., not str)
    with pytest.raises(TypeError):
        css(0)
        css(sqrt(2) + sqrt(2) / 3)
        css({"color": "cyan"})
        css(Color())
        css([128, 0, 128])
        css(())
        css(pi == pi)
        css(pi == (pi / 64))
        css(1.618)
        css(0x808000)

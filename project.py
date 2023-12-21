# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# project.py
# Contains main function for project


import color


def main():
    my_color = color.rgb(255, 0, 0)
    print(str(my_color) + "Red statement" + color.RESET, sep="")
    my_color = color.rgb(0, 255, 0)
    print(str(my_color) + "Green statement" + color.RESET, sep="")
    my_color = color.rgb(0, 0, 255)
    print(str(my_color) + "Blue statement" + color.RESET, sep="")
    my_color = color.rgb(255, 0, 255)
    print(str(my_color) + "Purple statement" + color.RESET, sep="")
    my_color = color.rgb(127, 127, 64)
    print(str(my_color) + "Blended statement" + color.RESET, sep="")


if __name__ == "__main__":
    main()
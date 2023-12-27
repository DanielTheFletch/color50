# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# project.py
# Contains main function for project


import color


def main():
    color1 = color.rgb(255, 0, 0)
    color2 = color.rgb(0, 0, 255)
    print(color2.bg() + color1.fg() + "Red message with a blue background" + color.RESET)

if __name__ == "__main__":
    main()

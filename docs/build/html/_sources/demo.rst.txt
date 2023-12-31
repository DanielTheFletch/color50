Demo Files
==========

``demo1.py``::

    from color50 import Color, constants
    import sys

    # Prompt for user input
    input_red = input("Enter an integer (0-255) for the color's RED value: ")
    input_green = input("Enter an integer (0-255) for the color's GREEN value: ")
    input_blue = input("Enter an integer (0-255) for the color's BLUE value: ")

    # Validate input type
    try:
        input_red = int(input_red)
        input_green = int(input_green)
        input_blue = int(input_blue)
    except ValueError:
        sys.exit("Error: Invalid color selection")

    # Validate input value
    my_color = Color()
    try:
        my_color.red = input_red
        my_color.green = input_green
        my_color.blue = input_blue
    except ValueError:
        sys.exit("Error: Invalid color selection")

    # Print message in user-specified color
    print(my_color + "Hello, World!" + constants.RESET)

----------

``demo2.py``::

    from color50 import constants, css, hexcode
    import sys

    # Prompt and validate hex code input
    input_hex = input("HEX color code: ")
    try:
        color1 = hexcode(input_hex)
    except (ValueError, TypeError):
        sys.exit("Error: Invalid HEX color code")

    # Prompt and validate CSS color input
    input_css = input("CSS color name: ")
    try:
        color2 = css(input_css)
    except (ValueError, TypeError):
        sys.exit("Error: CSS color name not recognized")

    # Echo inputs back to user, except in color
    print(f"HEX color code: {color1}{input_hex}{constants.RESET}")
    print(f"CSS color name: {color2}{input_css}{constants.RESET}")

----------

``demo3.py``::

    from color50 import ColorStr, rgb
    import random

    # Randomly select foreground color
    rand_red = random.randint(0, 255)
    rand_green = random.randint(0, 255)
    rand_blue = random.randint(0, 255)
    fg_color = rgb(rand_red, rand_green, rand_blue)

    # Randomly select background color
    rand_red = random.randint(0, 255)
    rand_green = random.randint(0, 255)
    rand_blue = random.randint(0, 255)
    bg_color = rgb(rand_red, rand_green, rand_blue)

    # Create and print ColorStr object between other strings
    my_color_str = ColorStr("What a randomly colorful string!", fg_color, bg_color)
    print("===>", my_color_str, "<===")

----------

``demo4.py``::

    from color50 import constants, css, colorize
    import random

    def main():
        # Greet user
        print(f"Welcome to {css("crimson")}DICE ROLLER!{constants.RESET}\n")
        print("You will roll 2 six-sided dice.")
        print("Your opponents, Beep and Boop, will each roll 3 four-sided dice.")
        print("Whoever has the highest sum at the end wins.")
        print(f"Try to get first place for the {css("gold")}gold medal!{constants.RESET}")

        # Track random die rolls
        die_rolls_user = []
        die_rolls_beep = []
        die_rolls_boop = []

        # Prompt user to enter name
        username = input("\nFirst, please enter your name: ")
        print(f"Nice to meet you, {username}! Best of luck.")

        # Simulate first die roll
        _ = input("\nPress [ENTER] to roll your first die. ")
        die_rolls_user.append(random.randint(1, 6))
        print_dice_roll("First dice roll", die_rolls_user[0])

        # Simulate second die roll
        _ = input("\nPress [ENTER] to roll your second die. ")
        die_rolls_user.append(random.randint(1, 6))
        print_dice_roll("Second dice roll", die_rolls_user[1])

        # Simulate Beep's rolls
        _ = input("\nPress [ENTER] to see Beep's rolls. ")
        for _ in range(3):
            die_rolls_beep.append(random.randint(1, 4))
        print_dice_roll("Beep's first dice roll", die_rolls_beep[0])
        print_dice_roll("Beep's second dice roll", die_rolls_beep[1])
        print_dice_roll("Beep's third dice roll", die_rolls_beep[2])

        # Simulate Boop's rolls
        _ = input("\nPress [ENTER] to see Boop's rolls. ")
        for _ in range(3):
            die_rolls_boop.append(random.randint(1, 4))
        print_dice_roll("Boop's first dice roll", die_rolls_boop[0])
        print_dice_roll("Boop's second dice roll", die_rolls_boop[1])
        print_dice_roll("Boop's third dice roll", die_rolls_boop[2])

        # Calculate final results
        _ = input("\nPress [ENTER] to see the final results! ")
        results = [
            { username: sum(die_rolls_user) },
            { "Beep": sum(die_rolls_beep) },
            { "Boop": sum(die_rolls_boop) }
        ]
        results = sorted(results, key=lambda index : list(index.values())[0])

        # Print messages for end-of-game rankings
        third_place_message(f"In third, it's {list(results[0].keys())[0]} with {list(results[0].values())[0]} points.")
        second_place_message(f"In second, it's {list(results[1].keys())[0]} with {list(results[1].values())[0]} points.")
        first_place_message(f"In first, it's {list(results[2].keys())[0]} with {list(results[2].values())[0]} points.")
        print(f"\nCongratulations to {list(results[2].keys())[0]} for winning the game!")


    def print_dice_roll(text: str, value: int):
        print(f"{text} ==> {css("slateblue").bg()}[ {value} ]{constants.RESET}")


    @colorize(css("gold"))
    def first_place_message(msg: str):
        print(msg)


    @colorize(css("silver"))
    def second_place_message(msg: str):
        print(msg)


    @colorize(css("brown"))
    def third_place_message(msg: str):
        print(msg)


    if __name__ == "__main__":
        main()

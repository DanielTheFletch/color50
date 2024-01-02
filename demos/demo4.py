# Daniel Fletcher
# Harvard CS50P 2024
# Final Project

# demo4.py
# Demonstration of package functionality (4 of 4)

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

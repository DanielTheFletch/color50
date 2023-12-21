# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# project.py
# Contains main function for project


ANSI = "\u001b"


def main():
    print(f"{ANSI}[38;2;40;47;249mThe quick brown fox jumped over the lazy dog.{ANSI}{"[0m"}\n")


if __name__ == "__main__":
    main()
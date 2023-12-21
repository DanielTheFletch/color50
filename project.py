# Daniel Fletcher
# Harvard CS50x 2023
# Final Project

# project.py
# Contains main function for project


ANSI = "\u001b"


def main():
    # Test 256 colors
    for i in range(256):
        print(f"{ANSI}[38;5;{i}m[{i}]: The quick brown fox jumped over the lazy dog.{ANSI}{"[0m"}\n")


if __name__ == "__main__":
    main()
"""Finds the amount of times the letter occurs in the word."""

def main():
    """Runs the program."""
    counter = 0
    char = input().split

    str_end = "".join(char[2:])
    str_a = char[0]

    if str_a in str_end:
        counter += 1
    print(counter)


if __name__ == "__main__":
    main()

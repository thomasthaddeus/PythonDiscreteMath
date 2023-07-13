"""
Print lists of colors and numbers

This file prints the index location and element from lists
"""

def main():
    colors = ['black', 'green', 'blue', 'red']
    numbers = [-2, -7, 7, 0, 3]

    print_colors(colors)
    print_numbers(numbers)


def print_colors(colors):
    """
    Prints the position and color from a list of colors.

    Args:
        colors (list): A list of colors.

    Returns:
        None
    """
    for position, color in enumerate(colors):
        print(position, color)


def print_numbers(numbers):
    """
    Prints the index and number from a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        None
    """
    for position, number in enumerate(numbers):
        if number < 0:
            print(position, 'x')
        else:
            print(position, number)


if __name__=='__main__':
    main()

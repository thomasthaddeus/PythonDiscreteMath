"""13.11 LAB: Multiples of ten in a list.

Write a program that reads a list of integers,
and outputs whether the list contains:
all multiples of 10,
no multiples of 10,
or mixed values.
"""


def is_list_mult10(list_in):
    """Define a function named is_list_mult10 that takes a list as a parameter,
    and returns a boolean that represents
    whether the list contains all multiples of ten."""
    for i in list_in:
        if i % 10 != 0:
            return False
    return True


def is_list_no_mult10(list_in):
    """Define a function named is_list_no_mult10
    that takes a list as a parameter
    and returns a boolean that represents
    whether the list contains no multiples of ten."""
    for i in list_in:
        if i % 10 == 0:
            return False
    return True


def main():
    """Write a main program that takes an integer,
    representing the size of the list, followed by the list values.
    The first integer is not in the list."""
    list_input = []
    list_range = int(input())
    for n in range(list_range):
        list_input.append(int(input()))

    if is_list_mult10(list_input) is True:
        print('all multiples of 10')
    elif is_list_no_mult10(list_input) is True:
        print('no multiples of 10')
    else:
        print('mixed values')


if __name__ == '__main__':
    main()

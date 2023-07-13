""" 13.11 LAB: Multiples of ten in a list.

Define a function named is_list_mult10 that takes a list as a parameter, and returns a boolean that represents whether the list contains all multiples of ten.
Define a function named is_list_no_mult10 that takes a list as a parameter and returns a boolean that represents whether the list contains no multiples of ten.
Then, write a main program that takes an integer, representing the size of the list, followed by the list values.
The first integer is not in the list.
"""

# Write a program that reads a list of integers,
# and outputs whether the list contains
# all multiples of 10, no multiples of 10, or mixed values.
list10 = [int(5), int(10), int(20), int(40), int(60), int(80)]

def is_list_mult10(list10):
    """returns a boolean that represents whether the list contains all multiples of ten"""
    mult10 = []
    for i in range(list10[1:]):
        if i == 5:
            continue
        elif i % 10 == 0:
            mult10.append(True)
        else:
            return False
    return True


def is_list_no_mult10(list10):
    """is_list_no_mult10"""
    mult10_not = []
    for i in range(int(list10[1:])):
        if i % 10 == 0:
            return False
        elif i % 10 != 0:
            continue
        else:
            mult10_not.append(True)
    return True


def main(list10):
    """Takes an integer, representing the size of the list, followed by the list values"""
    list10 = list10[1:]
    if is_list_mult10(list10) is True:
        print("All multiples of 10")
    elif is_list_no_mult10(list10) is True:
        print("No multiples of 10")
    else:
        print("Mixed values")

# [print(i) for i in list]

if __name__ == main(list10):
    main(list10)

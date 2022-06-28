"""Main.py 13.3 LAB: Max magnitude


# Use the function in the main program that takes
#   three integer inputs and outputs the largest magnitude value.

# Note: The function does not just return the largest value,
#   which for -17 -8 -2 would be -2.
# Though not necessary,
# you may use the built-in absolute value function
#   to determine the max magnitude,
# but you must still output the input number (Ex: Output -17, not 17).

# Your program must define and call the following function:
# def max_magnitude(user_val1, user_val2, user_val3)
"""


def main():
    """main _summary_"""
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    print(max_magnitude(user_val1, user_val2, user_val3))


def max_magnitude(user_val1, user_val2, user_val3):
    """Write a function max_magnitude() with three integer parameters
        that returns the largest magnitude value."""
    lst = [user_val1, user_val2, user_val3]
    lst.sort()
    if abs(lst[0]) > abs(lst[2]):
        return lst[0]
    else:
        return lst[2]


if __name__ == '__main__':
    main()

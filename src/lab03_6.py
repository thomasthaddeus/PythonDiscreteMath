"""lab activity 13.9 LAB: Swapping variables. -MAIN.py

Define a function named swap_values that takes four integers as parameters
and swaps the first with the second, and the third with the fourth values.
Then write a main program that reads four integers from input,
calls function swap_values() to swap the values,
and prints the swapped values on a single line separated with spaces.
"""

# The program must define and call the following function.
# def swap_values(user_val1, user_val2, user_val3, user_val4)

def swap_values(x1, x2, x3, x4):
    """Swaps two integers."""
    temp1, temp2 = x1, x3
    x1, x3 = x2, x4
    x2, x4 = temp1, temp2
    print(f"{x1} {x2} {x3} {x4}")
    return x1, x2, x3, x4


def main():
    """main _summary_"""
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())
    swap_values(val1, val2, val3, val4)


if __name__ == '__main__':
    main()

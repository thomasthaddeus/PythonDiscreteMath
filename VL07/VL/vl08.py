"""40.8.1: LAB: Number pattern.
Write a recursive function called print_num_pattern() to output the following number pattern.

Given a positive integer as input (Ex: 12),
subtract another positive integer (Ex: 3) continually until 0 or a negative value is reached,
and then continually add the second integer until the first integer is again reached.
For this lab, do not end output with a newline.
"""
def print_num_pattern(my_var1, my_var2):
    """Print the number pattern."""
    if my_var1 > 0:
        print(my_var1, end = ' ')
        print_num_pattern(my_var1 - my_var2, my_var2)
        print(my_var1, end = ' ')

    elif my_var1 <= 0:
        print(my_var1, end = ' ')
        return

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)

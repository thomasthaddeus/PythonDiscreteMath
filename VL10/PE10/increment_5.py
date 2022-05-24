"""22.4.1: LAB: Output range with increment of 5"""
# Write a program whose input is two integers.
# Output the first integer and subsequent increments of 5
#     as long as the value is less than or equal to the second integer.

# Ex: If the input is:
# -15
# 10

# the output is:
# -15 -10 -5 0 5 10

# Ex: If the second integer is less than the first as in:
# 20
# 5

# the output is:
# Second integer can't be less than the first.
# For coding simplicity, output a space after every integer, including the last.

def main():
    """Main function."""
    num_1 = int(input())  # -15
    num_2 = int(input())  # 10
    increment_5(num_1, num_2)

def increment_5(num1, num2):
    """Prints the range in increments of 5"""
    if num1 > num2:
        print("Second integer can't be less than the first.")
    else:
        while num1 <= num2:
            print(num1, end=' ')
            num1 += 5
        print()

if __name__ == '__main__':
    main()

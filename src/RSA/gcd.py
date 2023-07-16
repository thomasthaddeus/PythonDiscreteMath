"""Determine the greatest common divisor of two numbers, e.g., GCD(8, 12) = 4
"""
# Reference  NOTE:
# https://learn.zybooks.com/zybook/City_University_of_Seattle_-_CS351Spring2022/chapter/40/section/5

def main():
    """This program outputs the greatest common divisor of two numbers."""
    print ('\n\nThis program outputs the greatest '
        'common divisor of two numbers.\n')

    num1 = int(input('Enter first number:       '))
    num2 = int(input('Enter second number:      '))

    if (num1 < 1) or (num2 < 1):
        print('Note: Neither value can be below 1.')
    else:
        my_gcd = gcd(num1, num2)
        print('Greatest common divisor =', my_gcd)
        print('\n\n')


def gcd(num_1, num_2):
    """Return the greatest common divisor"""
    if num_1 % num_2 == 0:  # n2 is a common factor
        return num_2
    else:
        return gcd(num_2,num_1%num_2)


if __name__ == '__main__':
    main()

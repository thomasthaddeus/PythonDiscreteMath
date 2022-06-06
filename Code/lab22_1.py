"""22.1.1: LAB: Convert to reverse binary."""

# <body>Write a program that takes in a positive integer as input,<br>
#    and outputs a string of 1's and 0's<br>
#    representing the integer in reverse binary.</body>

# For an integer x, the algorithm is:

# As long as x is greater than 0<br>
#    Output x modulo 2 (remainder is either 0 or 1)<br>
#    Assign x with x divided by 2

# __Note:__ The above algorithm outputs the 0's and 1's in reverse order.

# Ex: If the input is:
# 6
# the output is:
# 011

# 6 in binary is 110; the algorithm outputs the bits in reverse.


def reverse(num):
    """Converts the input integer to binary and reverses it.""" #int(input())
    output = str('')
    while num > 0:
        modulus = num % 2
        output += str(modulus)
        num //= 2
    return str(output)


print(reverse(input()))

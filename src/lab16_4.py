"""16.4.1: LAB: Seasons.

1. Write a program that takes a date as input and
    outputs the date's season in the northern hemisphere.
2. The input is a string to represent the month
    and an int to represent the day.
EX: If the input is: April 11
    the output is: Spring
NOTE: In addition, check if the string and int are valid
(an actual month and day).
# Ex: If the input is: Blue 65
the output is: Invalid
"""
# NOTE: The dates for each season in the northern hemisphere are: </br>
# - Spring: March 20 - June 20
# - Summer: June 21 - September 21
# - Autumn: September 22 - December 20
# - Winter: December 21 - March 19


input_month = input()
input_day = int(input())

if input_day > 31 or input_day < 1:
    print("Invalid")

if input_month == 'January':
    if input_day > 0 and input_day < 32:
        print('Winter')
elif input_month == 'February':
    if input_day > 0 and input_day < 30:
        print('Winter')
elif input_month == "March":
    if input_day > 0 and input_day < 20:
        print('Winter')
    elif input_day >= 20 and input_day < 32:
        print('Spring')
elif input_month == 'April':
    if input_day > 0 and input_day < 31:
        print('Spring')
elif input_month == 'May':
    if input_day > 0 and input_day < 32:
        print('Spring')
elif input_month == "June":
    if input_day < 21 and input_day > 0:
        print('Spring')
    elif input_day >= 20 and input_day < 32:
        print('Summer')
elif input_month == "July":
    if input_day > 0 and input_day < 31:
        print('Summer')
elif input_month == "August":
    if input_day > 0 and input_day < 31:
        print('Summer')
elif input_month == "September":
    if input_day < 22 and input_day > 0:
        print('Summer')
    elif input_day >= 22 and input_day <= 30:
        print('Autumn')
    else:
        print('Invalid')
elif input_month == "October":
    if input_day > 0 and input_day < 32:
        print('Autumn')
elif input_month == "November":
    if input_day > 0 and input_day < 31:
        print('Autumn')
elif input_month == "December":
    if input_day < 21 and input_day > 0:
        print('Autumn')
    elif input_day >= 21 and input_day < 31:
        print('Winter')
else:
    print("Invalid")

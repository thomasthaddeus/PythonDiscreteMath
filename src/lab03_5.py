""" 13.7 LAB: Leap year - functions.

A common year in the modern Gregorian Calendar consists of 365 days.
In reality, Earth takes longer to rotate around the sun.
To account for the difference in time, every 4 years, a leap year takes place.
A leap year is when a year has 366 days: An extra day, February 29th.
The requirements for a given year to be a leap year are:
1) The year must be divisible by 4
2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400
- Some example leap years are 1600, 1712, and 2016.
----
1. Write a program that takes in a year and determines the number of days in February for that year.
### Ex: If the input is
1712
- the output is:
1712 has 29 days in February.
- Ex: If the input is:
> 1913
the output is:
> 1913 has 28 days in February.
Your program must define and call the following function. </br>
The function should return the number of days in February for the input year.
"""


def main():
    """Runs the program."""
    days_in_feb(int(input()))


def days_in_feb(user_year):
    """Return the number of days in February."""
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        print(f"{user_year} has 29 days in February.")
        return 29
    else:
        print(f"{user_year} has 28 days in February.")
        return 28


if __name__ == '__main__':
    main()

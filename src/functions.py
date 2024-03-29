"""11.4.1: Functions: Factoring out a unit-conversion calculation.

Write a function so that the main program below can be replaced
by the simpler code that calls function mph_and_minutes_to_miles()."""
# Original main program:

# miles_per_hour = float(input())
# minutes_traveled = float(input())
# hours_traveled = minutes_traveled / 60.0
# miles_traveled = hours_traveled * miles_per_hour

# print(f'Miles: {miles_traveled:f}')

# Sample output with inputs: 70.0 100.0
# Miles: 116.666667

MPH = 70.0
MIN_TR = 100.0

def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
    """Miles per hour and minutes to miles."""
    miles_per_hour = float(MPH)
    minutes_traveled = float(MIN_TR)
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled


print(f'Miles: {mph_and_minutes_to_miles(MPH, MIN_TR):.9}')

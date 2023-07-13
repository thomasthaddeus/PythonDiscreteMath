"""half_life.py

Caffeine Levels

This program calculates and outputs the caffeine levels after 6, 12, and 24
hours based on the input caffeine amount (in mg). The half-life of caffeine is
approximately 6 hours in humans.

Input:
    The initial caffeine amount (in mg) is taken as input.

Formatted Output:
    The program uses string formatting with conversion specifiers to output the
    caffeine levels as floating-point numbers. Each value is displayed with two
    digits after the decimal point.

Example:
    Input: 100
    Output:
    After 6 hours: 50.00 mg
    After 12 hours: 25.00 mg
    After 24 hours: 6.25 mg

Note:
    - A cup of coffee has about 100 mg of caffeine.
    - A soda has about 40 mg of caffeine.
    - An "energy" drink typically contains between 100 mg and 200 mg of caffeine.
"""

caffeine_mg = float(input())
half_life = caffeine_mg / 2
after_12 = half_life / 2
after_24 = after_12 / 4

print(
    f"After 6 hours: {half_life:.2f} mg\n"
    f"After 12 hours: {after_12:.2f} mg\n"
    f"After 24 hours: {after_24:.2f} mg"
)

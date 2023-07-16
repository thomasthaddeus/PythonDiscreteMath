"""Lab activity.

7.7.1: LAB*: Program: Cooking measurement converter.
"""


def gallon(i):
    """Convert from cups to gallons."""
    return i / 16


# STEP(1): Prompt the user for the number of cups needed to make lemonade.
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n\n'))

print(f"Lemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_cups:.2f} cup(s) agave nectar\n")

# (2) Prompt the user to specify the desired number of servings.
# Adjust the amounts of each ingredient accordingly,
# and then output the ingredients and serving size.
# (Submit for 4 points, so 6 points total).
servings_new = float(input('How many servings would you like to make?\n\n'))
ratio = (servings_new / servings)
water_cups = ratio * water_cups
agave_cups = ratio * agave_cups
lemon_juice_cups = ratio * lemon_juice_cups

print((f"Lemonade ingredients - yields {servings_new:.2f} servings"))
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_cups:.2f} cup(s) agave nectar\n")

# (3): Convert and output the ingredients from (2) to gallons
print(f"Lemonade ingredients - yields {servings_new:.2f} servings")
print(f"{gallon(lemon_juice_cups):.2f} gallon(s) lemon juice")
print(f"{gallon(water_cups):.2f} gallon(s) water")
print(f"{gallon(agave_cups):.2f} gallon(s) agave nectar")

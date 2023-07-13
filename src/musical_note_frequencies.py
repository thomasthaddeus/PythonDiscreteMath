"""7.5 LAB: Musical note frequencies."""
import math

# On a piano, a key has a frequency, say f0.
# Each higher key(black or white) has a frequency of f0 * rn,
# where n is the distance(number of keys) from that key, and r is 2(1/12).
# Given an initial key frequency, output that frequency
# and the next 4 higher key frequencies.
# Output each floating-point value with two digits after the decimal point,
# which can be achieved as follows:
# print(f'{your_value1:.2f} {your_value2:.2f}
#   {your_value3:.2f} {your_value4:.2f} {your_value5:.2f}')
# Ex: If the input is:
# 440
# (which is the A key near the middle of a piano keyboard), the output is:
# 440.00 466.16 493.88 523.25 554.37
# Note: Use one statement to compute r = 2(1/12)
# using the pow function(remember to import the math module).
# Then use that r in subsequent statements that use the formula
# frequency = f0 * rn with n being 1, 2, 3, and finally 4
ALPHA_KEY = float(input("Frequency: "))


def frequency(freq, numkeys):
    """Return musical frequency."""
    freq = ALPHA_KEY
    r = math.pow(2, 1 / 12)
    key_m = freq * pow(r, numkeys)
    return key_m


f0 = float(frequency(ALPHA_KEY, 0))
f1 = float(frequency(f0, 1))
f2 = float(frequency(f0, 2))
f3 = float(frequency(f0, 3))
f4 = float(frequency(f0, 4))

print(f'{f0:.2f} {f1:.2f} {f2:.2f} {f3:.2f} {f4:.2f}')

""" hourly_temperature.py

Write a loop to print all elements in hourly_temperature. Separate elements
with a -> surrounded by spaces.

Sample output for the given program with input: '90 92 94 95'
90 -> 92 -> 94 -> 95
Note: 95 is followed by a space, then a newline.

Print Hourly Temperature

This program takes a string of space-separated hourly temperature values as
input and prints them in a specific format.
The temperatures are separated by "->" with spaces around it.

Example:
    Input: '90 92 94 95'
    Output: 90 -> 92 -> 94 -> 95

"""

hourly_temperature = input().split()

for i, temperature in enumerate(hourly_temperature):
    print(temperature, end="")
    if i != len(hourly_temperature) - 1:
        print(" -> ", end="")

print()

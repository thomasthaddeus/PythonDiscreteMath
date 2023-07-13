""" 24.3.3: Hourly temperature reporting.

Write a loop to print all elements in hourly_temperature.
Separate elements with a -> surrounded by spaces.
Sample output for the given program with input: '90 92 94 95'
90 -> 92 -> 94 -> 95
Note: 95 is followed by a space, then a newline.
 """

user_input = input()
hourly_temperature = user_input.split()
space = "-> "
for i in range(len(hourly_temperature)):
    if i != (len(hourly_temperature) - 1):
        print(hourly_temperature[i], space, end="")
    else:
        print(f"{hourly_temperature[i]} ")

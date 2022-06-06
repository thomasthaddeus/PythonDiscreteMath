''' 24.3.3: Hourly temperature reporting.

Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces.

Sample output for the given program with input: '90 92 94 95'
90 -> 92 -> 94 -> 95 
Note: 95 is followed by a space, then a newline.
 '''
user_input = input()
hourly_temperature = user_input.split()
hr_temp = []
for i in hourly_temperature[0:-1]:
    
print(hr_temp)

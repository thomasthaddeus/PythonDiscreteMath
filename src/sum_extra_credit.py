"""24.3.2: Sum extra credit.

Assign sum_extra with the total extra credit received given list test_grades.
Iterate through the list with           for grade in test_grades:.
The code uses the Python split() method to split a string at each space
    into a list of string values
    and the map() function to convert each string value to an integer.
    Full credit is 100, so anything over 100 is extra credit.

Sample output for the given program with input: '101 83 107 90'
Sum extra: 8
(because 1 + 0 + 7 + 0 is 8)"""

user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


sum_extra = 0 # Initialize 0 before your loop
for grade in test_grades:
    if grade > 100:
        sum_extra += (grade - 100)
    else:
        sum_extra += 0

print('Sum extra:', sum_extra)

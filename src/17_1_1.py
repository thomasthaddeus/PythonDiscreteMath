"""17.1.1: Change order of elements in function list argument.

Write a function swap that swaps the first and last elements of a list argument.
Sample output with input: 'all,good,things,must,end,here'
['here', 'good', 'things', 'must', 'end', 'all']
"""

''' Your solution goes here '''

values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)

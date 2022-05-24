"""31.10 LAB: Descending selection sort with output during execution"""

# The program should use nested loops and
#     output the list after each iteration of the outer loop,
#     thus outputting the list N-1 times (where N is the size of the list).
# ###################
# Ex: If the input is:
# 20 10 30 40
# the output is:
# [40, 10, 30, 20]
# [40, 30, 10, 20]
# [40, 30, 20, 10]
# ####################
# Ex: If the input is:
# 7 8 3
# the output is:
# [8, 7, 3]
# [8, 7, 3]
# ####################
# NOTE: Use print(numbers) to output the list numbers and achieve the format shown in the example.

num_list = [int(num) for num in input().split(' ')]

def selection_dwn(num_list):
    """Takes an integer list as input and
    sorts the list into descending order using selection sort."""
    # loop through the list
    for i in range(len(num_list) - 1):
        num_high = i
        # loop for high number
        for j in range(i + 1, len(num_list)):
            if num_list[num_high] < num_list[j]:
                num_high = j
        # swap places
        num_list[i], num_list[num_high] = num_list[num_high], num_list[i]
        print(num_list)

selection_dwn(num_list)

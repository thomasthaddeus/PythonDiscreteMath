def merge(numbers, i, j, k):
    """
    merge _summary_

    Args:
        numbers (_type_): _description_
        i (_type_): _description_
        j (_type_): _description_
        k (_type_): _description_
    """
    merged_size = k - i + 1  # Size of merged partition
    merged_numbers = []  # Temporary list for merged numbers
    for _ in range(merged_size):
        merged_numbers.append(0)

    merge_pos = 0  # Position to insert merged number

    left_pos = i  # Initialize left partition position
    right_pos = j + 1  # Initialize right partition position

    #  Add smallest element from left or right partition to merged numbers
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] < numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    #  If left partition is not empty, add remaining elements to merged numbers
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    #  If right partition is not empty, add remaining elements to merged numbers
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    #  Copy merge number back to numbers
    merge_pos = 0
    while merge_pos < merged_size:
        numbers[i + merge_pos] = merged_numbers[merge_pos]
        merge_pos = merge_pos + 1


def merge_sort(numbers, i, k):
    """Merge then sort"""
    j = 0
    if i < k:
        j = (i + k) // 2  # Find the midpoint in the partition

        #  Recursively sort left and right partitions
        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)

        #  Merge left and right partition in sorted order
        merge(numbers, i, j, k)


num_list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', end=' ')
for _ in num_list:
    print(str(_), end=' ')
print()

#  initial call to merge_sort with index
merge_sort(num_list, 0, len(num_list) - 1)
print('SORTED:', end=' ')
for _ in num_list:
    print(str(_), end=' ')
print()

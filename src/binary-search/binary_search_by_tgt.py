'''binary_search_algorithm.py

Function to determine if a 'target' exists in the sorted list 'nums' or not
using a binary search algorithm
'''

def binary_search(nums, target):
    """Binary search algorithm."""
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)

    # loop till the search space is exhausted
    while left <= right:

        # find the mid-value in the search space and
        # compares it with the target

        mid = (left + right) // 2

        # overflow can happen. Use:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2

        # target is found
        if target == nums[mid]:
            return mid

        # discard all elements in the right search space,
        # including the middle element
        elif target < nums[mid]:
            right = mid - 1

        # discard all elements in the left search space,
        # including the middle element
        else:
            left = mid + 1

    # 'target' doesn't exist in the list
    return -1

if __name__ == '__main__':

    lst = [2, 5, 8, 10, 13, 19, 21, 32, 37, 52]
    NUM = 13

    index = binary_search(lst, NUM)

    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')

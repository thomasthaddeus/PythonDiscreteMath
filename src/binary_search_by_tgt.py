"""binary_search_by_tgt.py
Function to determine if a 'target' exists in the sorted list 'nums'
or not using a binary search algorithm
"""
def binary_search(nums, target):
    """Binary search algorithm to determine if 'target' exists in the sorted list 'nums' or not.

    Args:
        nums (list): The sorted list of numbers.
        target (int): The target number to search for.

    Returns:
        int: The index of the target if found, or -1 if not found.
    """

    # Define the search space as nums[left…right]
    left, right = 0, len(nums) - 1

    # Loop until the search space is exhausted
    while left <= right:

        # Find the mid-value in the search space and compare it with the target
        mid = (left + right) // 2

        # Overflow prevention:
        # mid = left + (right - left) // 2
        # mid = right - (right - left) // 2

        # Target is found
        if target == nums[mid]:
            return mid

        # Discard all elements in the right search space, including the middle element
        elif target < nums[mid]:
            right = mid - 1

        # Discard all elements in the left search space, including the middle element
        else:
            left = mid + 1

    # Target doesn't exist in the list
    return -1


if __name__ == '__main__':
    lst = [2, 5, 8, 10, 13, 19, 21, 32, 37, 52]
    target = 13

    index = binary_search(lst, target)

    if index != -1:
        print('Element found at index', index)
    else:
        print('Element not found in the list')

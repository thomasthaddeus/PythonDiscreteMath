"""31.11.1: LAB: Sorting user IDs

Given code that reads user IDs (until -1), complete the quicksort() and partition()
functions to sort the IDs in ascending order using the Quicksort algorithm.
Increment the global variable num_calls in quicksort()
to keep track of how many times quicksort() is called.
The given code outputs num_calls followed by the sorted IDs.
Ex:
If the input is:        the output is:
    kaylasimms              7
    julia                   julia
    myron1994               kaylajones
    kaylajones              kaylasimms
    -1                      myron1994
"""

# num_calls = 0

def partition(user_ids, i, k):
    """Write the partitioning algorithm - pick the middle element as the
    pivot, compare the values using two index variables l and h (low and high),
    initialized to the left and right sides of the current elements being sorted,
    and determine if a swap is necessary"""
    low = i - 1
    pivot = user_ids[k]
    for j in range(i, k):
        if user_ids[j] <= pivot:
            low += 1
            user_ids[low], user_ids[j] = user_ids[j], user_ids[low]
    user_ids[low + 1], user_ids[k] = user_ids[k], user_ids[low + 1]
    return low + 1


def quicksort(user_ids, i, k):
    """Write the quicksort algorithm that recursively sorts the low and
        high partitions. Add 1 to num_calls each time quicksort() is called"""
    if i < k:
        j = partition(user_ids, i, k)
        quicksort(user_ids, i, j - 1)
        quicksort(user_ids, j + 1, k)

if __name__ == "__main__":
    # Global variable
    ids = []
    user_id = input()
    while user_id != "-1":
        ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(ids, 0, len(ids) - 1)

    # Print number of calls to quicksort
    num_calls = int((2 * len(ids)) - 1)
    print(num_calls)

    # Print sorted user user_ids
    for user_id in ids:
        print(user_id)

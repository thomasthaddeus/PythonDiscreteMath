"""binary_search.py

_summary_

_extended_summary_
"""

def binary_search(mylist, item):
    """
    binarySearch _summary_

    _extended_summary_

    Args:
        alist (_type_): _description_
        item (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(mylist) == 0:
        return False
    else:
        midpoint = len(mylist)//2
        if mylist[midpoint]==item:
            return True
        else:
            if item<mylist[midpoint]:
                return binary_search(mylist[:midpoint],item)
            else:
                return binary_search(mylist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(binary_search(testlist, 3))
print(binary_search(testlist, 13))

"""Type your code here."""


def mini(x, y, z):
    """Return the minimum of 3 numbers."""
    mylist = []
    x = int(input())
    y = int(input())
    z = int(input())

    mylist.append(x)
    mylist.append(y)
    mylist.append(z)
    return min(mylist)


print(mini(10, 17, 21))

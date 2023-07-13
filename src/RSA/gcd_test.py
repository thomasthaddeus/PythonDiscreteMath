"""RSA key pool python"""

import random

def main():
    """
    main _summary_

    _extended_summary_
    """
    print(gcd(num1, num2))


def gcd(x, y):
    """returns the greatest common distribution"""
    larger = max(x, y)
    smaller = min(x, y)

    remainder = larger % smaller

    if remainder == 0:
        return smaller

    if remainder != 0:
        return gcd(smaller, remainder)


def num1():
    """
    num1 _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    return random.randint(1, 2**32) + 1


def num2():
    """
    num2 _summary_

    _extended_summary_
    """
    return random.randint(1, 2**32) - 1

if __name__ == "__main__":
    main()

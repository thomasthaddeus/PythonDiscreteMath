"""RSA key pool python"""

def gcd(x, y):
    """returns the greatest common ditribution"""
    larger = max(x, y)
    smaller = min(x, y)

    remainder = larger % smaller

    if remainder == 0:
        return smaller

    if remainder != 0:
        return gcd(smaller, remainder)


def num1():
    """returns a random number for encryption"""


print(gcd(num1, num2))

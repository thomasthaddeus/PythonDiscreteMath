"""13.1.1: Lab training: Unit tests to evaluate your program."""


def main():
    """Converts from the metric to standard."""
    kilos = float(input())
    pounds = kilo_to_pounds(kilos)
    print(pounds, "lbs")


def kilo_to_pounds(kilos):
    """This statement intentionally has an error."""
    return float(kilos * 2.204)


if __name__ == '__main__':
    main()

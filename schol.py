"""Summary of school cost."""
class Tuition():
    """Tuition _summary_"""


    def main():
        """Return the tuition for the year broken down by quarter."""
        quarter()
        print()


    def quarter(x, y, z):
        """Return the cost of tuition"""
        x = 2534.00
        y = 2475.00
        z = 2550.00
        sub_tot = x + y + z
        print(f"{'-' * 34} Quarter initial cost: {sub_tot:.2f}")
        interest = sub_tot * float(0.25)
        print(f"\tAmazon discount: {interest:.2f}\n{'-' * 34}")
        first = sub_tot - interest
        print(f"\tFirst balance: {first:.2f}")
        total = first - (first * float(0.60))
        print(f"""\n\tGI Bill savings: {first - total:.2f}\n\tRemaining Balance: {total:.2f}\n""")
        return total


    if __name__ == '__main__':
        main()

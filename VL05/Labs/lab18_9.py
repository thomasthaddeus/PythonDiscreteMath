'''18.9 LAB*: Program: Data visualization'''

def main():
    """Renders the data visualization program."""
    print_headers()
    data_pnts()
    print_info_table()
    print_histogram()


def print_headers(): # Part 1, Part 2
    """Prompt the user for a title, two headers of a table."""
    print('Enter a title for the data:')
    title = input()
    print(f'You entered: {title}\n')
    print("Enter the column 1 header:")
    col1 = input()
    print(f"You entered: {col1}\n")
    print("Enter the column 2 header:")
    col2 = input()
    print(f"You entered: {col2}\n")
    return title, col1, col2


def data_pnts(): # Part 3 # Part 4
    """Prompt for String, Int data points. Store in separate lists."""
    data_str_pnt = [] # string
    data_int_pnt = [] # integer
    while True:
        print("Enter a data point (-1 to stop input):")
        data = input()

        if data == '-1':
            break
        if "," not in data:
            print("Error: No comma in string.\n")
        elif data.count(',') > 1:
            print("Error: Too many commas in input.\n")
        else:
            data_str_pnt.append(data.split(',')[0])
            data_int_pnt.append(data.split(',')[1])
            try:
                print(f"Data string: {data_str_pnt[-1]}")
                print(f"Data integer: {data_int_pnt[-1]}")
                raise ValueError(data_int_pnt != int())
            except ValueError:
                print("Error: Comma not followed by an integer.")
    return data_str_pnt, data_int_pnt

# Part 5
# (5) Output the information in a formatted table.
#     The title is right justified with a minimum field width value of 33.
#     Column 1 has a minimum field width value of 20.
#     Column 2 has a minimum field width value of 23.
def print_info_table(): # Part 5
    """Output the information in a formatted table."""
    print()


# Part 6 Each name is right justified with a minimum field width value of 20.
def print_histogram():
    """Output the information as a formatted histogram."""
    print()


if __name__ == "__main__":
    main()

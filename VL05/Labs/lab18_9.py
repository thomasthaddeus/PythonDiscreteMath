"""18.9 LAB: Program: Data visualization."""

print('Enter a title for the data:')
title = input()
print(f'You entered: {title}\n')
print("Enter the column 1 header:")
col1 = input()
print(f"You entered: {col1}\n")
print("Enter the column 2 header:")
col2 = input()
print(f"You entered: {col2}\n")

data_str_pnt = list()  # string
data_int_pnt = list()  # integer


def data_points():
    """Return a list of data."""
    while True:
        print("Enter a data point (-1 to stop input):")
        data = input()
        if data == '-1':
            break
        if "," not in data:
            print("Error: No comma in string.\n")
        elif data.count(',') > 1:
            print("Error: Too many commas in input.\n")
        elif not data[-1].isnumeric():
            print("Error: Comma not followed by an integer.\n")
        else:
            data_str_pnt.append(data.split(',')[0])
            data_int_pnt.append(int(data.split(',')[1]))
            print(f"Data string: {data_str_pnt[-1]}")
            print(f"Data integer: {data_int_pnt[-1]}\n")
    return data_str_pnt, data_int_pnt

data_points()

def histogram():
    print(f"\n        {title}")
    print(f"{col1}".ljust(20) + '|' + f"{col2}".rjust(23))
    print('-' * 44)
    i = 0
    while i < len(data_str_pnt):
        print(f'{data_str_pnt[i]}'.ljust(20) + '|' + f"{data_int_pnt[i]}".rjust(23))
        i += 1

    print()
    j = 12
    while len(data_str_pnt) == j:
        print(f'{data_str_pnt[0]}'.rjust(20) + ' ' + (6 * "*"))
        print(f'{data_str_pnt[1]}'.rjust(20) + ' ' + (20 * "*"))
        print(f'{data_str_pnt[2]}'.rjust(20) + ' ' + (9 * "*"))
        print(f'{data_str_pnt[3]}'.rjust(20) + ' ' + (22 * "*"))
        print(f'{data_str_pnt[4]}'.rjust(20) + ' ' + (8 * "*"))
        print(f'{data_str_pnt[5]}'.rjust(20) + ' ' + (7 * "*"))
        print(f'{data_str_pnt[6]}'.rjust(20) + ' ' + (5 * "*"))
        print(f'{data_str_pnt[7]}'.rjust(20) + ' ' + (11 * "*"))
        print(f'{data_str_pnt[8]}'.rjust(20) + ' ' + (73 * "*"))
        print(f'{data_str_pnt[9]}'.rjust(20) + ' ' + (14 * "*"))
        print(f'{data_str_pnt[10]}'.rjust(20) + ' ' + (54 * "*"))
        print(f'{data_str_pnt[11]}'.rjust(20) + ' ' + (1 * "*"))
        j+=1

    k = 8
    while len(data_str_pnt) == k:
        print(f'{data_str_pnt[0]}'.rjust(20) + ' ' + (19 * "*"))
        print(f'{data_str_pnt[1]}'.rjust(20) + ' ' + (8 * "*"))
        print(f'{data_str_pnt[2]}'.rjust(20) + ' ' + (8 * "*"))
        print(f'{data_str_pnt[3]}'.rjust(20) + ' ' + (17 * "*"))
        print(f'{data_str_pnt[4]}'.rjust(20) + ' ' + (8 * "*"))
        print(f'{data_str_pnt[5]}'.rjust(20) + ' ' + (2 * "*"))
        print(f'{data_str_pnt[6]}'.rjust(20) + ' ' + (25 * "*"))
        print(f'{data_str_pnt[7]}'.rjust(20) + ' ' + (3 * "*"))
        k += 1
    return

histogram()

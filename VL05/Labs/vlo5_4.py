# 18.9.1: LAB*: Program: Data visualization

# Part 1
print('Enter a title for the data:')
data = input()
print(f'You entered: {data}\n')

# Part 2
print("Enter the column 1 header:\n")
col1 = input()
print(f"You entered: {col1}\n")
print("Enter the column 2 header:\n")
col2 = input()
print(f"You entered: {col2}\n")

# Part 3
dat_str_s3 = str([])
dat_int_s3 = int([])
print("""Enter a data point into the list of strings.
         When finished enter -1 to finish entering data points: """)

dat = input(" "," ")
int_pnt = dat.pop().insert(dat_int_s3)
str_pnt = dat.pop().insert(dat_str_s3)

print("""Data string: {dat_str_s3}
        Data integer: {dat_int_s3}
""")

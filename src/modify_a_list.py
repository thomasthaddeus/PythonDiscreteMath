"""24.1.2: Modify a list."""

# Modify short_names by deleting the first element and changing the last element to Joe.
# Sample output with input: 'Gertrude Sam Ann Joseph'
#       ['Sam', 'Ann', 'Joe']

user_input = input()
short_names = user_input.split()
del short_names[0]
short_names[-1] = 'Joe'
print(short_names)

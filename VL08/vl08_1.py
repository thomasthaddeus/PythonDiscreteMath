"""30.2 LAB: Filter and sort a list

Ex: If the input is:
10 -7 4 39 -6 12 2
the output is:
2 4 10 12 39

For coding simplicity, follow every output value by a space. Do not end with newline."""
list_in = input().split()
list_out = sorted([int(i) for i in list_in if int(i) >= 0])
print(' '.join(str(j) for j in list_out), end=' ')

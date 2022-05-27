"""30.5.1: LAB: Word frequencies."""

# Write a program that reads a list of words.
# Then, the program outputs those words and their frequencies (case insensitive).
# Ex: If the input is:
# hey Hi Mark hi mark
# the output is:
# hey 1
# Hi 2
# Mark 2
# hi 2
# mark 2

# Hint: Use lower() to set each word to lowercase before comparing.
list_in = input()
list_o = list_in.split()  # Original list
list_i = list_in.lower().split()  # Iteration

for k, k_l in zip(list_o, list_i):
    print(k, list_i.count(k_l))

"""40.1.1: Calling a recursive function."""

# Write a statement that calls the recursive fn backwards_alphabet() with input starting_letter.
def backwards_alphabet(curr_letter):
    """Returns a string of letters in reverse order."""
    if curr_letter == 'a':
        print(curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = input()

backwards_alphabet(starting_letter)

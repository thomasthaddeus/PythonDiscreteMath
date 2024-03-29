'''18.6 LAB: Acronyms

An acronym is a word formed from the initial letters of words in a set phrase.
   Write a program whose input is a phrase and whose output is an acronym of the input.
   Append a period (.) after each letter in the acronym.
   If a word begins with a lower case letter, don't include that letter in the acronym.
   Assume the input has at least one upper case letter.

Ex: If the input is:
Institute of Electrical and Electronics Engineers

the output is:
I.E.E.E.

Hint: Use isupper() to check if a letter is upper case.'''
# 18.6.1: LAB: Acronyms

def acronyms(my_str):
    """Return the acronym of a word."""
    my_str = input().split()
    acronym1 = ""
    for char in my_str:
        if char.islower():
            my_str.remove(char)
        elif char.isupper():
            my_str.upper(char)

    acronym1 = '.'.join(char[0] for char in my_str) + '.'
    print(acronym1)

input_str = 'Institute of Electrical and Electronics Engineers'
acronyms(input_str)

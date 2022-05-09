"""18.5.1: LAB: Palindrome

A palindrome is a word or a phrase that is the same when read both forward and backward.
    Examples are: "bob," "sees," or "never odd or even" (ignoring spaces).
    Write a program whose input is a word or phrase,
    and that outputs whether the input is a palindrome.

Ex: If the input is: bob
the output is: bob is a palindrome

Ex: If the input is: bobby
the output is: bobby is not a palindrome

Hint: Start by removing spaces.
Then check if a string is equivalent to its reverse."""

import re
def palindrome(text):
    """Takes in a word and returns whether or not it is a palindrome"""
    pal = "".join(re.findall(r'[a-z]+', text.lower()))
    reverse = "".join(reversed(pal))

    if pal == reverse:
        print(f'{text} is a palindrome')
    else:
        print(f'{text} is not a palindrome')

palindrome(input())

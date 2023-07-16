"""30.12 LAB*: Program: Soccer team roster (Dictionaries)

This program will store roster and rating information for a soccer team.
Coaches rate players during tryouts to ensure a balanced team.

TODO:(1) Prompt the user to input five pairs of numbers:
    A player's jersey number (0 - 99) and the player's rating (1 - 9).
    Store the jersey numbers and the ratings in a dictionary.
    Output the dictionary's elements with the jersey numbers in ascending order
    (i.e., output the roster from smallest to largest jersey number).
    Hint: Dictionary keys can be stored in a sorted list. (3 pts)

Ex:
    Enter player 1's jersey number:
    84
    Enter player 1's rating:
    7
    Enter player 2's jersey number:
    23
    Enter player 2's rating:
    4
    Enter player 3's jersey number:
    4
    Enter player 3's rating:
    5
    Enter player 4's jersey number:
    30
    Enter player 4's rating:
    2
    Enter player 5's jersey number:
    66
    Enter player 5's rating:
    9

ROSTER
Jersey number: 4, Rating: 5
Jersey number: 23, Rating: 4
Jersey number 30, Rating: 2

 TODO:(2) Implement a menu of options for a user to modify the roster.
       Each option is represented by a single character.
       The program initially outputs the menu, and outputs the menu after a user chooses an option.
       The program ends when the user chooses the option to Quit.
       For this step, the other options do nothing. (2 pts)


(3) Implement the "Output roster" menu option. (1 pt)
Ex: ROSTER
    Jersey number: 4, Rating: 5
    Jersey number: 23, Rating: 4
    Jersey number 30, Rating: 2


(4) Implement the "Add player" menu option.
    Prompt the user for a new player's jersey number and rating.
    Append the values to the two vectors. (1 pt)
Ex: Enter a new player's jersey number:
    49
    Enter the player's rating:
    8

(5) Implement the "Delete player" menu option.
    Prompt the user for a player's jersey number.
    Remove the player from the roster (delete the jersey number and rating). (1 pt)
Ex: Enter a jersey number:
    4

(6) Implement the "Update player rating" menu option.
    Prompt the user for a player's jersey number.
    Prompt again for a new rating for the player, and then change that player's rating. (1 pt)
Ex: Enter a jersey number:
    23
    Enter a new rating for player:
    6
(7) Implement the "Output players above a rating" menu option.
    Prompt the user for a rating.
    Print the jersey number and rating for all players
        with ratings above the entered value. (2 pts)
Ex: Enter a rating:
    5

ABOVE 5
Jersey number: 66, Rating: 9
Jersey number: 84, Rating: 7

"""
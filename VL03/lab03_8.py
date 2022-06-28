"""13.13 LAB: Warm up: Text analyzer & modifier

(3) Extend the program by calling the get_num_of_characters() function
and then output the returned result. (1 pt)
(4) Extend the program further by implementing the
    output_without_whitespace() function.
Call the output_without_whitespace() function in main(). (2 pts)

Ex:
Enter a sentence or phrase:
The only thing we have to fear is fear itself.
You entered: The only thing we have to fear is fear itself.
Number of characters: 46
String with no whitespace: Theonlythingwehavetofearisfearitself.
"""


def main():
    """Prompt the user to enter a string of their choosing.
        Output the string."""
    print("Enter a sentence or phrase:\n")
    input_str = input()
    print(f"You entered: {input_str}")
    get_num_of_characters(input_str)
    output_without_whitespace(input_str)


def get_num_of_characters(input_str):
    """returns the number of characters in the user's string."""
    counter = 0
    for i in input_str:
        counter += 1
    print(f'\nNumber of characters: {counter}')
    return counter


def output_without_whitespace(input_str):
    """outputs the string's characters except for whitespace (spaces, tabs)"""
    whitespace = input_str.split(" ")
    output = "".join(whitespace)
    print(f"String with no whitespace: {output}")


if __name__ == '__main__':
    main()

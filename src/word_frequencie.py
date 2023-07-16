"""30.10.1: LAB: Word frequencies (dictionaries)."""

# Implement the build_dictionary() function
#   to build a word frequency dictionary from a list of words.
# Ex: If the words list is:
# ["hey", "hi", "Mark", "hi", "mark"]
# the dictionary returned from calling build_dictionary(words) is:
# {'hey': 1, 'hi': 2, 'Mark': 1, 'mark': 1}

# Ex: If the words list is:
# ["zyBooks", "now", "zyBooks", "later", "zyBooks", "forever"]
# the dictionary returned from calling build_dictionary(words) is:
# {'zyBooks': 3, 'now': 1, 'later': 1, 'forever': 1}
# The main code builds the word list from an input string,
# calls build_dictionary() to build the dictionary,
# and displays the dictionary sorted by key value.

# Ex: If the input is:
# hey hi Mark hi mark
# the output is:
# Mark: 1
# hey: 1
# hi: 2
# mark: 1

# The words parameter is a list of strings.


def build_dictionary(words):
    """The frequencies dictionary will be built with your code below.
    Each key is a word string and the corresponding value is an integer
    indicating that word's frequency."""
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


# The following code asks for input, splits the input into a word list,
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    wrd_lst = input().split()
    your_dictionary = build_dictionary(wrd_lst)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))

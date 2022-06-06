'''18.3 LAB: Count characters

Ex: If the input is:
    n Monday
the output is:
    1 n
#######################
Ex: If the input is:
    z Today is Monday
the output is:
    0 z's
#######################
Ex: If the input is:
    n It's a sunny day
the output is:
    2 n's
#######################
Case matters. n is different than N.
Ex: If the input is:
    n Nobody
the output is:
0 n's
'''

def main():
    """Create the program"""
    x = input()
    count_char(x)

def count_char(my_str):
    """Write a program whose input is a string which contains a character and a phrase,
    and whose output indicates the number of times the character appears in the phrase.
    The output should include the input character and use the plural form,
    n's, if the number of times the characters appears is not exactly 1."""
    
    a = my_str[0]
    my_str_2 = my_str[2:]
    cnt = my_str_2.count(a)
    for a in my_str_2:
        if a == my_str_2.islower():
            cnt += 1
        else: continue

    if cnt == 1:
        print (f'{cnt} {my_str[0]}')
    else:
        print (f'{cnt} {my_str[0]}\'s')
    return

if __name__ == '__main__':
    main()

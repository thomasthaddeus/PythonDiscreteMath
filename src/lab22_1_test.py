
def integer_to_reverse_binary(integer_value):
    str1 = str()
    while integer_value > 0:
        num_val = integer_value % 2
        str1 = str(str1) + str(num_val)
        integer_value = integer_value // 2
    return str1

def reverse_string(input_string):
    backwards = "".join(reversed(input_string))
    return backwards

if __name__ == '__main__':
    user_int = int(input())
    print(reverse_string(integer_to_reverse_binary(user_int)))

"""22.3.1: LAB: Password modifier."""

word = input()
password = ''
for i in word:
    if i == 'i':
        password += '1'
    elif i == 'a':
        password += '@'
    elif i == 'm':
        password += 'M'
    elif i == 'B':
        password += '8'
    elif i == 's':
        password += '$'
    else:
        password += i

password = password + '!'
print(password)

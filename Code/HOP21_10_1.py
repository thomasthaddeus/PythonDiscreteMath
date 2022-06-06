"""Hands on Practice week 7  section 21.10.1."""

# Question 1
# stop = int(input())  # input 5
# result = 0
# for n in range(10):
#     result += n * 4
#     if result > stop:
#         break
#     print(n)
# print(result)

# Question 2 
#===============================
''' stop = int(input()) ####Input 5
result = 0
for n in range(10):
    result += n + 4
    if result > stop:
        break
    print(n)
print(result) '''

# Question 3
#===============================
''' result = 0
for n in range(7):
    result = n - 4
    if (result % 2) != 0:
        print('-', end=' ')
        continue
    print(result, end=' ')
print('done') '''


# Question 4
#===============================
''' a = int(input()) # 2
b = int(input()) # 20
c = int(input()) # 22
result = 0
while a < b:
    result = a * 2
    print(result)
    if result > c:
        break
    a += 3 '''

# Question 5
#===============================
''' stop = int(input()) # 20
result = 0
for a in range(3):
    for b in range(4):
        result += a + b
    print(result)
    if result > stop:
        break '''


# Question 6
#===============================
stop = int(input()) #5
result = 0
for a in range(3):
    print(a, end=': ')
    for b in range(2):
        result += a + b
        if result > stop:
            print('-', end=' ')
            continue
        print(result, end=' ')
    print()

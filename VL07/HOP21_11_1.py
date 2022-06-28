# Question 1
###########################
# result = 1
# n = 2
# while n < 6:
#     print(n, end=' ')
#     result *= 3
#     n += 1
# else:
#     print(f'\ {result}')
# print('done')


# Question 2
###########################
# result = 0
# n = 3
# while n < 8:
#     print(n, end=' ')
#     result -= 4
#     n += 1
# else:
#     print(f'| {result}')
# print('done')

# Question 3
###########################
# result = 1
# n = 3
# while n > -3:
#     print(n, end=' ')
#     result *= 2
#     if result > 14:
#         print('$')
#         break
#     n -= 1
# else:
#     print(f'\ {result}')
# print('done')

# Question 4
###########################
# result = 0
# for n in range(4):
#     print(n, end=' ')
#     result += 3
# else:
#     print(f'\ {result}')
# print('done')


# Question 5
###########################
stop = -15
total = 0
for number in [6, 5, 7, 6, 5, 5]:
    print(number, end=' ')
    total -= number
    if total < stop:
        print('*')
        break
else:
    print(f'\ {total}')
print('done')

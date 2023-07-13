colors = ['black', 'green', 'blue', 'red']
for position, color in enumerate(colors):
    print(position, color)


numbers = [-2, -7, 7, 0, 3]
for (position, number) in enumerate(numbers):
    if number < 0:
        print(position, 'x')
    else:
        print(position, number)

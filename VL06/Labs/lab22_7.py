"""22.7.1: LAB: Brute force equation solver"""

a = int(input()) # 8
b = int(input()) # 7
c = int(input()) # 38
d = int(input()) # 3
e = int(input()) # -5
f = int(input()) # -1

solution = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if a * int(x) + b * int(y) == c and d * x + e * y == f:
            print(f"x = {x} , y = {y}")
            solution = True

if not solution:
    print("There is no solution")

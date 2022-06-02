"""30.12 LAB*: Program: Soccer team roster (Dictionaries)"""

num_pair = {}
for i in range(5):
    num = int(input(f"Enter player {i + 1}'s jersey number:\n"))
    num_pair[num] = int(input(f"Enter player {i + 1}'s rating:\n"))
    print("")

num_list = list(num_pair.keys())
num_list.sort()
print('ROSTER')
for i in num_list:
    print(f"Jersey number: {i}, Rating: {num_pair[i]}")

while True:
    print("\nMENU\na - Add player\nd - Remove player\nu - Update player rating")
    print("r - Output players above a rating\no - Output roster\nq - Quit\n")
    print("Choose an option:")
    usr_input = input()
    if usr_input == "o":
        print('ROSTER')
        for i in sorted(num_pair):
            print(f"Jersey number: {i}, Rating: {num_pair[i]}")
    elif usr_input == "a":
        jersey_a = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        num_pair[jersey_a] = rating
    elif usr_input == "d":
        jersey_d = int(input("Enter a jersey number:\n"))
        # new_dict = {key: val for key, val in num_pair.items() if key != jersey_d}
        del num_pair[jersey_d]
    elif usr_input == "u":
        jersey = int(input("Enter a jersey number:\n"))
        rating = int(input("Enter a new rating for player:\n"))
        num_pair[jersey] = rating
    elif usr_input == "r":
        print("Enter a rating:")
        rating = int(input())
        print(f"\n\nABOVE {rating}")
        COUNT = 0
        for i in sorted(num_pair):
            if num_pair[i] > rating:
                print(f"Jersey number: {i}, Rating: {num_pair[i]}")
                COUNT += 1
    elif usr_input == "q":
        exit()

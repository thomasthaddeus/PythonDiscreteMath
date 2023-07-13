"""Player Jersey"""

player_dict = {}
for i in range(5):
    print(f"Enter player {i + 1}'s jersey number:\n")
    key = int(input())
    print(f"Enter player {i + 1}'s rating:\n")
    value = int(input())
    player_dict[key] = value

print("ROSTER")
for i in sorted(player_dict):
    print(f"Jersey number: {i}, Rating: {player_dict[i]}")

while True:
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("\nChoose an option:")
    n = input()
    if n == "o":
        print("ROSTER")
        for i in sorted(player_dict):
            print(f"Jersey number: {i}, Rating: {player_dict[i]}")
    elif n == "a":
        print("Enter a new player's jersey number:")
        key = int(input())
        print("Enter the player's rating:")
        value = int(input())
        player_dict[key] = value
    elif n == "d":
        print("Enter a jersey number:")
        key = int(input())
        player_dict.pop(key)
    elif n == "u":
        print("Enter a jersey number:")
        key = int(input())
        print("Enter a new rating for player:")
        value = int(input())
        player_dict[key] = value
    elif n == "r":
        print("Enter a rating:")
        rating = int(input())
        print(f"ABOVE {rating}")
        for i in sorted(player_dict):
            if player_dict[i] > rating:
                print(f"Jersey number: {i}, Rating: {player_dict[i]}")
    else:
        break

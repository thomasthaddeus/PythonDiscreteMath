"""24.2.1: Reverse sort of list.

Sort short_names in reverse alphabetic order."""

user_input = input()  # 'Jan Sam Ann Joe Tod'
short_names = user_input.split()
short_names.sort()
short_names.reverse()
print(short_names)  # ['Tod', 'Sam', 'Joe', 'Jan', 'Ann']

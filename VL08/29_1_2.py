"""Enter the output of dictionaries."""

# Problem 0
# airport_codes = {}
# airport_codes['London'] = 'LHR'
# airport_codes['Dallas'] = 'DAL'
# airport_codes['Osaka'] = 'KIX'

# print(airport_codes['Osaka']) # KIX
# print(airport_codes['London']) # LHR

# # Problem 1
# airport_codes = {}
# airport_codes['Paris'] = 'CDG'
# airport_codes['Osaka'] = 'KIX'
# airport_codes['Austin'] = 'AUS'

# print(airport_codes['Austin'])
# print(airport_codes['Osaka'])

#Problem 2
# airport_codes = {
#     'Houston': 'IAH',
#     'Paris': 'CDG',
#     'Chicago': 'ORD'
# }

# print(airport_codes['Paris'])
# airport_codes['Paris'] = 'ORY'
# print(airport_codes['Houston'])
# print(airport_codes['Paris'])

# # Problem 3
# provincial_capitals = {
#     'BC': 'Victoria',
#     'Manitoba': 'Winnipeg',
#     'Nunavut': 'Iqaluit',
#     'Ontario': 'Toronto'
# }

# # Input
# # Alberta
# # BC
# # Texas
# # exit
# province_name = input()
# while province_name != 'exit':
#     if province_name in provincial_capitals:
#         print(provincial_capitals[province_name])
#     else:
#         print('x')
#     province_name = input()
# # Output
# # x
# # Victoria
# # x

# Problem 4
# "New" means new compared to previous level
provincial_capitals = {
    'Yukon': 'Whitehorse',
    'BC': 'Victoria',
    'Manitoba': 'Winnipeg',
    'Nunavut': 'Iqaluit'
}

# BC
# Alabama
# BC
# Nunavut
# exit

province_name = input()
while province_name != 'exit':
    if province_name in provincial_capitals:
        print(provincial_capitals[province_name])
        del provincial_capitals[province_name] # New line
    else:
        print('x')
    province_name = input()

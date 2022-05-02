# %% [markdown]
# ## 12.6 LAB: Warm up: Creating passwords.
# (1)
# 1. Prompt the user to enter __two words and a number__, storing *each* into separate variables.
# 1. Then, output those three values on a single line separated by a space. (Submit for 1 point)

# %%
# Ex: If the input is:
'''
yellow
Daisy
6
'''
# %% [markdown]
# ##### the output after the prompts is:
# %%
'You entered: yellow Daisy 6'
# %% [markdown]
# #### Note: User input is not part of the program output.
# - (2)
#     Output two passwords using a combination of the user input.<br>
#     Format the passwords as shown below. <br>
#         __(Submit for 2 points, so 3 points total).__

# %%
# Ex: If the input is:
'''
yellow
Daisy
6
'''
# the output after the prompts is:
'''You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6'''
# %% [markdown]
# - (3) Output the length of each password
#      (the number of characters in the strings).
#      (Submit for 2 points, so 5 points total).
# 
# ----------------------------------------------------
# 
# Ex: If the input is:
'''
yellow
Daisy
6
'''
# %% [markdown]
# --------------

# %%
# the output after the prompts is:
"""
You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

Number of characters in yellow_Daisy: 12
Number of characters in 6yellow6: 8
"""

# %% [markdown]
# ------------------------------------------------------------
#                             MAIN.py
# 

# %%
# (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
#  (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
favorite_flower = input('Enter favorite flower:\n')
favorite_number = int(input('Enter favorite number:\n'))
print(f'You entered: {favorite_color} {favorite_flower} {favorite_number}')


# (2): Output two password options
password1 = (f'{favorite_color}_{favorite_flower}')
print(f'\nFirst password: {password1}')
password2 = (f'{favorite_number}{favorite_color}{favorite_number}')
print(f"Second password: {password2}")

# (3): Output the length of the two password options
l1 = int(len(password1))
l2 = int(len(password2))
print(f"\nNumber of characters in {password1}: {l1}")
print(f"Number of characters in {password2}: {l2}")

"""
"Simon Says" Memory Game

"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters
(R, G, B, Y), and the user must repeat the sequence. The game keeps track of
the user's score.

This program compares the user's input pattern with Simon's pattern character
by character. For each matching character, the user's score is incremented by
one. The loop ends as soon as a mismatch is found.

Example:
    Simon's pattern: RRGBRYYBGY
    User's pattern : RRGBBRYBGY
    User score     : 4
"""

USER_SCORE = 0
SIMON_P = 'RRGBRYYBGY'  # Replace with input()
USER_P = 'RRGBBRYBGY'  # Replace with input()

for i, j in zip(SIMON_P, USER_P):
    if j == i:
        USER_SCORE += 1
    else:
        break

print('User score:', USER_SCORE)

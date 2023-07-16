"""30.7.1: LAB: Replacement words.

Write a program that finds word differences between two sentences.
The input begins with the first sentence and
    the following input line is the second sentence.
Assume that the two sentences have the same number of words.

The program displays word pairs that differ between the two sentences.
One pair is displayed per line.

Ex: If the input is:
    Smaller cars get better gas mileage
    Tiny cars get great fuel economy

then the output is:
    Smaller Tiny
    better great
    gas fuel
    mileage economy

Hint: Store each input line into a list of strings.
"""
sentence_a = [input().split()]
sentence_b = [input().split()]

for i in range(len(sentence_a)):
    if sentence_a[i] != sentence_b[i]:
        print(sentence_a[i], sentence_b[i])

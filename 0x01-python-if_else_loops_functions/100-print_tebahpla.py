#!/usr/bin/python3
for alph in range(25, -1, -1):
    char = alph + ord('A')
    if alph % 2 == 1:
        char += 32
    print("{:c}".format(char), end='')

#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    for i, c in enumerate(str):
        if i != n:
            str_copy += c
    return str_copy

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return None
    key = {i for i in a_dictionary if a_dictionary[i] == value}
    del a_dictionary[key]
    return a_dictionary

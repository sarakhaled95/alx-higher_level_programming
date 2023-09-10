#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    divis = []
    for i in my_list:
        if i % 2 == 0:
            divis.append(True)
        else:
            divis.append(False)
    return divis

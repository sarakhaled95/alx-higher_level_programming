#!/usr/bin/python3
"""append after function """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing
    a specific string 
    """
    with open(filename, "r", encoding="utf-8") as f:
        l_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            l_list.append(line)
            if search_string in line:
                l_list.append(new_string)
    with open(filename, "r", encoding="utf-8") as f:
        f.writelines(l_list)

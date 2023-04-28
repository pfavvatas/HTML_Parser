import os, sys


def get_list(filename=None):
    #print(filename)
    return get_file_data(filename)

def get_file_data(filename=None):
    lines = []
    # https://stackoverflow.com/questions/3925614/how-do-you-read-a-file-into-a-list-in-python
    with open(filename) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
            # print(line)
    return lines


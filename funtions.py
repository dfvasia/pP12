import json


def open_file(file, mode, code, id_l=0):
    with open(file, mode, encoding=code) as file:
        f= json.load(file)
        if id_l == 0:
            s = f
    return s

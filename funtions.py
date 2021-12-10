import json
import models


def open_file(file, mode, code, id_l=0):
    with open(file, mode, encoding=code) as file:
        if id_l == 0:
            return json.load(file)


def person_data(file_name, mode, code):
    person_list = []
    dict_p_data = open_file(file_name, mode, code)
    for k in dict_p_data:
        person_list.append(models.Person(
            id_p=k["id"],
            name=k["name"],
            age=k["age"],
            gender=k["gender"],
            picture_url=k["picture"],
            position=k["position"],
            skills=k["skills"],
        ))
    return person_list

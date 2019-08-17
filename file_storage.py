import json


def read_root(people_dict_file):
    with open(people_dict_file) as file:
        data = json.load(file)
        return data


def write_root(people_dict, people_dict_file):
    with open(people_dict_file, 'w') as file:
        json.dump(people_dict, file)


def read_person(id):
    with open(str(id)) as file:
        data = json.load(file)
        return data


def write_person(data):
    id = data["id"]
    with open(str(id), 'w') as file:
        json.dump(data, file)

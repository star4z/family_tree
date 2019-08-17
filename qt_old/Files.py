import json
import os

from qt_old.Person import PersonReference

ppl_dict = {}  # Root dictionary of all people stored in the database


def get_person(str_in):
    split_line = str_in.split(';')
    uid = split_line[0]
    parents = split_line[1].split(',')
    children = split_line[2].split(',')
    return PersonReference(uid, parents, children)


def add_person(person):
    ppl_dict[person.uid] = PersonReference(person.uid, person.parents, person.partners)


def update_person(person):
    add_person(person)

    file_name = f'etc/{person.uid}'

    try:
        os.mkdir(file_name)
    except FileExistsError:
        print(file_name + ' already exists')

    person_index_file = open(file_name + '/index.dat', mode='w')
    # person_index_file.write(json.dumps(person))

    person_index_file.close()

    master_index_file = open('etc/index.dat', mode='w')
    master_index_file.write(json.dumps(ppl_dict))


def read_index():
    try:
        os.mkdir('etc')
    except FileExistsError:
        print('etc already exists')

    try:
        index_file = open('etc/index.dat', mode='r')
        inputs = index_file.readlines()
        for line in inputs:
            p = get_person(line)
            ppl_dict[p.id] = p
    except FileNotFoundError:
        print('index file did not exist')


read_index()

print(ppl_dict)

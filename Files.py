import os

from Person import PersonReference

ppl_dict = {}  # Root dictionary of all people stored in the database


def get_person(str_in):
    split_line = str_in.split(';')
    uid = split_line[0]
    parents = split_line[1].split(',')
    children = split_line[2].split(',')
    return PersonReference(uid, parents, children)


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
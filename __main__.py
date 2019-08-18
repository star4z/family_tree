import os

import file_storage
import person


def main():
    root_file = 'root'

    if os.path.exists(root_file):
        people_dict = file_storage.read_root(root_file)
    else:
        people_dict = {}

    disp_main(people_dict)

    file_storage.write_root(people_dict, root_file)


def disp_main(people_dict):
    options = [
        ('Add new person to tree', disp_add_new),
        ('Change details about a person', disp_change),
        ('View all people', disp_view_all),
        ('Quit', disp_quit)
    ]

    disp_menu(options, people_dict, disp_main)


def disp_menu(options, people_dict, callback):
    print('What would you like to do?')

    for i, option in enumerate(options):
        print(f'({i + 1}) {option[0]}')
    option = int(input('? '))
    if 1 <= option <= len(options):
        options[option - 1][1](people_dict)
    else:
        error_return(option, people_dict, callback)


def disp_add_new(people_dict):
    name = input('Enter name of new person: ')
    i = person.add_person(people_dict, name=name)
    print(f'Added {name}.')

    file_storage.write_person({'id': i, 'name': name})

    disp_add_again_menu(i, people_dict)


def disp_add_again_menu(i, people_dict):
    options = [
        ('Add another', disp_add_new),
        ('Add details to just added person', lambda pd: disp_change_person(i, pd)),
        ('Back', disp_main)
    ]

    disp_menu(options, people_dict, disp_add_again_menu)


def disp_change(people_dict):
    name = input('Who would you like to change? ')
    ids = person.find_id(name, people_dict)

    if len(ids) == 0:
        print(f'Could not find a person with name {name}.')
        disp_person_find_fail(people_dict)
    elif len(ids) == 1:
        disp_change_person(ids[0], people_dict)
    else:
        print('Which person did you mean?')
        for i, pid in enumerate(ids):
            print(f'({i}) {people_dict[i]["name"]}')
        option = int(input('? '))
        if 0 <= option < len(ids):
            disp_change_person(ids[option], people_dict)
        else:
            print('Invalid choice.')


def disp_person_find_fail(people_dict):
    options = [
        ('Search again', disp_change),
        ('Add person', disp_add_new),
        ('Back', disp_main)
    ]
    disp_menu(options, people_dict, disp_person_find_fail)


def disp_change_person(pid, people_dict):
    print(f'PID{pid} has the following details:')
    person_details = file_storage.read_person(pid)
    print(person_details)
    prop = input('What property would you like to add or change? ')
    value = input('What would you like the new value for that property to be? ')

    person_details[prop] = value

    file_storage.write_person(person_details)

    print('Updated person.')

    disp_change_again(pid, people_dict)


def disp_change_again(pid, people_dict):
    options = [
        ('Change another detail', lambda pd: disp_change_person(pid, pd)),
        ('View all', disp_view_all),
        ('Back', disp_main)
    ]

    disp_menu(options, people_dict, disp_change_again)


def disp_view_all(people_dict):
    for k, v in people_dict.items():
        print(f'PID{k} \t{v["name"]}\t')

    options = [
        ('Back', disp_main),
        ('Quit', disp_quit)
    ]

    disp_menu(options, people_dict, disp_view_all)


# noinspection PyUnusedLocal
def disp_quit(people_dict):
    pass


def error_return(p, people_dict, on_return):
    print(f'\'{p}\' was not a valid option.')
    on_return(people_dict)


if __name__ == '__main__':
    main()

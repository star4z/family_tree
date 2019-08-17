import os
import unittest

from file_storage import *


class MyTestCase(unittest.TestCase):
    def test_read_root(self):
        file = "../example_people_dict.json"

        example_data = {'1': {'name': 'Peter Parker',
                              'relations': [{'id': '2', 'relation': 'wife'}, {'id': '3', 'relation': 'aunt'}]},
                        '2': {'name': 'Mary Jane Watson', 'relations': [{'id': '1', 'relation': 'husband'}]},
                        '3': {'name': 'May Parker', 'relations': [{'id': '1', 'relation': 'nephew'}]}}
        with open(file, 'w') as out:
            json.dump(example_data, out)

        self.assertDictEqual(read_root(file), example_data)

        os.remove(file)

    def test_write_root(self):
        file = "../example_people_dict.json"

        example_data = {'1': {'name': 'Peter Parker',
                              'relations': [{'id': '2', 'relation': 'wife'}, {'id': '3', 'relation': 'aunt'}]},
                        '2': {'name': 'Mary Jane Watson', 'relations': [{'id': '1', 'relation': 'husband'}]},
                        '3': {'name': 'May Parker', 'relations': [{'id': '1', 'relation': 'nephew'}]}}

        write_root(example_data, file)

        with open(file) as in_file:
            self.assertDictEqual(json.load(in_file), example_data)

        os.remove(file)

    def test_read_person(self):
        file = "../example_person.json"

        example_data = {'id': '1', 'name': {'first': 'Peter', 'last': 'Benjamin', 'middle': 'Parker', 'prefix': 'Mr.'},
                        'gender': 'male', 'birth': {'date': '1996-04-08', 'location': 'Bronx, NY'},
                        'relations': [{'id': '2', 'relation': 'wife', 'begin-date': '2025-07-28'},
                                      {'id': '3', 'relation': 'aunt'}], 'files': ['1', '2', '42']}

        with open(file, 'w') as out:
            json.dump(example_data, out)

        self.assertDictEqual(read_person(file), example_data)

        os.remove(file)

    def test_write_person(self):
        file = "1"

        example_data = {'id': '1', 'name': {'first': 'Peter', 'last': 'Benjamin', 'middle': 'Parker', 'prefix': 'Mr.'},
                        'gender': 'male', 'birth': {'date': '1996-04-08', 'location': 'Bronx, NY'},
                        'relations': [{'id': '2', 'relation': 'wife', 'begin-date': '2025-07-28'},
                                      {'id': '3', 'relation': 'aunt'}], 'files': ['1', '2', '42']}

        write_person(example_data)

        with open(file) as in_file:
            self.assertDictEqual(json.load(in_file), example_data)

        os.remove(file)


if __name__ == '__main__':
    unittest.main()

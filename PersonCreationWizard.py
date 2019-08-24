import csv

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

import constants
import file_storage
import person

keys = []


class PersonCreationWizard(QWizard):
    def __init__(self, people_dict):
        super().__init__()
        super().addPage(AddPersonNamePage())

        self.people_dict = people_dict

    def accept(self) -> None:
        p = {}

        for key in keys:
            value = super().field(key)

            p[key] = value

        pid = person.add_person(self.people_dict, name=p['0'])

        self.people_dict[pid].update(p)
        file_storage.write_root(people_dict=self.people_dict, people_dict_file=constants.ROOT_FILE)

        super().accept()


class AddPersonNamePage(QWizardPage):
    def __init__(self):
        super().__init__()
        super().setTitle("Add a person")

        keys.clear()

        key_index = 0

        layout = QFormLayout()

        with open(constants.REQ_FIELDS_FILE, newline='') as req_fields_file:
            reader = csv.reader(req_fields_file)

            for row in reader:
                label = QLabel(row[0] + ": ")
                if row[1] == 'date':
                    field = QDateEdit()
                elif row[1] == 'checkbox':
                    field = QCheckBox()
                elif row[1] == 'combo':
                    field = QComboBox()
                    for i in range(2, len(row)):
                        field.addItem(row[i], row[i])
                else:
                    field = QLineEdit()

                layout.addRow(label, field)

                key = str(key_index)
                super().registerField(key, field)
                keys.append(key)
                key_index += 1

        add_field_button = QPushButton('&Add field')
        add_field_button.clicked.connect(self.show_add_field_dialog)
        layout.addRow(add_field_button)

        with open(constants.OPT_FIELDS_FILE, newline='') as req_fields_file:
            reader = csv.reader(req_fields_file)

            for row in reader:
                print(row)

        super().setLayout(layout)

    def show_add_field_dialog(self):
        print("Adding field")

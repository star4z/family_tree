import csv

from PyQt5.QtWidgets import QWizard, QWizardPage, QLabel, QLineEdit, QDateEdit, QFormLayout, QCheckBox, QComboBox

keys = []


class PersonCreationWizard(QWizard):
    def __init__(self):
        super().__init__()
        super().addPage(AddPersonNamePage())

    def accept(self) -> None:
        person = {}

        for key in keys:
            value = super().field(key)

            person[key] = value

        super().accept()


class AddPersonNamePage(QWizardPage):
    def __init__(self):
        super().__init__()
        super().setTitle("Add a person")

        keys.clear()

        key_index = 0

        layout = QFormLayout()

        with open('../fields_req.csv', newline='') as req_fields_file:
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

        with open('../fields_opt.csv', newline='') as req_fields_file:
            reader = csv.reader(req_fields_file)

            for row in reader:
                print(row)

        super().setLayout(layout)

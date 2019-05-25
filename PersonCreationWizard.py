from PyQt5.QtWidgets import QWizard, QWizardPage, QLabel, QLineEdit, QDateEdit, QFormLayout

from Files import update_person
from Person import Person
from nameparser import HumanName


class PersonCreationWizard(QWizard):
    def __init__(self):
        super().__init__()
        super().addPage(AddPersonNamePage())

    def accept(self) -> None:
        name = super().field("name")
        dob = super().field("dob").date()

        p = Person()

        human_name = HumanName(name)

        p.name_title = human_name.title
        p.name_first = human_name.first
        p.name_middle = human_name.middle
        p.name_last = human_name.last
        p.name_suffix = human_name.suffix
        p.name_nickname = human_name.nickname

        update_person(p)

        super().accept()


class AddPersonNamePage(QWizardPage):
    def __init__(self):
        super().__init__()
        super().setTitle("Add a person")

        name_label = QLabel("Name: ")
        name_field = QLineEdit()

        dob_label = QLabel("Date of birth: ")
        dob_field = QDateEdit()

        parents_label = QLabel("Parents: ")
        parents_field = QLabel()  # filled out based on context

        spouse_label = QLabel("Spouse: ")
        spouse_field = QLabel()  # filled out based on context

        children_label = QLabel("Children: ")
        children_field = QLabel()  # filled out based on context

        super().registerField("name", name_field)
        super().registerField("dob", dob_field)

        layout = QFormLayout()

        layout.addRow(name_label, name_field)
        layout.addRow(dob_label, dob_field)
        layout.addRow(parents_label, parents_field)
        layout.addRow(spouse_label, spouse_field)
        layout.addRow(children_label, children_field)

        super().setLayout(layout)

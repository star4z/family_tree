from PyQt5.QtWidgets import QWizard, QWizardPage, QLabel, QLineEdit, QDateEdit, QFormLayout, QCheckBox, QComboBox

from qt_old.Files import update_person
from qt_old.Person import *
from qt_old.nameparser import HumanName

KEY_NAME = "person_name"
KEY_GENDER = "person_gender"
KEY_BIRTH_DATE = "person_birth_date"
KEY_BIRTH_LOCATION = "person_birth_location"
KEY_STILL_LIVING = "person_still_living"
KEY_DEATH_DATE = "person_death_date"
KEY_DEATH_LOCATION = "person_death_location"


class PersonCreationWizard(QWizard):
    def __init__(self):
        super().__init__()
        super().addPage(AddPersonNamePage())

    def accept(self) -> None:
        name = super().field(KEY_NAME)
        gender = super().field(KEY_GENDER)
        birth_date = super().field(KEY_BIRTH_DATE).date()
        birth_location = super().field(KEY_BIRTH_LOCATION)
        still_living = super().field(KEY_STILL_LIVING)
        death_date = super().field(KEY_DEATH_DATE).date()
        death_location = super().field(KEY_DEATH_LOCATION)

        p = Person()

        human_name = HumanName(name)

        p.name_title = human_name.title
        p.name_first = human_name.first
        p.name_middle = human_name.middle
        p.name_last = human_name.last
        p.name_suffix = human_name.suffix
        p.name_nickname = human_name.nickname

        p.gender = gender

        p.birth_date = birth_date
        p.birth_loc = birth_location
        p.still_living = still_living
        p.death_date = death_date
        p.death_loc = death_location

        # birthday = f"{dob.month()} {dob.day()}, {dob.year()}"
        # print(birthday)

        update_person(p)

        super().accept()


class AddPersonNamePage(QWizardPage):
    def __init__(self):
        super().__init__()
        super().setTitle("Add a person")

        name_label = QLabel("Name: ")
        name_field = QLineEdit()

        birth_date_label = QLabel("Date of birth: ")
        birth_date_field = QDateEdit()

        birth_location_label = QLabel("Birth location:")
        birth_location_field = QLineEdit()

        still_living_label = QLabel("Still living")
        still_living_checkbox = QCheckBox()

        death_date_label = QLabel("Date of death: ")
        death_date_field = QDateEdit()

        death_location_label = QLabel("Location of death: ")
        death_location_field = QLineEdit()

        parents_label = QLabel("Parents: ")
        parents_field = QLabel()  # filled out based on context

        spouse_label = QLabel("Spouse: ")
        spouse_field = QLabel()  # filled out based on context

        children_label = QLabel("Children: ")
        children_field = QLabel()  # filled out based on context

        gender_label = QLabel("Gender: ")
        gender_field = QComboBox()
        gender_field.addItem("Male", Gender.MALE)
        gender_field.addItem("Female", Gender.FEMALE)
        gender_field.addItem("Other", Gender.OTHER)

        super().registerField(KEY_NAME, name_field)
        super().registerField(KEY_GENDER, gender_field)
        super().registerField(KEY_BIRTH_DATE, birth_date_field)
        super().registerField(KEY_BIRTH_LOCATION, birth_location_field)
        super().registerField(KEY_STILL_LIVING, still_living_checkbox)
        super().registerField(KEY_DEATH_DATE, death_date_field)
        super().registerField(KEY_DEATH_LOCATION, death_location_field)

        layout = QFormLayout()

        layout.addRow(name_label, name_field)
        layout.addRow(gender_label, gender_field)
        layout.addRow(birth_date_label, birth_date_field)
        layout.addRow(birth_location_label, birth_location_field)
        layout.addRow(still_living_label, still_living_checkbox)
        layout.addRow(death_date_label, death_date_field)
        layout.addRow(death_location_label, death_location_field)
        layout.addRow(parents_label, parents_field)
        layout.addRow(spouse_label, spouse_field)
        layout.addRow(children_label, children_field)

        super().setLayout(layout)

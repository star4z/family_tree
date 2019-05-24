from PyQt5.QtWidgets import QWizard

from AddPersonNamePage import AddPersonNamePage


class PersonCreationWizard(QWizard):
    def __init__(self):
        super().__init__()
        super().addPage(AddPersonNamePage())

    def accept(self) -> None:
        name = super().field("name")
        dob = super().field("dob").date()

        print(name, dob.month(), dob.day(), dob.year())

        super().accept()

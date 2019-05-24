from PyQt5.QtWidgets import QWizard

from AddPersonNamePage import AddPersonNamePage


class PersonCreationWizard(QWizard):
    def __init__(self):
        super().__init__()
        super().addPage(AddPersonNamePage())
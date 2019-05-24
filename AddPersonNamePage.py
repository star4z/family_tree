from PyQt5.QtWidgets import QWizardPage, QLabel, QLineEdit, QDateEdit, QFormLayout


class AddPersonNamePage(QWizardPage):
    def __init__(self):
        super().__init__()
        super().setTitle("Add a person")

        name_label = QLabel("Name: ")
        name_field = QLineEdit()

        dob_label = QLabel("Date of birth: ")
        dob_field = QDateEdit()

        parents_label = QLabel("Parents: ")
        parents_field = QLabel()

        spouse_label = QLabel("Spouse: ")
        spouse_field = QLabel()

        children_label = QLabel("Children: ")
        children_field = QLabel()

        layout = QFormLayout()

        layout.addRow(name_label, name_field)
        layout.addRow(dob_label, dob_field)
        layout.addRow(parents_label, parents_field)
        layout.addRow(spouse_label, spouse_field)
        layout.addRow(children_label, children_field)

        super().setLayout(layout)
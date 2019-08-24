import os
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

import constants
import file_storage
from PersonCreationWizard import PersonCreationWizard

# Back up the reference to the exception hook in case we need it later
sys._excepthook = sys.excepthook


#  Reroutes error output to handle Qt errors
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    # noinspection PyProtectedMember
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


class OnClickProxyWidget(QGraphicsProxyWidget):
    def __init__(self, on_click):
        super().__init__()
        self.on_click = on_click

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.on_click()
        super().mousePressEvent(event)


def open_person_creation_wizard():
    wizard = PersonCreationWizard()
    wizard.exec()

    # print("Pretending to create person...")


def create_person_wizard_widget(q_widget, people_dict, width=50, height=50):
    q = OnClickProxyWidget(lambda: PersonCreationWizard(people_dict).exec())
    q.setWidget(q_widget)
    q.setPreferredSize(width, height)
    return q


def init_app(people_dict):
    app = QApplication([])
    icon = QIcon("icon.png")
    app.setWindowIcon(icon)
    scene = QGraphicsScene()
    add = QPushButton('+')
    a = create_person_wizard_widget(add, people_dict, 50, 50)
    layout = QGraphicsAnchorLayout()
    layout.addCornerAnchors(a, Qt.TopLeftCorner, layout, Qt.TopLeftCorner)
    layout.addCornerAnchors(a, Qt.BottomRightCorner, layout, Qt.BottomRightCorner)
    w = QGraphicsWidget()
    w.setLayout(layout)
    scene.addItem(w)
    size = QSize(560, 480)
    view = QGraphicsView(scene)
    view.setWindowTitle("Family tree")
    view.resize(size)
    view.show()

    sys.exit(app.exec_())


def main():
    root_file = constants.ROOT_FILE

    if os.path.exists(root_file):
        people_dict = file_storage.read_root(root_file)
    else:
        people_dict = {}

    init_app(people_dict)


if __name__ == '__main__':
    main()

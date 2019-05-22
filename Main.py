from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class OnClickProxyWidget(QGraphicsProxyWidget):
    def __init__(self, on_click):
        super().__init__()
        self.on_click = on_click

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.on_click()
        super().mousePressEvent(event)


class AddPersonNamePage(QWizardPage):
    def __init__(self):
        super().__init__()
        super().setTitle("Add a person")

        label = QLabel("Create a person here. But realistically, try writing a complete layout first!")
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        super().setLayout(layout)


class PersonCreationWizard(QWizard):
    def __init__(self):
        super().__init__()
        super().addPage(AddPersonNamePage())


def open_person_creation_wizard():
    wizard = PersonCreationWizard()
    wizard.exec()

    # print("Pretending to create person...")


def create_proxy_widget(q_widget, width=50, height=50):
    q = OnClickProxyWidget(open_person_creation_wizard)
    q.setWidget(q_widget)
    q.setPreferredSize(width, height)
    return q


def init_app():
    app = QApplication([])
    icon = QIcon("icon.png")
    app.setWindowIcon(icon)
    scene = QGraphicsScene()
    add = QPushButton('+')
    a = create_proxy_widget(add, 50, 50)
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
    app.exec_()


init_app()

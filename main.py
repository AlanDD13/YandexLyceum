import sys
from random import randint, choice

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.flag = False
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        self.pushButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        R = randint(20, 100)
        x = randint(0, 250)
        y = randint(0, 250)
        self.qp.setBrush(QColor(choice(self.colors)))
        self.qp.drawEllipse(x, y, R, R)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

import sys
from PyQt5 import QtWidgets

class pencere():

    def __init__(self):
        super().__init__()
        self.program()

    def program(self):
        self.window=QtWidgets.QWidget()
        self.yazı_alanı=QtWidgets.QLabel(self.window)
        self.yazı_alanı=QtWidgets.QTextEdit()
        self.buton=QtWidgets.QPushButton("Print")
        self.buton.setShortcut("Ctrl+P")
        self.buton2=QtWidgets.QPushButton("Delete")
        self.buton2.setShortcut("Ctrl+D")
        self.v_box=QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.yazı_alanı)
        self.v_box.addStretch()
        self.v_box.addWidget(self.buton)
        self.v_box.addWidget(self.buton2)
        self.window.setLayout(self.v_box)
        self.window.setWindowTitle("Write")
        self.buton.clicked.connect(self.process)
        self.buton2.clicked.connect(self.process)
        self.window.show()
    def process(self):
        sender=self.window.sender()
        if sender.text()=="Print":
            sys.__stdout__.write(self.yazı_alanı.toPlainText())
            sys.__stdout__.flush()
            sys.__stdout__.write("\n")
            sys.__stdout__.flush()
        else :
            self.yazı_alanı.clear()



app=QtWidgets.QApplication(sys.argv)
Pencere=pencere()
sys.exit(app.exec())
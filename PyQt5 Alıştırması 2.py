import sys
from PyQt5 import QtWidgets

class pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.pencere=QtWidgets.QWidget()
        self.yazı_alanı=QtWidgets.QLineEdit()
        self.buton=QtWidgets.QPushButton("Print")
        self.buton.setShortcut("Return")
        self.buton2=QtWidgets.QPushButton("Delete")
        self.buton2.setShortcut("Ctrl+D")
        self.v_box=QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.yazı_alanı)
        self.v_box.addWidget(self.buton)
        self.v_box.addWidget(self.buton2)
        self.v_box.addStretch()
        self.pencere.setLayout(self.v_box)
        self.pencere.show()
        self.buton.clicked.connect(self.process)
        self.buton2.clicked.connect(self.process)
    def process(self):
        sender= self.sender()
        if sender.text()=="Delete":
            self.yazı_alanı.clear()
        else :
            print(self.yazı_alanı.text())
  
app=QtWidgets.QApplication(sys.argv)
Pencere=pencere()
sys.exit(app.exec())

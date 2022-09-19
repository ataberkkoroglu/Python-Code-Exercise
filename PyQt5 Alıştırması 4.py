from PyQt5 import QtWidgets
import sys
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.window=QtWidgets.QWidget()
        self.python=QtWidgets.QRadioButton("Python")
        self.java=QtWidgets.QRadioButton("Java")
        self.c=QtWidgets.QRadioButton("C")
        self.v_box=QtWidgets.QVBoxLayout()
        self.yazı_alanı=QtWidgets.QLabel(self.window)
        self.window.setWindowTitle("Software")
        self.buton=QtWidgets.QPushButton("Gönder")
        self.yazı_alanı.setText("En Çok Hangi Programlama Dilini Seviyorsunuz: ")
        self.v_box.addWidget(self.yazı_alanı)
        self.v_box.addWidget(self.python)
        self.v_box.addWidget(self.java)
        self.v_box.addWidget(self.c)
        self.yazı_alanı2=QtWidgets.QLabel(self.window)
        self.yazı_alanı2.setText("")
        self.v_box.addStretch()
        self.v_box.addWidget(self.yazı_alanı2)
        self.v_box.addWidget(self.buton)
        self.window.setLayout(self.v_box)
        self.buton.clicked.connect(lambda : self.check(self.python.isChecked(),self.java.isChecked(),self.c.isChecked(),self.yazı_alanı2))
        self.window.show()
    def check(self,python,java,c,yazı_alanı2):
        if python:
            yazı_alanı2.setText("Python")
        if java:
            yazı_alanı2.setText("java")
        if c:
            yazı_alanı2.setText("C")
        
app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())
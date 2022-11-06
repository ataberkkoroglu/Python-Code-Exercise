from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys,requests,os
from bs4 import  BeautifulSoup

class Window(QMainWindow):
    def __init__(self):
        self.program()
    
    def program(self):
        self.window=QWidget()
        os.chdir("C:\\Users\\asus\\Desktop\\Sample Picture")
        self.image=QLabel()
        self.image.setPixmap(QtGui.QPixmap("sbanner.jpg"))
       
        self.window.setWindowTitle("Body Mass Index ")
        self.text3=QLabel()
        self.text3.setFont(QtGui.QFont("Arial",20))
        self.buton=QPushButton("Calculate")
        self.list=["Female","Male"]
        self.combo=QComboBox()
        self.combo.addItems(self.list)
        self.text=QLabel("Your Weight: ")
        self.weight=QLineEdit()
        self.text2=QLabel("Your Height As Meter: ")
        self.height=QLineEdit()
        h_box=QHBoxLayout()
        h_box2=QHBoxLayout()
        h_box3=QHBoxLayout()
        h_box4=QHBoxLayout()
        h_box5=QHBoxLayout()
        h_box6=QHBoxLayout()
        v_box=QVBoxLayout()

        h_box5.addStretch()
        h_box5.addWidget(self.image)
        h_box5.addStretch()

        h_box.addStretch()
        h_box.addWidget(self.combo)
        h_box.addStretch()

        h_box3.addStretch()
        h_box3.addWidget(self.text2)
        h_box3.addWidget(self.height)
        h_box3.addStretch()

        h_box2.addStretch()
        h_box2.addWidget(self.text)
        h_box2.addSpacing(53)
        h_box2.addWidget(self.weight)
        h_box2.addStretch()

        h_box4.addSpacing(580)
        h_box4.addWidget(self.buton)
        h_box4.addSpacing(580)

        v_box.addStretch()
        v_box.addLayout(h_box5)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box4)
        """
        h_box6.addStretch()
        h_box6.addWidget(self.text3)
        h_box6.addStretch()
        v_box.addLayout(h_box6)
        """
        v_box.addStretch()
        
        self.window.setLayout(v_box)
        self.buton.clicked.connect(self.Process)
        self.window.show()

    def Process(self):
        gender=self.combo.currentText()
        if gender=="female":
            self.text3.setText("Kadın")
        else:
            self.text3.setText("Erkek")

app=QApplication(sys.argv)
window=Window()

app.setWindowIcon(QtGui.QIcon("sbanner.jpg"))
sys.exit(app.exec())
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys,requests,os
from bs4 import  BeautifulSoup

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.program()
    
    def program(self):
        self.windows=QWidget()
        os.chdir("C:\\Users\\asus\\Desktop\\Sample Picture")
        self.windows.setMaximumSize(800,720)
        self.windows.setMinimumSize(800,720)
        self.image=QLabel()
        self.image.setPixmap(QtGui.QPixmap("sbanner.jpg"))
        self.windows.setStyleSheet("background:black")
        self.windows.setWindowTitle("Body Mass Index ")
        self.text3=QLabel()
        self.text3.setFont(QtGui.QFont("Arial",20))
        self.text3.setStyleSheet("color:white")
        
        self.buton=QPushButton("Calculate")
        self.buton.setStyleSheet("background: green")
        self.buton.setShortcut("return")
        self.buton.setFont(QtGui.QFont('Arial',20,3))
        self.list=["Female","Male"]
        
        self.combo=QComboBox()
        self.combo.setStyleSheet("color:white")
        self.combo.addItems(self.list)
        self.text=QLabel("Your Weight: ")
        
        self.weight=QLineEdit()
        self.text2=QLabel("Your Height As Meter: ")
        self.text2.setFont(QtGui.QFont('Arial',20,4))
        self.text.setFont(QtGui.QFont('Arial',20,4))
        self.text2.setStyleSheet("color:blue")
        self.text.setStyleSheet("color:pink")
        self.weight.setStyleSheet("color: white")
        
        self.tall=QLineEdit()
        self.tall.setStyleSheet("color : white")
        self.tall.setFixedHeight(30)
        self.weight.setFixedHeight(30)
        self.weight.setFont(QtGui.QFont('Arial',20,3))
        self.tall.setFont(QtGui.QFont('Arial',20,3))
        
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
        h_box3.addWidget(self.tall)
        h_box3.addStretch()

        h_box2.addStretch()
        h_box2.addWidget(self.text)
        h_box2.addSpacing(130)
        h_box2.addWidget(self.weight)
        h_box2.addStretch()

        h_box4.addSpacing(580)
        h_box4.addWidget(self.buton)
        h_box4.addSpacing(580)
        
        h_box6=QHBoxLayout()
        h_box6.addStretch()
        h_box6.addWidget(self.text3)
        h_box6.addStretch()
        
        v_box.addStretch()
        v_box.addLayout(h_box5)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box4)
        v_box.addStretch()
        v_box.addLayout(h_box6)
        self.windows.setLayout(v_box)
        self.buton.clicked.connect(self.Process)
        self.windows.show()

    def Process(self):
      sender=self.windows.sender()
      if sender.text()=="Calculate":
       height=float(self.tall.text())
       weight=float(self.weight.text())
       print(height,weight,sep='\n')
       body_mass=weight/(height**2)
       print(body_mass)
       if body_mass<18:
           self.text3.setStyleSheet('color: red')
       elif body_mass>=18 and body_mass<25:
           self.text3.setStyleSheet('color: green')
       elif body_mass>=25 and body_mass<30:
           self.text3.setStyleSheet('color: yellow')
       elif body_mass>=30 and body_mass<35:
           self.text3.setStyleSheet('color: orange')
       else:
           self.text3.setStyleSheet('color: red')
           
       self.text3.setText(f"Your Body Mass: {str(body_mass)} Kg/M^2")

app=QApplication(sys.argv)
window=Window()

app.setWindowIcon(QtGui.QIcon("sbanner.jpg"))
sys.exit(app.exec_())
from datetime import datetime
from PyQt5.QtWidgets import QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QApplication,QMainWindow,QWidget,QLineEdit,QInputDialog,QFontDialog
import sys
from PyQt5.QtGui import QIcon

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.pencere=QWidget()
        self.pencere.setWindowTitle("Calculator")
       
        self.now=datetime.now()
        self.date=QLabel(str(datetime.strftime(self.now,format("TARİH:%d/%m/%Y SAAT: %H.%M.%S"))))
        self.one=QPushButton("1")
        
        self.two=QPushButton("2")
        
        self.three=QPushButton("3")
        
        self.plus=QPushButton("+")
        self.four=QPushButton("4")
        
        self.five=QPushButton("5")
        
        self.six=QPushButton("6")
        
        self.minus=QPushButton("-")
        self.seven=QPushButton("7")
        
        self.eight=QPushButton("8")
        
        self.nine=QPushButton("9")
        
        self.cross=QPushButton("x")
        self.clear=QPushButton("C")
        self.parantez=QPushButton("()")
        self.percent=QPushButton("%")
        self.division=QPushButton("/")
        self.icon=QPushButton("+/-")
        self.zero=QPushButton("0")
        self.mark=QPushButton(".")
        self.equal=QPushButton("=")
        self.hesap_alan=QLineEdit()
        self.hesap_alan2=QLineEdit()
        self.hesap_alan3=QLineEdit()
        self.hesap_alan4=QLineEdit()
        self.hesap_alan5=QLineEdit()
        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        h_box2=QHBoxLayout()
        h_box3=QHBoxLayout()
        h_box4=QHBoxLayout()
        h_box5=QHBoxLayout()
        v_box2=QVBoxLayout()
        h_box6=QHBoxLayout()
        h_box4.addWidget(self.clear)
        h_box4.addWidget(self.parantez)
        h_box4.addWidget(self.percent)
        h_box4.addWidget(self.division)
        v_box.addWidget(self.date)
        h_box6.addWidget(self.hesap_alan)
        h_box6.addWidget(self.hesap_alan2)
        h_box6.addWidget(self.hesap_alan3)
        h_box6.addWidget(self.hesap_alan4)
        h_box6.addWidget(self.hesap_alan5)
        h_box3.addWidget(self.seven)
        h_box3.addWidget(self.eight)
        h_box3.addWidget(self.nine)
        h_box3.addWidget(self.cross)
        h_box2.addWidget(self.four)
        h_box2.addWidget(self.five)
        h_box2.addWidget(self.six)
        h_box2.addWidget(self.minus)
        h_box.addWidget(self.one)
        h_box.addWidget(self.two)
        h_box.addWidget(self.three)
        h_box.addWidget(self.plus)
        h_box5.addWidget(self.icon)
        h_box5.addWidget(self.zero)
        h_box5.addWidget(self.mark)
        h_box5.addWidget(self.equal)
        v_box.addLayout(h_box6)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box5)
        v_box.addStretch()
        v_box2.addLayout(v_box)
        v_box.addStretch()
        self.pencere.setLayout(v_box2)
        self.one.clicked.connect(self.islem)
        self.two.clicked.connect(self.islem)
        self.three.clicked.connect(self.islem)
        self.four.clicked.connect(self.islem)
        self.five.clicked.connect(self.islem)
        self.six.clicked.connect(self.islem)
        self.seven.clicked.connect(self.islem)
        self.eight.clicked.connect(self.islem)
        self.nine.clicked.connect(self.islem)
        self.zero.clicked.connect(self.islem)
        self.minus.clicked.connect(self.islem2)
        self.icon.clicked.connect(self.islem2)
        self.plus.clicked.connect(self.islem2)
        self.division.clicked.connect(self.islem2)
        self.clear.clicked.connect(self.islem2)
        self.equal.clicked.connect(self.islem2)
        self.cross.clicked.connect(self.islem2)
        self.mark.clicked.connect(self.islem2)
        self.parantez.clicked.connect(self.islem2)
        self.percent.clicked.connect(self.islem2)
        self.pencere.setMaximumSize(500,250)
        self.pencere.show()
    def islem(self):
        sender=self.pencere.sender()
        if sender.text()=="1":
            
            self.hesap_alan.setText("1")
            if self.hesap_alan.text()!="\0":
              self.islem4()
        elif sender.text()=="2":
            self.hesap_alan.setText("2")
            if self.hesap_alan.text()!="\0":
              self.islem4()
        elif sender.text()=="3":
            self.hesap_alan.setText("3")
            if self.hesap_alan.text()!="\0":
              self.islem4()
        elif sender.text()=="4":
            self.hesap_alan.setText("4")
            if self.hesap_alan.text()!="\0":
             self.islem4()
        elif sender.text()=="5":
            self.hesap_alan.setText("5")
            if self.hesap_alan.text()!="\0":
             self.islem4()
        elif sender.text()=="6":
            self.hesap_alan.setText("6")
            if self.hesap_alan.text()!="\0":
               self.islem4()
        elif sender.text()=="7":
            self.hesap_alan.setText("7")
            if self.hesap_alan.text()!="\0":
              self.islem4()
        elif sender.text()=="8":
            self.hesap_alan.setText("8")
        
            if self.hesap_alan.text()!="\0":
              self.islem4()
        elif sender.text()=="9":
            self.hesap_alan.setPlaceholderText("9")
            if self.hesap_alan.text()!="\0":
              self.islem4()
        elif sender.text()=="0":
            self.hesap_alan.setText("0")
            if self.hesap_alan.text()!="\0":
              self.islem4()
        
       
    def islem2(self):
        sender=self.pencere.sender()
        if sender.text()=="+":
            self.hesap_alan2.setText("+")
            
        elif sender.text()=="/":
            self.hesap_alan2.setText("/")
            
        elif sender.text()=="-":
            self.hesap_alan2.setText("-")
            
        elif sender.text()=="x":
            self.hesap_alan2.setText("x")
            
        elif sender.text()=="+/-":
            self.hesap_alan2.setText("(-")
            
        elif sender.text()=="()":
            self.hesap_alan2.setText("()")
            
        elif sender.text()==".":
            self.hesap_alan2.setText(".")
            
        elif sender.text()=="C":
            self.hesap_alan.clear()
            self.hesap_alan2.clear()
            self.hesap_alan3.clear()
            self.hesap_alan4.clear()
            self.hesap_alan5.clear()
        elif sender.text()=="%":
            self.hesap_alan2.setText("%")
            
        elif sender.text()=="=":
            self.hesap_alan4.setText("=")
            self.islem3()
    def islem3(self):
        if self.hesap_alan2.text()=="+":
          hesap=int(self.hesap_alan.text())+int(self.hesap_alan3.text())
          self.hesap_alan5.setText(str(hesap))
        elif self.hesap_alan2.text()=="-":
          hesap=int(self.hesap_alan.text())-int(self.hesap_alan3.text())
          self.hesap_alan5.setText(str(hesap))
        elif self.hesap_alan2.text()=="x":
            hesap=int(self.hesap_alan.text())*int(self.hesap_alan3.text())
            self.hesap_alan5.setText(str(hesap))
        elif self.hesap_alan2.text()=="/":
            hesap=int(self.hesap_alan.text())/float(self.hesap_alan3.text())
            self.hesap_alan5.setText(str(hesap))
    def islem4(self):
        
        sender2=self.pencere.sender()
        
        if sender2.text()=="1":
            self.hesap_alan3.setText("1")
        elif sender2.text()=="2":
           self.hesap_alan3.setText("2")
            
        elif sender2.text()=="3":
            self.hesap_alan3.setText("3")
            
        elif sender2.text()=="4":
            self.hesap_alan3.setText("4")
        elif sender2.text()=="5":
            self.hesap_alan3.setText("5")
        elif sender2.text()=="6":
            self.hesap_alan3.setText("6")
           
        elif sender2.text()=="7":
            self.hesap_alan3.setText("7")

        elif sender2.text()=="8":
            self.hesap_alan3.setText("8")
            
        elif sender2.text()=="9":
            self.hesap_alan3.setText("9")
          
        elif sender2.text()=="0":
            self.hesap_alan3.setText("0")
         
        
app=QApplication(sys.argv)
app.setWindowIcon(QIcon("Calculator.jpg"))
window=Window()
sys.exit(app.exec())

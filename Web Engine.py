import pywhatkit as py,sys
from PyQt5 import QtWidgets,QtGui


class window:
    
    def __init__(self):
        self.program()
    def program(self):
     self.main_window=QtWidgets.QWidget()
     self.main_window.setWindowTitle("Web Engine")
     self.main_window.setStyleSheet("background: lightblue")
     self.text=QtWidgets.QLabel("What Do You Want to Search: ")
     self.text.setFont(QtGui.QFont("Arial",24,4))
     self.text_field=QtWidgets.QLineEdit()
     self.text_field.setFont(QtGui.QFont("Arial",24,4))
     self.buton=QtWidgets.QPushButton("Search")
     self.buton.setFont(QtGui.QFont("Arial",20,4))
     self.text_field.setStyleSheet("background :White")
     self.buton.setStyleSheet("background: green")
     self.buton.setShortcut("Return")
     v_box=QtWidgets.QVBoxLayout()
     v_box.addStretch()
     v_box.addWidget(self.text)
     v_box.addSpacing(20)
     v_box.addWidget(self.text_field)
     v_box.addSpacing(50)
     v_box.addWidget(self.buton)
     v_box.addStretch()
     h_box=QtWidgets.QHBoxLayout()
     h_box.addStretch()
     h_box.addLayout(v_box)
     h_box.addStretch()
     self.main_window.setLayout(h_box)
     self.buton.clicked.connect(self.search)
     self.main_window.setMaximumSize(self.main_window.size())
     self.main_window.show()
     
    def search(self):
         py.search(self.text_field.text())
         
     
app=QtWidgets.QApplication(sys.argv)

Window=window()
app.setWindowIcon(QtGui.QIcon("C:/Users/asus/Desktop/Sample Picture/Google.png"))
sys.exit(app.exec())
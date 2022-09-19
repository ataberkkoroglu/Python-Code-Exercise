import os
import sys
from PyQt5.QtWidgets import QFileDialog,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QApplication,QTextEdit
from PyQt5.QtWidgets import QMainWindow,qApp,QAction
class Notepad(QWidget):
    def __init__(self):
       super().__init__()
       self.program()
    def program(self):
        self.window=QWidget()
        self.window.setWindowTitle("NotePad")
        self.yazı_alanı=QTextEdit()
        self.buton1=QPushButton("Delete")
        self.buton2=QPushButton("Open")
        self.buton3=QPushButton("Save")
        h_box=QHBoxLayout()
         
        h_box.addWidget(self.buton1)
        h_box.addWidget(self.buton2)
        h_box.addWidget(self.buton3)
        v_box=QVBoxLayout()
        v_box.addWidget(self.yazı_alanı)
        v_box.addLayout(h_box)
        self.window.setLayout(v_box)
        self.buton1.clicked.connect(self.process)
        self.buton2.clicked.connect(self.process)
        self.buton2.clicked.connect(self.process)
    def process(self):
        sender=self.window.sender()

        if sender.text() =="Delete":
            self.yazı_alanı.clear()
        elif sender.text()=="Open":
            dosya_ismi= QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("ataberk köroğlu"))
            with open(dosya_ismi[0],"r") as file:
                self.yazı_alanı.setText(file.read())
        elif sender.text()=="Save":
            dosya_ismi2= QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("ataberk köroğlu"))
            with open(dosya_ismi2[0],"w") as file2:
                file2.write(self.yazı_alanı.toPlainText())
class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere=Notepad()
        self.setCentralWidget(self.pencere)
        self.menu_olustur()
    def menu_olustur(self):
        menubar=self.menuBar()
        dosya=menubar.addMenu("Dosya")
        dosya_ac=QAction("Open File",self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet=QAction("Save File",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        temizle=QAction("Delete",self)
        temizle.setShortcut("Ctrl+D")
        cıkıs=QAction("Exit",self)
        cıkıs.setShortcut("Ctrl+Q")
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cıkıs)
        dosya.triggered.connect(self.response)
        self.setWindowTitle("Text Editor")
        self.show()

    def response(self,action):
      if action.text()=="Save File":
        print("Button of Save File Was Pressed.")
      elif action.text()=="Open File":
        print("Button of Open File Was Pressed.")
      elif action.text()=="Delete":
        print("Button of Delete Was Pressed.")
      elif action.text()=="Exit":
        qApp.quit()
app=QApplication(sys.argv)
Menu=menu()
sys.exit(app.exec())

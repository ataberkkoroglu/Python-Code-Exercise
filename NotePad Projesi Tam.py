from datetime import datetime
import sys
import os 
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QVBoxLayout,qApp,QApplication,QWidget,QFileDialog,QLabel,QHBoxLayout
import time
class pencere (QMainWindow):
    def __init__(self):
        super().__init__()
        self.program()
    def program(self):
      self.pencere=QWidget()
      #self.pencere.setStyleSheet("Background-color:black")
      menubar=self.menuBar()
      self.dosya=menubar.addMenu("File")
      self.edit=menubar.addMenu("Edit")
      self.yazı_alanı=QTextEdit()
      self.now=datetime.now()
      self.cıkıs=menubar.addMenu("Exit")
      self.time=QLabel(str(datetime.strftime(self.now,format("%d-%m-%Y/ %H-%M-%S"))))
      self.alt=QLabel("       %100        |  Windows(CRLF)  | UTF-8 ")
      self.v_box=QVBoxLayout()
      self.h_box=QHBoxLayout()
      self.v_box.addWidget(self.yazı_alanı)
      self.h_box.addWidget(self.time)
      self.h_box.addStretch()
      self.h_box.addWidget(self.alt)
      self.v_box.addLayout(self.h_box)
      self.pencere.setLayout(self.v_box)
      self.setCentralWidget(self.pencere)
      self.dosya_ac=QAction("Open File",self)
      self.dosya_ac.setShortcut("Ctrl+O")
      self.dosya.addAction(self.dosya_ac)
      self.dosya_kaydet=QAction("Save File",self)
      self.dosya_kaydet.setShortcut("Ctrl+S")
      self.dosya.addAction(self.dosya_kaydet)
      self.temizle=QAction("Delete",self)
      self.temizle.setShortcut("Ctrl+D")
      self.edit.addAction(self.temizle)
      self.cıkıs2=QAction("Exit",self)
      self.cıkıs2.setShortcut("Ctrl+Q")
      self.cıkıs.addAction(self.cıkıs2)
      self.setWindowTitle("NotePad")
      self.print=QAction("Print",self)
      self.print.setShortcut("Ctrl+P")
      self.edit.addAction(self.print)
      self.dosya.triggered.connect(self.response)
      self.edit.triggered.connect(self.response)
      self.cıkıs.triggered.connect(self.response)
            
      self.show()

    def response(self,action):
        if action.text()=="Open File":
            dosya_ismi= QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("ataberk köroğlu"))
            with open(dosya_ismi[0],"r") as file:
                self.yazı_alanı.setText(file.read())
        elif action.text()=="Save File":
            dosya_ismi2= QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("ataberk köroğlu"))
            self.sayac=0
            while (True):
                 if(file.tell()%86==0):
                  self.sayac +=1
                 else:
                    break
            self.alt3.setText(str(self.sayac))
            self.alt2.setText(str (file.tell())-str(self.sayac*86))
            with open(dosya_ismi2[0],"w") as file2:
                file2.write(self.yazı_alanı.toPlainText())
        elif action.text()=="Delete":
            self.yazı_alanı.clear()
        elif action.text()=="Exit":
            qApp.quit()
        elif action.text()=="Yakınlaştır":
            pass
        elif action.text()=="Uzaklaştır":
            pass
        elif action.text()=="Print":
            print("Your Essay is being Printed...")
            time.sleep(5)
            print("Your Essay was Printed.")
app=QApplication(sys.argv)
Pencere=pencere()
sys.exit(app.exec())
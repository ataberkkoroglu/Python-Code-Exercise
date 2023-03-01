from PyQt5 import QtWidgets,QtGui
import sys,sqlite3,time,webbrowser,instaloader
class pencere():
    def __init__(self):
     super().__init__()
     
     self.init_ui()
     self.baglantı_olustur()
     
    def baglantı_olustur(self):
      con=sqlite3.connect("information.db")
      cursor=con.cursor()
      cursor.execute("Create Table IF NOT Exists Member(Username TEXT,Password TEXT) ")
      con.commit()
    
 
    def init_ui(self):
      self.window=QtWidgets.QWidget()
      self.window.setWindowTitle("Instagram")
      self.kullanici_girisi=QtWidgets.QLineEdit()
      self.kullanici_girisi.setFixedHeight(20)
      self.image=QtWidgets.QLabel()
      self.image.setPixmap(QtGui.QPixmap("Instagram.jpg"))
      self.kullanici_sifresi=QtWidgets.QLineEdit()
      self.kullanici_sifresi.setFixedHeight(20)
      self.kullanici_sifresi.setEchoMode(QtWidgets.QLineEdit.Password)
      self.sifre_unutma=QtWidgets.QPushButton("Did You Forget Your Password?If Your Answer is Yes, Click here")
      self.login=QtWidgets.QPushButton("Login")
      self.login.setShortcut("Return")
      self.v_box=QtWidgets.QVBoxLayout()
      self.yazi=QtWidgets.QLabel(self.window)
      self.v_box.addStretch()
      self.v_box.addWidget(self.image)
      self.yazi.setText("Username")
      self.v_box.addWidget(self.yazi)
      self.v_box.addWidget(self.kullanici_girisi)
      self.yazi2=QtWidgets.QLabel(self.window)
      self.yazi2.setText("Password")
      self.v_box.addWidget(self.yazi2)
      self.v_box.addWidget(self.kullanici_sifresi)
      
      self.v_box.addWidget(self.login)
      self.v_box.addWidget(self.sifre_unutma)
      self.v_box.addStretch()
      self.h_box=QtWidgets.QHBoxLayout()
      self.h_box.addStretch()
      self.h_box.addLayout(self.v_box)
      self.h_box.addStretch()
      self.window.setLayout(self.h_box)
      
      self.h_box.addLayout(self.v_box)
      self.window.setLayout(self.h_box)
      self.window.show()
      self.login.clicked.connect(self.process)
      self.sifre_unutma.clicked.connect(self.process)
    def process(self):
      sender=self.window.sender()
      if sender.text()=="Login":
         con=sqlite3.connect("information.db")
         cursor=con.cursor()
         cursor.execute("Select * From Member Where Username=? and Password=?",(self.kullanici_girisi.text(),self.kullanici_sifresi.text()))
         result=cursor.fetchone()
         if result!=None:
          etiket5=QtWidgets.QLabel(self.window)
          etiket5.setText("Program is being logged in...")
          self.window.close()
          
         else:
           etiket4=QtWidgets.QLabel(self.window)
           etiket4.setText("Write Wrong Value")

         self.window2=QtWidgets.QWidget()
         self.window2.setMinimumSize(250,250)
         self.v_box3=QtWidgets.QVBoxLayout()
         self.v_box3.addStretch()
         self.v_box3.addWidget(self.image)
         self.yazi5=QtWidgets.QLabel()
         self.yazi5.setText("Welcome To Application...")
         self.v_box3.addWidget(self.yazi5)
         self.v_box3.addStretch()
         self.window.close()
         self.window2.show()
         
         webbrowser.Chrome("C:/Program Files/Google/Chrome/Application/chrome.exe")
         webbrowser.open_new_tab("https://www.instagram.com/")
        
         self.window2.close()
      else:
        self.window.close()
        self.window3=QtWidgets.QWidget()
        self.yazı3=QtWidgets.QLabel(self.window3)
        con=sqlite3.connect("information.db")
        cursor=con.cursor()
      
        if self.kullanici_girisi.text()=="":
         self.username_text=QtWidgets.QLabel(self.window3)
         self.username_text.setText("Username")
         self.username=QtWidgets.QLineEdit()
         self.yazı4=QtWidgets.QLabel(self.window3)
         self.yazı4.setText("New Password")
         self.yeni_sifre=QtWidgets.QLineEdit()
         self.yeni_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
         self.buton=QtWidgets.QPushButton("Save Changes")
         self.buton.setShortcut("Return")
         self.v_box2=QtWidgets.QVBoxLayout()
         self.v_box2.addStretch()
         self.v_box2.addWidget(self.image)
         self.v_box2.addWidget(self.username_text)
         self.v_box2.addWidget(self.username)
         self.v_box2.addWidget(self.yazı3)
         self.v_box2.addWidget(self.yazı4)
         self.v_box2.addWidget(self.yeni_sifre)
         self.v_box2.addWidget(self.buton)
         self.v_box2.addStretch()
         self.window3.setLayout(self.v_box2)
         self.buton.clicked.connect(self.Change)
         self.window3.show()
         
        else:
         self.text=QtWidgets.QLabel()
         self.yazı4=QtWidgets.QLabel(self.window3)
         self.yazı4.setText("New Password")
         self.yeni_sifre=QtWidgets.QLineEdit()
         self.yeni_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
         self.buton=QtWidgets.QPushButton("Save Changes")
         self.buton.setShortcut("Return")
         self.v_box2=QtWidgets.QVBoxLayout()
         self.v_box2.addWidget(self.yazı3)
         self.v_box2.addWidget(self.yazı4)
         self.v_box2.addWidget(self.yeni_sifre)
         self.v_box2.addWidget(self.buton)
         self.v_box2.addWidget(self.text)
         self.v_box2.addStretch()
         self.window3.setLayout(self.v_box2)
         self.buton.clicked.connect(self.Change2)
         self.window3.show()
         
    def Change(self):
      con=sqlite3.connect("information.db")
      cursor=con.cursor()
      if self.username.text()!="":
       cursor.execute("Select * From Member Where Username=? ",(self.username.text(),))
       result=cursor.fetchall()
       if result!=None:
        cursor.execute("Update Member set Password=? Where Username=?",(self.yeni_sifre.text(),self.username.text()))
        con.commit()
        self.init_ui()
        self.window3.close()
      else:
        self.text.setText("There is No Like Username...")
        
        
    def Change2(self):
      con=sqlite3.connect("information.db")
      cursor=con.cursor()
      cursor.execute("Select * From Member Where Username=? ",(self.kullanici_girisi.text(),))
      result=cursor.fetchall()
      if result!=None:
        cursor.execute("Update Member set Password=? Where Username=?",(self.yeni_sifre.text(),self.kullanici_girisi.text()))
        con.commit()
        self.init_ui()
        self.window3.close()
      else:
        self.text.setText("There is No Like Username...")
        
App=QtWidgets.QApplication(sys.argv)
App.setWindowIcon(QtGui.QIcon("Instagram2.jpg"))
Pencere=pencere()
sys.exit(App.exec())
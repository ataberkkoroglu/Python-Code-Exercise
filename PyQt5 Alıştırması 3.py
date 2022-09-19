from PyQt5 import QtWidgets,QtGui
import sys
import sqlite3
class pencere():
    def __init__(self):
     super().__init__()
     self.init_ui()
     self.baglantı_olustur()
    def baglantı_olustur(self):
      con=sqlite3.connect("bilgi.db")
      self.cursor=con.cursor()
      self.cursor.execute("Create Table IF NOT Exists üyeler(kullanıcı_adı TEXT,Kullanıcı_parola TEXT) ")
      con.commit()
    def init_ui(self):
      self.window=QtWidgets.QWidget()
      self.window.setWindowTitle("Instagram")
      self.kullanici_girisi=QtWidgets.QLineEdit()
      self.kullanici_sifresi=QtWidgets.QLineEdit()
      self.kullanici_sifresi.setEchoMode(QtWidgets.QLineEdit.Password)
      self.sifre_unutma=QtWidgets.QPushButton("Şifreyi Unuttunuz Mu? Evet ise Tıklayın")
      self.login=QtWidgets.QPushButton("Giriş")
      self.v_box=QtWidgets.QVBoxLayout()
      self.yazi=QtWidgets.QLabel(self.window)
      self.v_box.addStretch()
      self.yazi.setText("Kullanıcı Adı")
      self.v_box.addWidget(self.yazi)
      self.v_box.addWidget(self.kullanici_girisi)
      self.yazi2=QtWidgets.QLabel(self.window)
      self.yazi2.setText("Kullanıcı Şifresi")
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
      if sender.text()=="Giriş":
        while True:
         kullanıcı_adı=self.kullanici_girisi
         kullanıcı_parolası=self.kullanici_sifresi
         self.cursor.execute("Select * From üyeler Where kullanıcı_adı=? and kullanıcı_parola=? ",(kullanıcı_adı,kullanıcı_parolası,))
         data=self.cursor.fetchall()
         if len(data)!=0:
          etiket5=QtWidgets.QLabel(self.window)
          etiket5.setText("Programa Giris Yapiyorsunuz...")
          self.window.close()
          break
         else:
           etiket4=QtWidgets.QLabel(self.window)
           etiket4.setText("Yanlış Değer Girdiniz")

         self.window2=QtWidgets.QWidget()
         self.yazi5=QtWidgets.QLabel(self.window2)
         self.yazi5.setText("Uygulamaya Hoşgeldiniz...")
         self.window2.show()
      else:
        self.window.close()
        self.window3=QtWidgets.QWidget()
        self.yazı3=QtWidgets.QLabel(self.window3)
        self.yazı3.setText("Eski Şifreniz")
        self.eski_sifre=QtWidgets.QLineEdit()
        self.yazı4=QtWidgets.QLabel(self.window3)
        self.yazı4.setText("Yeni Şifreniz")
        self.eski_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.yeni_sifre=QtWidgets.QLineEdit()
        self.yeni_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buton=QtWidgets.QPushButton("Değişikliği Kaydet")
        self.v_box2=QtWidgets.QVBoxLayout()
        self.v_box2.addWidget(self.yazı3)
        self.v_box2.addWidget(self.eski_sifre)
        self.v_box2.addWidget(self.yazı4)
        self.v_box2.addWidget(self.yeni_sifre)
        self.v_box2.addWidget(self.buton)
        self.v_box2.addStretch()
        self.window3.setLayout(self.v_box2)
        self.yazı4=self.yazı3
        self.window3.show()
App=QtWidgets.QApplication(sys.argv)
Pencere=pencere()
sys.exit(App.exec())
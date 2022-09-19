from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from PyQt5.QtWidgets import QWidget,QMainWindow,QPushButton,QTextEdit,QLineEdit,QLabel,QHBoxLayout,QVBoxLayout,QAction,QApplication,QFileDialog,QCheckBox,qApp
from PyQt5 import QtGui
import time,os
class Pencere(QMainWindow):
    a=0
    def __init__(self):
        super().__init__()
        self.giris()
        self.init_ui()    
    def init_ui(self):     
        self.pencere=QWidget()
        self.pencere.setWindowTitle("Mail Gönderme")
        self.kim=QLineEdit()
        self.kim2=QLabel("Gönderici")
        self.kime=QLineEdit()
        menubar=self.menuBar()
        self.exit=menubar.addMenu("Çıkış")
        self.cıkıs_yap=QAction(self.exit)
        self.cıkıs_yap.setShortcut("Ctrl+Q")
        self.exit.addAction(self.cıkıs_yap)
        self.kime2=QLabel("Alıcı")
        self.subject=QLineEdit()
        self.subject2=QLabel("Konu:")
        self.now=datetime.now()
        self.time=QLabel(str(datetime.strftime(self.now,format("TARİH:%d/%m/%Y SAAT: %H.%M.%S"))))
        self.yazı_alanı=QTextEdit()
        self.yazı_alanı2=QLabel("Mail")
        self.buton=QPushButton("Gönder")
        self.buton2=QPushButton("Taslak Olarak Kaydet")
        self.buton3=QPushButton("Sil")
        self.buton3.setShortcut("Ctrl+D")
        self.buton.setShortcut("Ctrl+M")
        self.buton2.setShortcut("Ctrl+S")
        self.buton5=QPushButton("Aç")
        self.buton5.setShortcut("Ctrl+O")
        font=QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.yazı_alanı.setFont(font)
        self.yazı=QLabel()
        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        v_box.addWidget(self.time)
        v_box.addWidget(self.kim2)
        v_box.addWidget(self.kim)
        v_box.addWidget(self.kime2)
        v_box.addWidget(self.kime)
        v_box.addWidget(self.subject2)
        v_box.addWidget(self.subject)
        v_box.addWidget(self.yazı_alanı2)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.yazı)
        h_box.addWidget(self.buton)
        h_box.addWidget(self.buton2)
        h_box.addWidget(self.buton5)
        h_box.addWidget(self.buton3)
        v_box.addLayout(h_box)
        self.pencere.setLayout(v_box)
        self.pencere.setMinimumSize(250,250)
        self.buton.clicked.connect(self.response)
        self.buton2.clicked.connect(self.response)
        self.buton3.clicked.connect(self.response)
        self.buton5.clicked.connect(self.response)
        #self.pencere.show()
    def giris(self):
         self.pencere2=QWidget()
         self.pencere2.setWindowTitle("Gmail")
         self.kullanıcı_adı=QLabel("Kullanıcı Adınız")
         self.kullanıcı_sifresi=QLabel("Kullanıcı Şifresi")
         self.remember=QCheckBox("Beni Hatırla")
         self.password=(QLineEdit())
         self.password.setEchoMode(QLineEdit.Password)
         self.kullanıcı_adı2=QLineEdit()
         self.etiket2=QLabel()
         self.etiket2.setPixmap(QtGui.QPixmap("Gmail2.jpg"))
         self.buton4=QPushButton("Giriş Yap")
         self.buton4.setShortcut("Ctrl+M")
         self_unutma=QPushButton("Şifreyi Unuttunuz Mu?")
         v_box=QVBoxLayout()
         h_box=QHBoxLayout()
         v_box.addStretch()
         v_box.addWidget(self.etiket2)
         v_box.addWidget(self.kullanıcı_adı)
         v_box.addWidget(self.kullanıcı_adı2)
         v_box.addWidget(self.kullanıcı_sifresi)
         v_box.addWidget(self.password)
         v_box.addWidget(self.remember)
         v_box.addWidget(self.buton4)
         v_box.addWidget(self_unutma)
         v_box.addStretch()
         h_box.addStretch()
         h_box.addLayout(v_box)
         h_box.addStretch()
         self.pencere2.setLayout(h_box)
         self.remember.clicked.connect(self.check)
         self.buton4.clicked.connect(self.check)
         self_unutma.clicked.connect(self.windows)
         self.pencere2.show()
    def check(self,x):
        sender=self.pencere2.sender()
        self.parola="2606Atam"
        self.ad="ataberkkoroglu02@gmail.com"
        if sender.text()=="Giriş Yap":
           #if str(self.kullanıcı_adı2)==self.ad and str(self.password)==self.parola:
                time.sleep(1)
                self.pencere2.close()
                self.init_ui()
                self.pencere.show()
                if self.remember.isChecked():
                    pass             
        elif sender.text()=="Şifreyi Unuttunuz Mu?":
         if(not str(self.password))in x.items:
           self.windows()
           self.parola.__dir__()
        elif sender.text()=="Kaydet":
             self.parola=self.yeni_sifre2
             
             print("Kaydedildi")
             self.pencere3.close()
             self.giris()
        elif sender.text()=="Sil":
            self.yeni_sifre2.clear()         
                   
    def windows(self):
        self.pencere2.close()
        self.pencere3=QWidget()
        self.yeni_sifre=QLabel("Yeni Şifre")
        self.yeni_sifre2=QLineEdit()
        self.yeni_sifre2.setEchoMode(QLineEdit.Password)
        self.kaydet=QPushButton("Kaydet")
        self.parola=self.yeni_sifre2
        self.sil=QPushButton("Sil")
        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.yeni_sifre)
        v_box.addWidget(self.yeni_sifre2)
        v_box.addWidget(self.kaydet)
        v_box.addWidget(self.sil)
        v_box.addStretch()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.pencere3.setLayout(h_box)
        self.kaydet.clicked.connect(self.check)
        self.sil.clicked.connect(self.check)
        self.pencere3.show()
    def control(self):
        self.ad=('ataberkkoroglu02@gmail.com')
        self.parola="2606Atam"
    def response(self):
        sender=self.pencere.sender()
        if sender.text()=="Gönder":
            mesaj=MIMEMultipart()
            mesaj["From"]=self.kim
            mesaj["to"]=self.kime
            mesaj["Subject"]=self.subject
            yazi=self.yazı_alanı.toPlainText()
            mesaj_govdesi=MIMEText(yazi,"plain")
            mesaj.attach(mesaj_govdesi)
            try:
             mail= smtplib.SMTP("stmp.gmail.com",587)
             mail.ehlo()
             mail.starttls()
             mail.login(self.kullanıcı_adı2,self.password)
             mail.sendmail(mesaj["From"],mesaj["To"],mesaj["Subject"],mesaj.as_string())
             self.yazı.setText("Mailiniz Başarıyla Gönderildi.")
             mail.close()
            except:
              self.yazı.setText("Mailiniz Gönderilemedi")
        elif sender.text()=="Taslak Olarak Kaydet":
            dosya_ismi2= QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("ataberk köroğlu"))
            with open(dosya_ismi2[0],"w") as file2:
                file2.write("Gönderici:\t")
                file2.write(self.kim.text())
                file2.write("\n")
                file2.write("Alıcı:\t")
                file2.write(self.kime.text())
                file2.write("\n")
                file2.write("Konu:\t")
                file2.write(self.subject.text())
                file2.write("\n")
                file2.write("Yazı:\t")
                file2.write(self.yazı_alanı.toPlainText())
                file2.close()
        elif sender.text()=="Sil":
            self.yazı_alanı.clear()
            self.subject.clear()
            self.kime.clear()
            self.kim.clear()
        elif sender.text()=="Aç":
            dosya_ismi= QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("ataberk köroğlu"))
            with open(dosya_ismi[0],"r+") as file:
               self.kim.setText(file.readline())
               self.kime.setText(file.readline())
               self.subject.setText(file.readline())
               self.yazı_alanı.setText(file.readline())
               file.close()

app=QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("Gmail3.svg"))
pencere=Pencere()
sys.exit(app.exec())
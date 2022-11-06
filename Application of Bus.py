import requests,time,sys,os,webbrowser
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from bs4 import BeautifulSoup
from datetime import datetime
class Bus(QMainWindow):

  def __init__(self):

    self.program()
  
  def program(self):

    self.pencere=QWidget()
    self.pencere.setWindowTitle("Eshot")
    self.list=QComboBox()
    response=requests.get("https://www.eshot.gov.tr/")
    content=response.content
    soup=BeautifulSoup(content,"html.parser")
    x=list()
    for i in soup.find("ul",{"class":"selector"}):
        if i.text!=None:
          x.append(i.text)
          
    self.list.addItems(x)
    os.chdir("C:\\Users\\asus\\Desktop\\Sample Picture")
    self.date=QLabel(str(time.ctime(datetime.timestamp(datetime.now()))))
    self.date.setFont(QtGui.QFont("Arial",20))
    self.image=QLabel()
    self.image.setPixmap(QtGui.QPixmap("Eshot.jpg"))
    self.button=QPushButton("Show Informations")
    self.text=QLabel("")
    v_box=QVBoxLayout()
    h_box=QHBoxLayout()
    v_box.addStretch()
    v_box.addWidget(self.date)
    v_box.addWidget(self.image)
    v_box.addWidget(self.list)
    v_box.addWidget(self.button)
    v_box.addWidget(self.text)
    v_box.addStretch()
    h_box.addStretch()
    h_box.addLayout(v_box)
    h_box.addStretch()
    self.pencere.setLayout(h_box)
    self.button.clicked.connect(self.Information)
    self.pencere.show()
 
  def Information(self):
    sender=self.pencere.sender()
    if sender.text()=="Show Informations":
     webbrowser.open_new("https://www.eshot.gov.tr/")

app=QApplication(sys.argv)
bus=Bus()
app.setWindowIcon(QtGui.QIcon("Eshot.jpg"))
sys.exit((app.exec()))
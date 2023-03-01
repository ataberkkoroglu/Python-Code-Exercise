from PyQt5.QtWidgets import QComboBox,QPushButton,QApplication,QLabel,QVBoxLayout,QHBoxLayout,QMainWindow,QWidget,QTextEdit
from PyQt5.QtGui import QFont,QIcon
import sys,time,os,deep_translator,sqlite3
from datetime import datetime
from gtts import gTTS

os.chdir("C:/Users/asus/Desktop/Sample Picture")
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sql()
        
        self.program2()

    def sql(self):
         con=sqlite3.connect("Translate.db")
         cursor=con.cursor()
         try:
           cursor.execute("Create Table translate(english INT,turkish INT,french INT,spanish INT,arabic INT,german INT,italian INT,greek INT,russian INT,japanese INT,korean INT,chinese INT)")
           con.commit()
           cursor.execute("Insert Into translate values(?,?,?,?,?,?,?,?,?,?,?,?)",(0,0,0,0,0,0,0,0,0,0,0,0))
           con.commit()   
           cursor.execute("Select * From translate")
           self.count=cursor.fetchone()
         
         except:
            cursor.execute("Select * From translate")
            self.count=cursor.fetchone()
          
 
            
    def program2(self):
        
        self.pencere=QWidget()
        self.Language1=QComboBox()
        self.Language2=QComboBox()
        self.line=QLabel()
        self.pencere.setWindowTitle("Google Translate")
        self.time=QLabel(str(datetime.strftime(datetime.now(),"%H:%M:%S %D")))
        self.time.setFont(QFont("Arial",20,weight=QFont.Normal,italic=True))
        Language=[]
        ceviri=deep_translator.GoogleTranslator()
        Language.extend(ceviri.get_supported_languages())
       
        self.Language1.addItems(Language)
        self.language=Language.copy()
        self.Language2.addItems(self.language)
        self.pencere.setStyleSheet("background-color: lightblue")
        
        self.Text3=QLabel("Welcome To Google Translate")
        self.Text3.setFont(QFont("Arial",48,QFont.Bold))
        self.change=QPushButton("Change")
        self.clear=QPushButton("Clear")
        self.Text1=QTextEdit()
        self.Text2=QTextEdit()
        self.original=QLabel("Original Text:")
        self.original.setFont(QFont("Arial",11,weight=QFont.Bold,italic=False))
        self.translated=QLabel("Translated Text:")
        self.translated.setFont(QFont("Arial",11,weight=QFont.Bold,italic=False))
        self.buton=QPushButton("Translate")
        self.buton.setShortcut("Return")
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.h_box2=QHBoxLayout()
        self.h_box3=QHBoxLayout()
        self.h_box4=QHBoxLayout()
        self.h_box5=QHBoxLayout()
        self.h_box5.addStretch()
        self.h_box5.addWidget(self.Text3)
        self.h_box5.addStretch()
        self.v_box.addLayout(self.h_box5)
        self.v_box.addSpacing(30)
        self.h_box4.addStretch()
        self.h_box4.addWidget(self.time)
        self.h_box4.addStretch()
        self.v_box.addLayout(self.h_box4)
        self.v_box.addSpacing(10)
        self.h_box3.addWidget(self.Language1)
        self.h_box3.addSpacing(10)
        self.h_box3.addWidget(self.Language2)
        self.h_box.addWidget(self.original)
        self.h_box.addSpacing(18)
        self.h_box.addWidget(self.Text1)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addSpacing(10)
        self.v_box.addLayout(self.h_box)
        self.v_box.addSpacing(10)
        self.h_box2.addWidget(self.translated)
        self.h_box2.addWidget(self.Text2)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addSpacing(10)
        self.v_box.addWidget(self.buton)
        self.v_box.addSpacing(5)
        self.v_box.addWidget(self.clear)
        self.v_box.addSpacing(5)
        self.v_box.addWidget(self.change)
        self.v_box.addSpacing(5)
        self.v_box.addWidget(self.line)
        self.pencere.setLayout(self.v_box)
        
        self.buton.clicked.connect(self.Translate)
        self.clear.clicked.connect(self.Translate)
        self.change.clicked.connect(self.Translate)
        self.pencere.show()
        
    def Translate(self):
        sender=self.sender()
        if sender.text()=="Translate":
            self.line.setFont(QFont("Arial",15,QFont.Normal))
            
            ceviri=deep_translator.GoogleTranslator(source=str(self.Language1.currentText()), target=str(self.Language2.currentText()))
            text4=self.Text1.toPlainText()
            
            sample=ceviri.translate(text4)
    
            self.Text2.setText(sample)
            #self.Text2.setText("Your Process Couldn't Complete Successfully.")
            
            if self.Text2.toPlainText()!='':
                b=0
                d=0
                a=self.Language2.currentText()
                c=self.Language1.currentText()
                language1={"english":'en',"turkish":'tr',"french":'fr',"spanish":"es","arabic":"ar","german":"de","italian":"it","greek":"el","russian":"ru","japanese":"ja","korean":"ko","chinese (traditional)":"zh-cht"}
                for i,e in language1.items():
                    if a==i:
                        break
                    else:
                        b +=1
                for k,j in language1.items():
                    if c==k:
                        break
                    else:
                        d +=1
                    
                con=sqlite3.connect("Translate.db")
                cursor=con.cursor()
                cursor.execute("Select * From translate")
                self.count=cursor.fetchone()
               
                audio2=f'Original Text {c}{self.count[b]}.mp3'
                audio=f'translated Text {a}{self.count[b]}.mp3'
            
                cursor.execute(f"Update translate set {a}=? Where {a}=?",(self.count[b]+1,self.count[b]))
                con.commit()                    
                language=self.Language2.currentText()
                language2=self.Language1.currentText()
                
                if language in language1.keys():
                    sp=gTTS(text=self.Text2.toPlainText(),lang=language1[language],slow=False)
                    sp.save(audio)
                if language2 in language1.keys():
                    sp2=gTTS(text=self.Text1.toPlainText(),lang=language1[language2],slow=False)
                    sp2.save(audio2)
                
                self.line.setText("Process Time: {}".format(time.process_time()))
            else:
                self.line.setText("Process Time: 0")
                
        elif sender.text()=="Clear":
            self.choice=self.Language1.currentText()
            self.Language1.setCurrentText(str(self.Language2.currentText()))
            self.Language2.setCurrentText(str(self.choice))
            self.line.clear()
            self.Text1.clear()
            self.Text2.clear()
            
            #self.Language1.setCurrentText("English")
            #self.Language2.setCurrentText("Turkish")
        else:
            self.line.clear()
            self.Text=self.Text1.toPlainText()
            self.Text1.setText(str(self.Text2.toPlainText()))
            self.Text2.setText(self.Text)
            self.choice=self.Language1.currentText()
            self.Language1.setCurrentText(str(self.Language2.currentText()))
            self.Language2.setCurrentText(str(self.choice))
            self.line.setText("Process Time: {}".format(time.process_time()))
        
        


app=QApplication(sys.argv)
app.setWindowIcon(QIcon("Google Translate.png"))
window=Window()
sys.exit(app.exec())
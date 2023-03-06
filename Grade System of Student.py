import pandas as pd,sys,sqlite3
from PyQt5 import QtGui,QtWidgets
from sqlalchemy  import create_engine

class Window:
    def __init__(self):
        self.Program()
              
    def Program(self):
        
        self.main_window=QtWidgets.QMainWindow()
        self.window=QtWidgets.QWidget()
        
        
        self.main_window.setWindowTitle("Program")
        self.window.setStyleSheet("background: lightblack")
       
        self.label1=QtWidgets.QLabel("Name Of Lesson : ")
        self.label1.setFont(QtGui.QFont('Arial',18,4))
        self.label2=QtWidgets.QLabel("Name & Surname Of Student : ")
        self.label2.setFont(QtGui.QFont('Arial',18,4))
        self.label3=QtWidgets.QLabel("Grade Of Student : ")
        self.label3.setFont(QtGui.QFont('Arial',18,4))
        self.label1.setStyleSheet(" color: white")
        self.label2.setStyleSheet(" color: white")
        self.label3.setStyleSheet(" color: white")
        self.img=QtWidgets.QLabel()
        self.img.setPixmap(QtGui.QPixmap("C:\\Users\\asus\\Desktop\\Sample Picture\\Student.png"))
        self.Lesson=QtWidgets.QLineEdit()
        self.Lesson.setFont(QtGui.QFont('Arial',18,4))
        self.Lesson.setStyleSheet(" color: white")
        self.Student=QtWidgets.QLineEdit()
        self.Student.setFont(QtGui.QFont('Arial',18,4))
        self.Student.setStyleSheet(" color: white")
        self.Grade=QtWidgets.QLineEdit()
        self.Grade.setFont(QtGui.QFont('Arial',18,4))
        self.Grade.setStyleSheet(" color: white; alpha=4")
        self.buton=QtWidgets.QPushButton("Add to Your List")
        self.buton.setFont(QtGui.QFont('Arial',18,4))
        self.buton.setStyleSheet("background: green")
        self.buton.setShortcut("Return")
        
        self.buton2=QtWidgets.QPushButton("Delete")
        self.buton2.setStyleSheet("background: red")
        self.buton2.setFont(QtGui.QFont('Arial',18,4))
        self.buton2.setShortcut("Ctrl+D")
        self.buton.setFixedWidth(300)
        self.buton2.setFixedWidth(300)
        h_box0=QtWidgets.QHBoxLayout()
        h_box=QtWidgets.QHBoxLayout()
        h_box2=QtWidgets.QHBoxLayout()
        h_box3=QtWidgets.QHBoxLayout()
        h_box4=QtWidgets.QHBoxLayout()
         
        h_box0.addStretch()
        h_box0.addWidget(self.img)
        h_box0.addStretch()
         
        h_box.addStretch()
        h_box.addWidget(self.label1)
        h_box.addSpacing(168)
        h_box.addWidget(self.Lesson)
        h_box.addStretch()
        
        h_box2.addStretch()
        h_box2.addWidget(self.label2)
        h_box2.addSpacing(10)
        h_box2.addWidget(self.Student)
        h_box2.addStretch()
        
        h_box3.addStretch()
        h_box3.addWidget(self.label3)
        h_box3.addSpacing(168)
        h_box3.addWidget(self.Grade)
        h_box3.addStretch()
        
        h_box4.addStretch()
        h_box4.addWidget(self.buton2)
        h_box4.addSpacing(50)
        h_box4.addWidget(self.buton)
        h_box4.addStretch()
        
        v_box=QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box0)
        v_box.addSpacing(50)
        v_box.addLayout(h_box)
        v_box.addSpacing(20)
        v_box.addLayout(h_box2)
        v_box.addSpacing(20)
        v_box.addLayout(h_box3)
        v_box.addSpacing(50)
        v_box.addLayout(h_box4)
        v_box.addStretch()
        self.window.setLayout(v_box)
        self.main_window.setCentralWidget(self.window)
        self.buton.clicked.connect(self.process)
        self.buton2.clicked.connect(self.process)
        self.main_window.show()
        
    def process(self):
        
        sender=self.main_window.sender()
        
        if sender.text()=="Add to Your List" and self.Student.text()!="" and self.Lesson.text()!="" and self.Grade.text()!="":
           conclusion=self.csv()
           if conclusion==True:
           
            self.window2=QtWidgets.QWidget()
            self.window2.setStyleSheet("background : black")
            self.img2=QtWidgets.QLabel()
           
            self.img2.setPixmap(QtGui.QPixmap("C:\\Users\\asus\\Desktop\\Sample Picture\\tik.jpg"))
            self.img2.setStyleSheet("color: black")
            self.text=QtWidgets.QLabel("Your Process Could Be Successfully.")
            self.text.setStyleSheet("Color: white")
            self.text.setFont(QtGui.QFont("Arial",36,10))
           
            v_box=QtWidgets.QVBoxLayout()
            h_box=QtWidgets.QHBoxLayout()
            h_box1=QtWidgets.QHBoxLayout()
           
            h_box.addStretch()
            h_box.addWidget(self.img2)
            h_box.addStretch()
           
            h_box1.addStretch()
            h_box1.addWidget(self.text)
            h_box1.addStretch()
           
            v_box.addStretch()
            v_box.addLayout(h_box)
            v_box.addSpacing(100)
            v_box.addLayout(h_box1)
            v_box.addStretch()
            self.window2.setLayout(v_box)
            self.window2.show()
           else:
            self.window2=QtWidgets.QWidget()
            self.window2.setStyleSheet("background : black")
            self.img2=QtWidgets.QLabel()
           
            self.img2.setPixmap(QtGui.QPixmap("C:\\Users\\asus\\Desktop\\Sample Picture\\forbidden.png"))
            self.img2.setStyleSheet("color: black")
            self.text=QtWidgets.QLabel("Your Process Couldn't Be Successfully.")
            self.text.setStyleSheet("Color: white")
            self.text.setFont(QtGui.QFont("Arial",36,10))
           
            v_box=QtWidgets.QVBoxLayout()
            h_box=QtWidgets.QHBoxLayout()
            h_box1=QtWidgets.QHBoxLayout()
           
            h_box.addStretch()
            h_box.addWidget(self.img2)
            h_box.addStretch()
           
            h_box1.addStretch()
            h_box1.addWidget(self.text)
            h_box1.addStretch()
           
            v_box.addStretch()
            v_box.addLayout(h_box)
            v_box.addSpacing(100)
            v_box.addLayout(h_box1)
            v_box.addStretch()
            self.window2.setLayout(v_box)
            self.window2.show()
            
        elif sender.text()=="Delete" and self.Student.text()!="" and self.Lesson.text()!="" and self.Grade.text()!="":
            self.Lesson.clear()
            self.Student.clear()
            self.Grade.clear()
            
        else:
            self.window2=QtWidgets.QWidget()
            self.window2.setStyleSheet("background : black")
            self.img2=QtWidgets.QLabel()
           
            self.img2.setPixmap(QtGui.QPixmap("C:\\Users\\asus\\Desktop\\Sample Picture\\forbidden.png"))
            self.img2.setStyleSheet("color: black")
            self.text=QtWidgets.QLabel("Your Process Couldn't Be Successfully.")
            self.text.setStyleSheet("Color: white")
            self.text.setFont(QtGui.QFont("Arial",36,10))
           
            v_box=QtWidgets.QVBoxLayout()
            h_box=QtWidgets.QHBoxLayout()
            h_box1=QtWidgets.QHBoxLayout()
           
            h_box.addStretch()
            h_box.addWidget(self.img2)
            h_box.addStretch()
           
            h_box1.addStretch()
            h_box1.addWidget(self.text)
            h_box1.addStretch()
           
            v_box.addStretch()
            v_box.addLayout(h_box)
            v_box.addSpacing(100)
            v_box.addLayout(h_box1)
            v_box.addStretch()
            self.window2.setLayout(v_box)
            self.window2.show()
            
    def csv(self):
        
        con=sqlite3.connect("Student.db")
        cursor=con.cursor()
        cursor.execute("Create Table if Not Exists student(Lesson TEXT,STUDENT TEXT,GRADE INT)")
        con.commit()
        cursor.execute("Insert Into student Values (?,?,?)",(self.Lesson.text(),self.Student.text(),int(self.Grade.text())))
        con.commit()
        cursor.execute("Select * From student Where Lesson=? and STUDENT=? and GRADE=? ",(self.Lesson.text(),self.Student.text(),int(self.Grade.text())))
        result=cursor.fetchone()
        
        if result!=None:
          con.close()
          con=create_engine('sqlite:///Student.db').connect()
          data=pd.read_sql_table("student",con)
          
          data.to_csv(f"Student.csv",index=False)
          return True
        else:
            return False
        
        
    
    
        
app=QtWidgets.QApplication(sys.argv)       
window=Window()
app.setWindowIcon(QtGui.QIcon("C:\\Users\\asus\\Desktop\\Sample Picture\\student.jpg"))
sys.exit(app.exec())

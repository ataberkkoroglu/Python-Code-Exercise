from PyQt5.QtWidgets import QMainWindow,QLabel,QVBoxLayout,QWidget,QApplication,QCalendarWidget,QHBoxLayout
import sys,os
from PyQt5.QtCore import QDate,QTime,QTimer
from PyQt5 import QtGui
from datetime import datetime

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Program()

    def Program(self):
        self.pencere=QWidget()
        self.calendar=QCalendarWidget()
        self.calendar.setMinimumDate(QDate(1900,1,1))
        self.calendar.setMaximumDate(QDate(3000,1,1))
        self.pencere.setWindowTitle("Calendar")
        self.clock=QLabel()
        self.date=QLabel()
        self.date.setFont(QtGui.QFont('Arial',20))
        self.date.setText(str(datetime.strftime(datetime.now(),"%d.%m.%Y")))
        self.clock.setFont(QtGui.QFont('Arial',20))
        timer=QTimer(self)
        timer.startTimer(1000)
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.clock.setText(label_time)
        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.clock)
        h_box.addSpacing(10)
        h_box.addWidget(self.date)
        h_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addWidget(self.calendar)
        self.pencere.setLayout(v_box)
        self.pencere.show()           

app=QApplication(sys.argv)
Pencere=Window()
os.chdir("C:\\Users\\asus\\Desktop\\Sample Picture")
app.setWindowIcon(QtGui.QIcon("Calendar.png"))
sys.exit(app.exec())
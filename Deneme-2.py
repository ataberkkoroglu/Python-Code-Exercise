from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication
import sys
class Pencere (QMainWindow):
    def __init__(self):
        super().__init__()
        self.program()
    def program(self):
        self.pencere=QWidget()
        self.pencere.setWindowTitle("Deneme")
        self.pencere.setMinimumSize(100,100)
        
        self.pencere.show()
app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())

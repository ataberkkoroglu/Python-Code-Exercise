import sys,os
from PyQt5.QtWidgets import QMainWindow,QAction,QApplication,qApp,QFileDialog,QTextEdit,QTextBrowser,QVBoxLayout,QWidget
class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere=QWidget()
        menubar=self.menuBar()
        self.dosya=menubar.addMenu("File")
        self.edit=menubar.addMenu("Edit")
        self.setWindowTitle("Menüler")
        self.dosya_aç=QAction("Open File",self)
        self.dosya_aç.setShortcut("Ctrl+O")
        self.dosya_kaydet=QAction("Save File",self)
        self.dosya_kaydet.setShortcut("Ctrl+S")
        self.çıkış=QAction("Exit",self)
        self.yazı_alanı=QTextEdit()
        self.çıkış.setShortcut("Ctrl+Q")
        self.dosya.addAction(self.dosya_aç)
        self.dosya.addAction(self.dosya_kaydet)
        self.dosya.addAction(self.çıkış)
        self.temizle=QAction("Delete",self)
        self.menu=self.edit.addMenu("Call And Change")
        self.ara=QAction("Call",self)
        self.degistir=QAction("Change",self)
        self.menu.addAction(self.ara)
        self.menu.addAction(self.degistir)
        self.edit.addAction(self.temizle)
        v_box=QVBoxLayout()
        v_box.addWidget(self.yazı_alanı)
        self.pencere.setLayout(v_box)
        self.çıkış.triggered.connect(self.cikis_yap)
        self.dosya.triggered.connect(self.response)
        self.show()
    def cikis_yap(self):
        qApp.quit()
    def response(self,action):
        if action.text()=="Open File":
           dosya_ismi= QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("ataberk köroğlu"))
           with (dosya_ismi[0],"r+") as file:
            pass
           print("Be Pressed Open File Button")
        if action.text()=="Save File":
           dosya_ismi= QFileDialog.getSaveFileName(self,"Dosya Aç",os.getenv("ataberk köroğlu"))
           with (dosya_ismi[0],"w+") as file:
             file.write()
           print("Be Pressed Save File Button")
        if action.text()=="Exit":
            qApp.quit()
            print("Be Pressed Exit Button")

app=QApplication(sys.argv)
Menu=menu()
sys.exit(app.exec())
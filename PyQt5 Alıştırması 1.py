from PyQt5 import QtWidgets,QtGui
import sys
#from PIL import Image
def pencere():
    app = QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()

    window .setWindowTitle("Ataberk")
    
    Buton=QtWidgets.QPushButton("Okey")
    Buton2=QtWidgets.QPushButton("Cancel")
    h_box=QtWidgets.QHBoxLayout()
    h_box.addStretch() 
    h_box.addWidget(Buton)
    h_box.addWidget(Buton2)
    v_box=QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    window.setLayout(v_box)
    etiket1=QtWidgets.QLabel(window)
    etiket1.setText("BADEM IS STUPID...")
    etiket1.move(400,10)
    #image=Image.open("Badem.jpeg")
    #kırpılacak_alan=(100,0,700,1000)
    #image.crop(kırpılacak_alan).save("Badem2.jpeg")
    etiket2=QtWidgets.QLabel(window)
    etiket2.setPixmap(QtGui.QPixmap("Badem2.jpeg"))
    etiket2.move(300,100)
    window.setGeometry(100,100,500,500)
    window.show()
    sys.exit(app.exec())
pencere()

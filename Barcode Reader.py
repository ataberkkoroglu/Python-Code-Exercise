import cv2,sys,random
from pyzbar.pyzbar import decode
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QFont,QPixmap
from datetime import datetime

cap=cv2.VideoCapture(0)

def Program():
    app=QApplication(sys.argv)
    pencere=QWidget()
    text=QLabel()
    pencere.setWindowTitle("Barcode Reader")
    date=QLabel()
    img=QLabel()
    
    date.setText(str(datetime.strftime(datetime.now(),"Date: %d / %m / %Y  Hour: %H : %M : %S")))
    date.setFont(QFont('Arial',32,QFont.Normal,True))
    text.setFont(QFont('Arial',48,QFont.Bold))
    img.setPixmap(QPixmap("C:\\Users\\asus\\Desktop\\Sample Picture\\Market.jpg")) #Sample Image of Product
    text.setText(f"Product is {str(random.randint(0,1000)+float(random.randrange(0,1,100)))} Dolar")
    
    v_box=QVBoxLayout()
    h_box=QHBoxLayout()
    v_box.addStretch()
    v_box.addWidget(date)
    v_box.addSpacing(50)
    v_box.addWidget(img)
    v_box.addSpacing(50)
    v_box.addWidget(text)
    v_box.addStretch()
    h_box.addStretch()
    h_box.addLayout(v_box)
    h_box.addStretch()
    pencere.setLayout(h_box)
    
    pencere.show()
    sys.exit(app.exec())
   
counter=0    
while 1:
    ret,frame=cap.read()
    Barcode=decode(frame)
    for barcode in Barcode:
        (x,y,h,z)=barcode.rect
        cv2.rectangle(frame,(x,y),(x+h,y+z),(100,255,100),2)
        Program()
    cv2.imshow("Barcode Reader",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
   
cap.release()
cv2.destroyAllWindows()
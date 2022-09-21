import cv2
import webbrowser

çap=cv2.VideoCapture(0)
scanner=cv2.QRCodeDetector()

while 1:
    _,img=çap.read()
    data,one,_=scanner.detectAndDecode(img)
    if data:
        link=data
        break
    cv2.imshow("QR Code Reader",img)
    if cv2.waitKey(1)==ord('q'):
        break
b=webbrowser.open(str(link))
çap.release(link)
cv2.destroyAllWindows()

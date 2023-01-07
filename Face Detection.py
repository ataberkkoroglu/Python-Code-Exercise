import cv2,os
os.chdir('C:\\Users\\asus\Desktop\\Workshop-1_Proje\\__pycache__\\preview\\OpenCV\\opencv\\sources\\data\\haarcascades')
capture = cv2.VideoCapture(0)

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

    ret, frame = capture.read()   
    faces = cascade.detectMultiScale(frame,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(frame,"Ataberk",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.50,(0,0,255),1)
        
    cv2.imshow('Kamera',frame)
    if cv2.waitKey(30) & 0xff ==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
import cv2

cap=cv2.VideoCapture(0)

cascade=cv2.CascadeClassifier("C:\\Users\\asus\\Desktop\\Workshop-1_Proje\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml")
cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
while (1):
    _,frame=cap.read()
    mask=cascade.detectMultiScale(frame,minSize=(20,20))
    for Mask in mask:
        x1,y1,w,h=Mask.ravel()
        cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(255,0,255),2)
        cv2.putText(frame,"Person",(x1,y1),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,0,0),thickness=2,lineType=cv2.LINE_AA)
    """M=cv2.getRotationMatrix2D((frame.shape[0]/1.5,frame.shape[1]/1.5),90,1)
    frame=cv2.warpAffine(frame,M,(frame.shape[0],frame.shape[1]))"""
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    thresh=cv2.adaptiveThreshold(frame,127,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imshow("Frame",thresh)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone import FPS,HandTrackingModule,PoseModule


cap=cv2.VideoCapture(0)

detect=FaceDetector()
fpsReader=FPS()
hand=HandTrackingModule.HandDetector()
cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)
while(1):
    ret,frame=cap.read()
    frame,result=detect.findFaces(frame)
    hands,frame=hand.findHands(frame)
    
    fps,frame=fpsReader.update(frame,pos=(30,30))
    try:
     
     for Result in result:
        
        x,y,w,h=Result['bbox']
        
        yeni=frame[y:y+h,x:x+w]
        yeni=cv2.blur(yeni,(45,45),borderType=cv2.BORDER_DEFAULT)
        frame[y:y+h,x:x+w]=yeni
    except:
        pass
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
print(hands)
    

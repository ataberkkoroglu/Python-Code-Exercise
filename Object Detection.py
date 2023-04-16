import cv2,numpy as np
from ultralytics import YOLO
import requests

url=("http://192.168.1.34:8080/shot.jpg")
model=YOLO("yolov8n.pt")

while(1):
    img_resp=requests.get(url)    
    img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    frame=cv2.imdecode(img_arr,cv2.IMREAD_COLOR)
    
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=model(frame,verbose=False)
    labels=results[0].names
    
    for i in range(len(results[0].boxes)):
        x1,y1,x2,y2=results[0].boxes.xyxy[i]
        score=results[0].boxes.conf[i]
        label=results[0].boxes.cls[i]
        x1,y1,x2,y2,score,label=int(x1),int(y1),int(x2),int(y2),float(score),int(label)
        name=labels[label]
        if score<0.5:
          continue
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
        text=name+" "+str(format(score,'.2f'))
        cv2.putText(frame,text,(x1,y1-10),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,255,255),2)   
         
    cv2.imshow("Frame",frame)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
    
cap.release()
cv2.destroyAllWindows()
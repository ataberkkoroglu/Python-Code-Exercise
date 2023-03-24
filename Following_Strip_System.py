import cv2,numpy as np,requests

url=("http://192.168.1.32:8080/shot.jpg")

while 1:
    img_resp=requests.get(url)    
    img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    frame=cv2.imdecode(img_arr,cv2.IMREAD_COLOR)
     
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(frame_gray,100,255)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=8)
    print(lines)
    
    try:
     for line in lines:
        x1,y1,x2,y2=line.ravel()
        
        if (x1==(1980/2) or x2==(1980/2)):
            cv2.putText(frame,"Doing Strip Breach",(x1,y1-10),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),cv2.LINE_AA)
        else:
            cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
        
    except:
        pass
    cv2.imshow("Lines",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
   

cv2.destroyAllWindows()
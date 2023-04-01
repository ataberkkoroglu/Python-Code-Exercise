import sqlite3,cv2
from datetime import datetime
class Face:
   def __init__(self):
       self.Main_SQL()
       self.main()
   def Main_SQL(self):
     con=sqlite3.connect("Face.db")
     cursor=con.cursor()
     return con,cursor
     
   def Data(self):
       con,cursor=self.Main_SQL()
       cursor.execute("Select * From face")
       count=len(cursor.fetchall())
       return count
    
      
   def SQL2(self):
       con,cursor=self.Main_SQL()
       cursor.execute("Create Table If Not Exists face(Name TEXT,FootAge BLOB,Date TEXT)")
       con.commit()
       
   def SQL3(self):
       with open(f"FootAge_{self.Data()}.png",'rb') as file:
           data=file.read()
       
       con,cursor=self.Main_SQL()
       cursor.execute("Select * From face")
       count=len(cursor.fetchall())
       cursor.execute("Insert Into face Values(?,?,?)",(f"FootAge_{count+1}",data,str(datetime.strftime(datetime.now(),"%H :%M %S %d.%m.%Y"))))
       con.commit()
       con.close()
       
       
   
   def main(self):
       self.SQL2()
       cap=cv2.VideoCapture(0)
       cascade=cv2.CascadeClassifier("C:\\Users\\asus\\Desktop\\Workshop-1_Proje\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml")
       
       codec=cv2.VideoWriter_fourcc('m','p','4','v')

       Video=cv2.VideoWriter("Camera.mp4",codec,30,(640,480))
      
       while 1:
           ret,frame=cap.read()
           multi=cascade.detectMultiScale(frame,minSize=(20,20))
           if cv2.waitKey(1) & 0xFF==13:         #Press Enter Key   
            for Multi in multi:
                cv2.imwrite(f"FootAge_{self.Data()}.png",frame)
                self.SQL3() 
           cv2.imshow("Camera",frame)
            
           Video.write(frame)
           if cv2.waitKey(1) & 0xFF==ord('q'):
               break
       cap.release()
       cv2.destroyAllWindows()
         

face=Face()
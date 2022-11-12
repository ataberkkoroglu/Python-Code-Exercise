import sys,time
from datetime import datetime

x=datetime.timestamp(datetime.now())
print("Welcome To Program..\n"+time.ctime(x))
y=list()
i=0
while(i<15):
  try:
    if(i!=0):
      print("If You want to quit Program, Press 'q' Key...")
    x=input("Write One by One Number Which You Want to Write: ")
    if (x=='q'):
      sys.exit()
    else:
      x=int(x,10)
      if(x<10 and x>=0):
       y.append(str(x))
       i +=1 
    
  except:
    break
y.reverse()

print("".join(y))

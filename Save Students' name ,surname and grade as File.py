import time,sys,os
k=0 
v=0
p=0
a=list()
os.chdir("C:/Users/asus/Desktop/")
while(1):
  try:
    with open("FizikLab2.Txt","r",encoding="utf-8") as fp:
     a.extend(fp.readlines())
     if ("Number Name Surname Grade\n" not in a):
      fp.write("Number Name Surname Grade\n")
      
     v +=len(a)-1
     
  except:
    with open("FizikLab2.Txt","w",encoding="utf-8") as fp:
      fp.write("Number Name Surname Grade\n")
     
  while(1):
   
    with open("FizikLab2.Txt","a+",encoding="utf-8") as fp:
      while(1):
        x=input("Write Student's Name? :  ")
        if (len(x)>=3):
          break
        else:
          sys.__stderr__.write("\nInvalid Name...\a\n")
          time.sleep(1)
      while(1):
       y=input("Write Student's Surname ? : ")
       if (len(y)>=3):
          break
       else:
          sys.__stderr__.write("\nInvalid Surname...\a\n")
          time.sleep(1)
      while(1):
       z=int(input("Write Student's Grade: "))
       if (z>=0 and z<=100):
        break
       else:
        sys.__stderr__.write("\nInvalid Grade...\a\n")
        time.sleep(1)
      v +=1
      fp.write(str(v))
      fp.write(')')
      fp.write(' ')
      fp.write(x[0])
      fp.write(x[1])
      i=0
      for i in range(2,len(x)):
        if x[i]!=' ':
          k +=1
        else:
          p +=1
          break
      print(k)
      fp.write((k)*"*")
      if p!=0:
       fp.write(x[k+2])
       fp.write(x[k+3])
       fp.write((len(x)-(k+4))*"*")
      fp.write(' ')
      
      if len(y)<4:
        for i in range(0,len(y)):
          if i==len(y)-1 or i==len(y)-2:
            fp.write("*")
          else:
            fp.write(y[i])
      else:
        fp.write(y[0])
        fp.write(y[1])
        fp.write(y[2])
        fp.write((len(y)-3)*"*")      

      fp.write(' ')
      fp.write('= ')
      fp.write(str(z))
      fp.write("\n")
      fp.seek(fp.tell())
      
    while(1):
      sec=input("Would You Like To Contunie(Y/N) ? : ")
      if  sec=='Y' or sec=='y':
        time.sleep(3)
        break
      elif sec=='N' or sec=='n':
        sys.__stdout__.write("\nHave a Good Days...\a")
        sys.__stdout__.flush()
        sys.exit()
      else:
        sys.__stderr__.write("\nWrong Input...\a")
        sys.__stderr__.flush()

    

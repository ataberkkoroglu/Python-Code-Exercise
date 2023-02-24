import numpy as np,sys,time
from datetime import datetime

print("Welcome To Program...\n"+datetime.strftime(datetime.now(),"%H:%M:%S %d / %m / %Y "))
main_cluster=list()
counter2=0
counter3=0
while 1:
  counter2=0  
  while counter2<9:
   
   cluster=[]
   counter3=0
   while counter3<3:
    num2=np.random.randint(1,9) 
    if not num2 in cluster:
        cluster.insert(counter3,num2)
        counter3 +=1                
   for i in range(len(cluster),9):
       cluster.append(None)
   
   for i in range(0,9):
      if counter2==0:
       if cluster[i]!=None:
        cluster[np.random.randint(0,9)]=cluster[i]
        cluster[i]=None
      else:
        a=np.random.randint(0,9)
        for e in range(0,len(main_cluster)):
         if cluster[i]!=None:
           if cluster[i]!=main_cluster[e][a]:
            cluster[a]=cluster[i]
            cluster[i]=None
            
   for i in cluster:
       rep=cluster.count(i)
       if i!=None and rep!=1:
           for e in range(0,rep):
               cluster.remove(i)   
   if counter2==0:
     print(cluster)
   else:
       for i in range(0,len(main_cluster)):
           print(f"\n-------------------{i+1}.Square----------------------\n{main_cluster[i]}")
           
   life=10 
   for i in cluster:
    if i==None:
      a=cluster.index(i)
      life=10
      while life>0:
           
        counter=0
        num=int(input("Write a Unique Number: "))
        if num<10 and num>=0:
            if counter2!=0: 
             for e in range(0,len(main_cluster)):
              if main_cluster[e][a]==num:
                  counter +=1
             if counter==0 and not num in cluster:
               cluster.pop(a)
               cluster.insert(a,num)
               print(cluster)
               break
             else:
                 for i in range(0,len(main_cluster)):
                  print(f"\n-------------------{i+1}.Square----------------------\n{main_cluster[i]}")
                  life -=1 
            else:
                if not num in cluster and i==None:
                    cluster.remove(i)
                    cluster.insert(a,num)
                    print(cluster)
                    break
                else:
                    life -=1 
    if life<=0:
       print("you Have Failed!..".upper()) 
       counter2=10
       break          
   if not None in cluster:           
     main_cluster.extend([cluster])
  
   counter2 +=1
  if counter2==8:
   main_cluster2=np.array(main_cluster).reshape(9,9)
   print("\n")
   for i in main_cluster2:
      for e in i:
          print(e,end="|")
      print("","-"*20,sep="\n")
   print("congratulations!... ".upper())
  while 1:
      ch=input("Would You Like To Contunie(Y/N) ? : ")
      if(ch=='Y' or ch=='y'):
          time.sleep(2)
          break
      elif (ch=='N' or ch=='n'):
          print("Have a Good Days...\n"+datetime.strftime(datetime.now(),"%H:%M:%S %d / %m / %Y "))
          sys.exit()
      else:
          print("Wrong Character...\nPlease Write Again")
 
 
 
    

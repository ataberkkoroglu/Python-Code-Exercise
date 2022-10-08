import random,time,sys
from datetime import datetime
print(datetime.ctime(datetime.now()))
print("Welcome Program Which Calculates Arrival  of Bus to  Stop")
while(1):
 person=random.randint(1,9)
 bus=random.randint(1,10)
 i=1
 sayac=0
 while(i<10):
   print(datetime.ctime(datetime.now()))
   if i==person and person>bus and sayac==0:
        print("The Bus arrived stop which you become in {}. Stop ".format(i))
        break
   elif i!=person and person>bus and sayac==0:
        i +=1
        time.sleep(random.randint(5,15))
        if i==person:
           pass
        else:
          print("The Bus is in {}. Stop".format(i))
   else:
    sayac +=1
    print("Missed The Bus...")
    break
 while(1):
  sec=input("Would you like to continue ? :  ")

  if sec=='E' or sec=='e':
    time.sleep(3)
    break
  elif sec=='H' or sec=='h':
    print("Have a Good Days")
    sys.exit()
  else:
    print("Wrong Character")
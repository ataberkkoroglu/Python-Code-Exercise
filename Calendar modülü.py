import calendar,time,sys
from datetime import datetime

print("Welcome To Program...\n "+time.ctime(datetime.timestamp(datetime.now())))
while(1):
 month=input("Write Month: ")
 year=int(input("Write year: "))
 
 month=month.capitalize()
 print(month)
 x={"January":1 ,"February":2,"March":3,"April":4,"May":5,"June" :6,"July":7,"August":8,"September":9,"October":10, "November":11,"December":12}
 y=(1,2)
 print(type(y))
 for i,e in x.items():
    if i==month:
        print(calendar.month(year,e))
 while(1):
  sec=input("Would You Like To Contunie(Y/N) ? : ")
  if (sec=='Y' or sec=='y'):
    time.sleep(2)
    break
  elif (sec=='N' or sec=='n'):
    print("Have a Good Days...")
    sys.exit()
  else:
    sys.__stderr__.write("\nWrong Input...\a")
    sys.__stderr__.flush()





         
        
      
  
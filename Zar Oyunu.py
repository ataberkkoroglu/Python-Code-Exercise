from datetime import datetime
import random,time,os,sys
print("Programa Hoşgeldiniz...\n"+str(datetime.ctime(datetime.now())))
a=list()
b=list()
while(1):
 x=random.randint(1,6)
 y=random.randint(1,6)
 a.append(x)
 b.append(y)
 for i,e in zip(a,b):
    print("1.Zar:{},2.Zar: {}".format(i,e))
 while(1):
  sec=input("Devam Etmek İstiyor Musunuz(E/H) ? : ")
  if (sec=='E' or sec=='e'):
    print("Devam Ediliyor...")
    a.remove(x)
    b.remove(y)
    time.sleep(3)
    break
  elif (sec=='H' or sec=='h'):
    print("Yine Bekleriz...")
    sys.exit()
  else:
    sys.__stderr__.write("\nYanlış Girildi...\a")
    sys.__stderr__.flush()
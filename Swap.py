import sys
from datetime import datetime
import os,time
def Swap(x,y):
 x,y=y,x

 print(x,y)
sys.__stdout__.write("Programa Hoşgeldiniz...\n")
sys.__stdout__.flush()
sys.__stdout__.write(str(datetime.ctime(datetime.now())))
sys.__stdout__.flush()

while(1):
 x=int(input("\n1.Sayıyı Giriniz: "))
 y=int(input("2. Sayıyı Giriniz: "))
 Swap(x,y)
 sec=input("Devam Etmek İstiyor Musunuz(E/H) ? : ")
 if (sec=="E" or sec=="e"):
    sys.__stdout__.write("\nPrograma Devam Ediliyor...")
    time.sleep(3)
 elif (sec=='H' or sec=='h'):
    sys.__stdout__.write("\nYine Bekleriz...")
    sys.__stdout__.flush()
    time.sleep(5)
    os._exit(3)
 else:
    sys.__stderr__.write("\nYanlış Girildi...\a")
    sys.__stderr__.flush()
    os.abort()


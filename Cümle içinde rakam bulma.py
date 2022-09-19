import sys,time,os
from datetime import datetime
y=list()
x=list()
print("Uygulamaya Hoşgeldiniz...")
sayac=0
sys.__stdout__.write(str(datetime.ctime(datetime.now())))
sys.__stdout__.flush()
while(1):
 sayac=0
 a=input("\nCümleyi Yazınız: ")
 for i in range(0,10):
    b=a.count(str(i))
    if (b!=0):
        sayac +=1
 print("Yazılan Cümlede {} Tane Sayı Bulunuyor.".format(sayac))
 sec=input("Devam Etmek İstiyor Musunuz(E/H) ? : ")
 if (sec=="E" or sec=='e'):
    print("Devam Ediliyor...")
    time.sleep(3)
 elif (sec=='H' or sec=='h'):
    print("Yine Bekleriz...")
    time.sleep(5)
    sys.exit()
 else:
    sys.__stderr__.write("\nYanlış Değer Girildi...\a")
    sys.__stderr__.flush()
    time.sleep(2)
    os.abort()
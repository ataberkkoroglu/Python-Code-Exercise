from datetime import datetime
import time
print("Programa Hoşgeldiniz")
now=datetime.now()
print(datetime.ctime(now))
sayi=list()
i=0
while(i<4):
 print(i+1,end=" ")
 x=int(input("Sayıyı Giriniz: "))
 sayi.append(x)
 i +=1
for k,i in enumerate(sayi):
    print(k+1,i,sep="-")

islem=((sayi[0]+sayi[1])*2)/sayi[2]+(4*sayi[3])
time.sleep(2)
print("İşlemin Sonucu: {}".format(islem))

import sys,time
from datetime import datetime

x=datetime.timestamp(datetime.now())
print("Programa Hoşgeldiniz...\n"+time.ctime(x))
y=list()
i=0
while(i<15):
  try:
    if(i!=0):
      print("Çıkmak İstiyorsanız 'q' ya Basınız...")
    x=int(input("Girmek İstediğiniz Sayının Rakamlarını Soldan Sağa Doğru Teker Teker Yazınız: "))
    if(x<10 and x>=0):
     y.append(str(x))
     i +=1 
  except:
    break
y.reverse()

print("".join(y))

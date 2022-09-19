from datetime import datetime
import random,sys,os,time
sys.__stdout__.write("Programa Hoşgeldiniz...\n")

print(datetime.ctime(datetime.now()))
name=list()
surname=list()
while(1):
        
    x=input("Adınızı Yazınız: ")
    name.append(x)
    y=input("Soyadınızı Yazınız: ")
    surname.append(y)
    x=len(name)
    y=len(surname)
    if x>1 and y>1:
      a=random.randint(0,x-1)
      c=random.randint(0,y-1)
      print(a,c)
      print(name[a],surname[c])
 
    else:
     print(name[0],surname[0])
    b=input("Devam Etmek İstiyor Musunuz(E/H)? : ")
    if b=="h" or b=="H":
        sys.__stdout__.write("\nYine Bekleriz...")
        time.sleep(5)
        break
    elif b=="E" or b=="e":
        sys.__stdout__.write("Devam Ediliyor...\n")
        time.sleep(3)
    else:
        sys.__stderr__.write("Hatalı Giriş Yapıldı...")
        os.abort()

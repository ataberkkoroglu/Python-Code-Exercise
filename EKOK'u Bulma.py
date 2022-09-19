from datetime import datetime
import sys,os,time
print("Programa Hoşgeldiniz...\n"+str(datetime.ctime(datetime.now())))
while(1):
 x=int(input("1.Sayıyı Giriniz: "))
 y=int(input("2.Sayıyı Giriniz: "))
 if x<0 or y<0:
    sys.__stderr__.write("\nYanlış Değer Girdiniz...\n")
    sys.__stderr__.flush()
 else:
    while(1):
        if x==y:
            print("Girilen İki Sayının({} {}) EKOK'u: {}".format(x,y,x))
            break
        elif x>y and x%y==0:
            print("Girilen İki Sayının({} {}) EKOK'u: {}".format(x,y,x))
            break
        elif y>x and y%x==0:
            print("Girilen İki Sayının({} {}) EKOK'u: {}".format(x,y,y))
            break
        else:
            if x>y:
               for i in range(x+1,(x*y)+1):
                if (i%x==0 and i%y==0):
                   print("Girilen İki Sayının({} {}) EKOK'u: {}".format(x,y,i))
                   break 
               break
            elif y>x:
              for e in range(y+1,(y*x)+1):
                if (e%x==0 and e%y==0):
                   print("Girilen İki Sayının({} {}) EKOK'u: {}".format(x,y,e))
                   break 
              break
    sec=input("Devam Etmek İstiyor Musunuz(E/H) ? : ")
    if (sec=='E' or sec=='e'):
        print("Devam Ediliyor...")
        time.sleep(3)
    elif (sec=='h' or sec=='H'):
        print("Yine Bekleriz...")
        sys.exit()
    else:
        sys.__stderr__.write("Yanlış Değer Girildi...\a")
        sys.__stderr__.flush()
        os.abort()
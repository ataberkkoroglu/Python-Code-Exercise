print("Programa Hoşgeldiniz...")
from os import abort
import sys,time
while True:
 x=int(input("4 Basamaklı 1 Sayı Giriniz: "))
 toplam=0
 i=0
 if (x>999 and x<10000):
    while(i<4):
        e=int(x%10)
        x /=10.0
        print(e)
        toplam +=e
        i +=1
    print("Toplam :{}".format(int(toplam)))
    sec=input("Devam Etmek İstiyor Musunuz(E/H)? :")
    if sec=="e" or sec=="E":
        print("Devam Ediyorsunuz...")
    elif sec=="H"or sec=="h":
        print("Programdan Çıkıyorsunuz...")
        time.sleep(3)
        sys.exit()
    else:
        print("Yanlış Değer Girdiniz...")
        abort()
 else:
    sys.stderr.write("Yanlış Değer Girdiniz...")
    sys.stderr.flush()
    sec=input("\nDevam Etmek İstiyor Musunuz(E/H)? :")
    if sec=="e" or sec=="E":
        print("Devam Ediyorsunuz...")
    elif sec=="H" or sec=="h":
        print("Programdan Çıkıyorsunuz...")
        time.sleep(3)
        break

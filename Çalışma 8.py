import time,sys
print("Programa Hoşgeldiniz...")
while True:
 x=int(input("Girmek İstediğiniz Sayıyı Giriniz: "))
 a=x%5
 print(a)
 sec=input("Devam Etmek İstiyor Musunuz(E/H)? :")
 if sec=="H" or sec=="h":
    print("Programdan Çıkış Yapıyorsunuz...")
    time.sleep(3)
    sys.exit()
 elif sec=="E" or sec=="e":
    print("Devam Ediyorsunuz...")
    time.sleep(1)
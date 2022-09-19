x=["1","2","3","4","5","6","Badem","7","89","91","100","110"]
print("Programa Hoşgeldiniz...")
import time
while(1):
  y=input("Aramak İstediğiniz Kelimeyi veya Numarayı Yazınız: ")
  if(y in x):
   print(x.index(y))
   z=int(input("Devam Etmek İstiyorsanız 1'e Arama Programını Kapatmak İstiyorsanız 0'ı tuşlayınız: "))
   if(z==0):
    print("Çıkış Yapılıyor...")
    break
   elif(z==1):
     print("Devam Ediliyor...")
     time.sleep(1)
     
   else:
     print("Yanlış Değer Girdiniz")
     while(1):
        z=int(input("Devam Etmek İstiyor Musunuz: "))
        if(z==0):
          print("Çıkış Yapılıyor...")
          break
        elif(z==1):
          print("Devam Ediliyor...")
          break
        else:
          print("Yanlış Değer Girdiniz")
     if(z==0):
      break
  elif(x.count(y)==0):
    print("Girmiş Olduğunuz Sayı Veya Kelime Bulunamadı.")
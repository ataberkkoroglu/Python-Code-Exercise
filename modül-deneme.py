import random
import time
print(
"""
 Sayi Tahmin Etme Oyunu

1 ile 40 Arasindaki Sayiyi Tahmin Ediniz
"""
)

rastgele_sayi=random.randint(1,40)

tahmin_hakki=7

while tahmin_hakki>0:

  x=int(input("Sayinizi Giriniz= "))
  if x<rastgele_sayi:
      print("Bilgiler Sorgulanıyor...")
      time.sleep(1)
      print("Daha yüksek Bir Sayıyı Söyleyiniz.")
      tahmin_hakki -=1
      if tahmin_hakki==0:
           print("Oynama Hakkınız Kalmamıştır...")
           print(rastgele_sayi)
           break
  elif x==rastgele_sayi:
      print("Tebrikler Sayiyi Buldunuz.")
      break
  elif x>rastgele_sayi:
       print("Bilgiler Sorgulanıyor...")
       time.sleep(1)
       print("Daha Düşük Bir Sayıyı Söyleyiniz.")
       if tahmin_hakki==0:
           print("Oynama Hakkınız Kalmamıştır...")
           print(rastgele_sayi)
           break

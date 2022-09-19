import sys
print("Uygulamaya Hoşgeldiniz...")

while(1):
 sayi=int(input("1.Sınav Notunuzu Giriniz: "))
 sayi2=int(input("2.sınav Notunuzu Giriniz: "))

 if(sayi>=0 and sayi<=100) &(sayi2>=0 and sayi2<=100):
      ortalama=(sayi+sayi2)/2
      print("1.Sınav Notunuz: {}\n2.Sınav Notunuz:{}\nOrtalamanız:{}".format(sayi,sayi2,ortalama))
      cıkıs=input("Uygulamadan Çıkmak için 'q' a basınız.\n")
      if(cıkıs=="q"):
        sys.exit()
 else:
    sys.stderr.write("Yanlış Değer Girdiniz...\n")
    sys.stderr.flush()

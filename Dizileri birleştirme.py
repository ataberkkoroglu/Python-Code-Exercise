from functools import reduce


print("Uygulamaya Hoşgeldiniz...")
a=list()
b=list()
c=list()
while(1):
    print("")
    print("----1.Dizi İçin Veri Türleri---\n1-FLoat\n2-İnteger\n3-String\n4-Bool\n5-Çıkış")
    x=int(input("Gireceğiniz Verinin Türünü Yazınız(1/2/3/4/5) ? :"))
    if (x==1):
         y=float(input("Girmek İstediğiniz Ondalıklı Sayıyı Yazınız: "))
         a.append(y)
    elif (x==2):
         y=int(input("Girmek İstediğiniz Tam Sayıyı Yazınız: "))
         a.append(y)
    elif (x==3):
         y=input("Girmek İstediğiniz Metni Yazınız: ")
         a.append(y)
    elif (x==4):
        y=bool(input("True(1) veya False(0) Giriniz: "))
        a.append(y)
    elif (x==5):
        break
while(1):
    print("----2.Dizi İçin Veri Türleri---\n1-FLoat\n2-İnteger\n3-String\n4-Bool\n5-Çıkış")
    z=int(input("Gireceğiniz Verinin Türünü Yazınız(1/2/3/4/5) ? :"))
    if (z==1):
         y=float(input("Girmek İstediğiniz Ondalıklı Sayıyı Yazınız: "))
         b.append(y)
    elif (z==2):
         y=int(input("Girmek İstediğiniz Tam Sayıyı Yazınız: "))
         b.append(y)
    elif (z==3):
         y=input("Girmek İstediğiniz Metni Yazınız: ")
         b.append(y)
    elif (z==4):
        y=bool(input("True(1) veya False(0) Giriniz: "))
        b.append(y)
    elif (z==5):
        break
c.extend(a)
c.extend(b)
print(c)


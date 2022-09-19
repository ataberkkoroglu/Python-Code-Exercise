print("Programa Hoşgeldiniz")
sayi=list()
i=0
while(i<3):
    number=int(input("Sayıyı Giriniz: "))
    sayi.append(number)
    i +=1
sayi.sort()
print("En Büyük Sayı: {} ".format(sayi[2]))

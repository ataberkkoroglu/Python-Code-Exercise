print("Programa Hoşgeldiniz...")

while True:
 x=int(input("5 Basamaklı Sayı Giriniz: "))  
 if x>9999 and x<99999:
   break
toplam =0
while True:
     c=int(x%10)
     toplam +=c
     x /=10
     if x>=0 and x<1:
        print(toplam)
        break
   
     

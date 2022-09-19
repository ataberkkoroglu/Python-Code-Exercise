print("Programa Hoşgeldiniz...")
y=list()
i=0
while(i<5):
 x=int(input("Girmek İstediğiniz Sayının Rakamlarını Soldan Sağa Doğru Teker Teker Yazınız: "))
 if(x<10 and x>=0):
   y.append(str(x))
   i +=1 
y.reverse()

print("".join(y))

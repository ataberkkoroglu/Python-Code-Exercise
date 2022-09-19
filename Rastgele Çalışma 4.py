import random
print("Programa Hoşgeldiniz...")
sayac=0
i=0
y=list()
while i<600:
 x= random.randint(0,1000)
 
 if x<100:
    y.append(x)
    sayac +=1
 i +=1
print(y)
print(sayac)


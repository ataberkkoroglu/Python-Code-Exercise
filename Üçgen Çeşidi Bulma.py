import time,sys,os

print("Programa Hoşgeldiniz...")
x=list()

while(1):
 i=0
 while(i<3):
    
    x.append(int(input("{}. Kenarı Giriniz: ".format(i+1))))
    i +=1
 if(x[0]==x[1] and x[1]==x[2] and x[0]==x[2]):
    print("{} {} ve{} Kenar Uzunluklarına Sahip OLan Üçgen Eşkenar Üçgendir...".format(x[0],x[1],x[2]))
 elif (x[0]==x[1] or x[1]==x[2]):
    print("{} {} ve{} Kenar Uzunluklarına Sahip OLan Üçgen İkizkenar Üçgendir...".format(x[0],x[1],x[2]))
 else:
    print("{} {} ve{} Kenar Uzunluklarına Sahip OLan Üçgen Çeşitkenar Üçgendir...".format(x[0],x[1],x[2]))
 y=input("Devam Etmek İstiyor Musunuz(E/H) ? : ")
 if (y=="E" or y=="e"):
    time.sleep(2)
    for i in x:
        x.remove(i)
 elif (y=="H" or y=="h"):
    sys.__stdout__.write("Yine Bekleriz...")
    sys.__stdout__.flush()
    sys.exit()
 else:
    sys.__stderr__.write("Yanlış Girildi...")
    os.abort()


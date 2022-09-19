print("Uygulamaya Hosgeldiniz...")
a=input("Dörtgen Mi Yoksa Üçgen Tipi Mi Bulmak İstersiniz= ")
if a=="Dörtgen" or a=="dörtgen":
    y=float(input("Dörtgenin Birinci Kenarını Giriniz= "))
    z=float(input("Dörtgenin İkinci Kenarini Giriniz= "))
    x=float(input("Dörtgenin Üçüncü Kenarını Giriniz= "))
    v=float(input("Dörtgenin Dördüncü Kenarını Giriniz= "))
    if x==z==v==y:
        print("Dörtgenin Tipi Kare veya Eşkenar Dörtgendir.")
    elif x==z and v==y:
        print("Dörtgenin Tipi Dikdörtgendir.")
    elif x==y and z==v:
        print("Dörtgenin Tipi Dikdörtgendir.")
    elif x==v and z==y:
        print("Dörtgenin Tipi Dikdörtgendir.")
    elif x!=y and y!=v and v!=z and x!=z:
        print("Sıradan Dörtgen")
    else:
        print("Yanlış Değerler Girdiniz.")
elif a=="Üçgen" and a=="üçgen":
    b=float(input("Üçgenin Birinci Kenarını Giriniz= "))
    c=float(input("Üçgenin İkinci Kenarını Giriniz= "))
    d=float(input("Üçgenin Üçüncü Kenarını Giriniz= "))
    if b==c==d:
        print("Üçgenin Tipi Eşkenar Üçgendir.")
    elif b==c or b==d or c==d:
        print("Üçgenin Tipi İkizkenar Üçgendir.")
    elif b!=c and c!=d and b!=d :
        print("Üçgenin Tipi Çeşitkenar Üçgendir.")
else:
    print("Yanlış Girdiniz.")
grade=open("Geçenler.txt","a",encoding="utf-8")
point=open("Kalanlar.txt","a",encoding="utf-8")
while True:
    Ad_Soyad=input("Adınızı ve Soyadınızı Giriniz= ")
    Okul_Numarası=int(input("Okul Numaranızı Giriniz= "))
    vize=int(input("Vize Notunuzu Giriniz= "))
    final=int(input("Final Notunuzu Giriniz= "))
    Ortalama= vize*0.4+final*0.6
    if Ortalama>=90:
        with open("Geçenler.txt","a",encoding="utf-8") as grade:
            grade.write(Ad_Soyad)
            grade.write("\n")
            break
        
    elif Ortalama>=85:
        with open("Geçenler.txt","a",encoding="utf-8") as grade:
            
            grade.write(Ad_Soyad)
            grade.write("\n")
            break
    elif Ortalama>=80:
         with open("Geçenler.txt","a",encoding="utf-8") as grade:
            
            grade.write(Ad_Soyad)
            grade.write("\n")
            break
    elif Ortalama>=80:
         with open("Geçenler.txt","a",encoding="utf-8") as grade:
            
            grade.write(Ad_Soyad)
            grade.write("\n")
            break
    elif Ortalama>=75:
         with open("Geçenler.txt","a",encoding="utf-8") as grade:
            
            grade.write(Ad_Soyad)
            grade.write("\n")
            break
    elif Ortalama>=70:
         with open("Geçenler.txt","a",encoding="utf-8") as grade:
            
            grade.write(Ad_Soyad)
            grade.write("\n")
            break
    elif Ortalama>=65:
         with open("Geçenler.txt","a",encoding="utf-8") as grade:
            
            grade.write(Ad_Soyad)
            grade.write("\n")
            break
    elif Ortalama>=60:
         with open("Geçenler.txt","a",encoding="utf-8") as grade:
            
            grade.write(Ad_Soyad)
            grade.write("\n")
            break
    elif Ortalama<60:
         with open ("Kalanlar.txt","a",encoding="utf-8") as point:
                
                point.write(Ad_Soyad)
                point.write("\n")
                break
    else:
        print("Yanlış Değer Girdiniz...")
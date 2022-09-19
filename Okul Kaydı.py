import sys,os,time,random
from datetime import datetime
import sqlite3

class OkulKayıt():
    def __init__(self,ad,soyad,tc,dy,tel):
        self._Ad=ad
        self._Soyad=soyad
        self._Tc=tc
        self._Dy=dy
        self._Tel=tel

    
class Ogrenci(OkulKayıt):
    def __init__(self,ad,soyad,tc,dy,tel,no):
        super().__init__(ad,soyad,tc,dy,tel)
        self.__No=no
    def __str__(self):
        print("Öğrencinin Adı: {}\nÖğrencinin Soyadı: {}\nÖğrencinin Tc Numarası: {}\nÖğrencinin Doğum Tarihi:{}\nÖğrencinin Cep Telefon Numarası: {}\nÖğrencinin Okul Numarası: {}".format(self._Ad,self._Soyad,self._Tc,self._Dy,self._Tel,self.__No))

class Ogretmen(OkulKayıt):
    def __init__(self,ad,soyad,tc,dy,tel,brans):
        super().__init__(ad,soyad,tc,dy,tel)
        self.__Brans=brans
    def __str__(self):
        print("Öğretmenin Adı: {}\nÖğretmenin Soyadı: {}\nÖğretmenin Tc Numarası: {}\nÖğretmenin Doğum Tarihi:{}\nÖğretmenin Cep Telefon Numarası: {}\nÖğretmenin Branşı: {}".format(self._Ad,self._Soyad,self._Tc,self._Dy,self._Tel,self.__Brans))

class Personel(OkulKayıt):
    def __init__(self,ad,soyad,tc,dy,tel,gorev):
        super().__init__(ad,soyad,tc,dy,tel)
        self.__Gorev=gorev
    def __str__(self):
        print("Personelin Adı: {}\nPersonelin Soyadı: {}\nPersonelin Tc Numarası: {}\nPersonelin Doğum Tarihi:{}\nPersonelin Cep Telefon Numarası: {}\nPersonelin Görevi: {}".format(self._Ad,self._Soyad,self._Tc,self._Dy,self._Tel,self.__Gorev))

sys.__stdout__.write("Programa Hoşgeldiniz...\n")
sys.__stdout__.flush()
sys.__stdout__.write(str(datetime.ctime(datetime.now())))
sys.__stdout__.flush()
print("\n")
#Öğrenci Database
con=sqlite3.connect("Ogrenci.db")
cursor=con.cursor()
sorgu=("Create Table If Not Exists Ogrenci (Ad TEXT,Soyad TEXT,Tc TEXT,Dy TEXT,Tel TEXT,No Int)")
cursor.execute(sorgu,)
con.commit()


#Öğretmen Database
con2=sqlite3.connect("Ogretmen.db")
cursor2=con2.cursor()
cursor2.execute("Create Table If Not Exists Ogretmen(Ad TEXT,Soyad TEXT,Tc TEXT,Dy TEXT,Tel TXT,Brans TXT)")
con2.commit()


#Personel Database
con3=sqlite3.connect("Personel.db")
cursor3=con3.cursor()
cursor3.execute("Create Table If Not Exists personel(Ad TEXT,Soyad TEXT,Tc TEXT,Dy TEXT,Tel TXT,Gorev TXT)")
con3.commit()
#Main Function
while(1):
 print("---işlemler---")
 print("1-Ekle\n2-Sorgula\n3-Güncelle\n4-Sil")
 x=int(input("Hangi İşlemi Yapmak İstiyorsunuz(1/2/3/4) ? : "))
 if (x==1):
  while(1):
   print("""\n---Kategoriler---\n1-Ogrenci\n2-Ogretmen\n3-Personel""")
   print("Çıkmak için 4'e Basınız...")
   sec=int(input("Hangi Kategoride Kayıt Gerçekleştirmek İstiyorsunuz(1/2/3/4): "))
   if (sec==1):
    print("---Öğrenci Kategorisinde Kayıtlı Olanlar---")
    cursor.execute("Select * From Ogrenci")
    record6=cursor.fetchall()
    for i in record6:
     print(i)
    Ad=input("Öğrencinin Adını Yazınız: ")
    Soyad=input("Öğrencinin Soyadını Yazınız: ")
    Tc=input("Öğrencinin Tc Kimlik Numarasını Yazınız: ")
    Dy=input("Öğrencinin Dy Tarihini Yazınız: ")
    Tel=input("Öğrencinin Velisinin Cep Telefon Numarasını Giriniz: ")
    sorgu2="Select * From Ogrenci Where Tc=?"
    cursor.execute(sorgu2,(Tc,))
    kayıt=cursor.fetchone()
    if kayıt==None:
     No=random.randint(0,1000)
     ogrenci=Ogrenci(Ad,Soyad,Tc,Dy,Tel,No)
     ogrenci.__str__()
     cursor.execute("Insert Into Ogrenci Values(?,?,?,?,?,?)",(Ad,Soyad,Tc,Dy,Tel,No))
     con.commit()
     
     break
    else:
        sys.__stderr__.write("\nGirmiş Olduğunuz Bilgilere Sahip Öğrenci Zaten Kayıtlı.\n")
        sys.__stderr__.flush()
        print(kayıt)
        
        break
   elif (sec==2):
    print("\n---Öğretmen Kategorisinde Kayıtlı Olanlar---")
    cursor2.execute("Select * From Ogretmen")
    record4=cursor2.fetchall()
    for i in record4:
     print(i)
    Ad=input("Öğretmenin Adını Yazınız: ")
    Soyad=input("Öğretmenin Soyadını Yazınız: ")
    Tc2=input("Öğretmenin Tc Kimlik Numarasını Yazınız: ")
    Dy=input("Öğretmenin Dy Tarihini Yazınız: ")
    Tel2=input("Öğretmenin Cep Telefon Numarasını Giriniz: ")
    Brans=input("Öğretmenin Branşını Yazınız: ")
    sorgu3="Select * From Ogretmen Where Tc=? or Tel=?"
    cursor2.execute(sorgu3,(Tc2,Tel2))
    kayıt2=cursor2.fetchone()
    if kayıt2==None :
     ogretmen=Ogretmen(Ad,Soyad,Tc2,Dy,Tel2,Brans)
     ogretmen.__str__()
     cursor2.execute("Insert Into Ogretmen Values(?,?,?,?,?,?)",(Ad,Soyad,Tc2,Dy,Tel2,Brans))
     con2.commit()
     
     break
    else:
        sys.__stderr__.write("\nGirmiş Olduğunuz Bilgilere Sahip Öğretmen Zaten Kayıtlı.\n")
        sys.__stderr__.flush()
        print(kayıt2)
        
        break
   elif (sec==3):
     print("\n---Personel Kategorisinde Kayıtlı Olanlar---")
     cursor3.execute("Select * From Personel")
     record5=cursor3.fetchall()
     for i in record5:
       print(i)
     Ad=input("Personelin Adını Yazınız: ")
     Soyad=input("Personelin Soyadını Yazınız: ")
     Tc3=input("Personelin Tc Kimlik Numarasını Yazınız: ")
     Dy=input("Personelin Dy Tarihini Yazınız: ")
     Tel3=input("Personelin Cep Telefon Numarasını Giriniz: ")
     Gorev=input("Personelin Görevini Yazınız: ")
     sorgu4="Select * From personel Where Tc=? or Tel=?"
     cursor3.execute(sorgu4,(Tc3,Tel3))
     kayıt3=cursor3.fetchone()
     if kayıt3==None:
      personel=Personel(Ad,Soyad,Tc3,Dy,Tel3,Gorev)
      personel.__str__()
      cursor3.execute("Insert Into personel Values(?,?,?,?,?,?)",(Ad,Soyad,Tc3,Dy,Tel3,Gorev))
      con3.commit()
     else:
        sys.__stderr__.write("\nGirmiş Olduğunuz Bilgilere Sahip Personel Zaten Kayıtlı.\n")
        sys.__stderr__.flush()
        print(kayıt3)
        break
   elif (sec==4):
        break
   else:
        sys.__stderr__.write("\nYanlış Değer Girildi...\n")
        sys.__stderr__.flush()


 #Sorgulama 
 elif (x==2):
     while(1):
      print("""\n---Kategoriler---\n1-Ogrenci\n2-Ogretmen\n3-Personel""")
      print("Çıkış Yapmak için 4'e Basınız...")
      sec2=int(input("Hangi Kategoride Sorgulama Yapmak İstiyorsunuz(1/2/3/4) ? : "))
      if (sec2==4):
        break
      if (sec2==1):
        ter=input("Sadece Öğrencinin Adı Mı Girmek İstiyorsunuz(E/H) ? : ")
        if (ter=="H" or ter=="h"):
         Ad=input("Sorgulamak İstediğiniz Öğrencinin Adını Yazınız: ")
         Soyad=input("Sorgulamak İstediğiniz Öğrencinin Soyadını Yazınız: ")
         cursor.execute("Select * From Ogrenci Where Ad=? and Soyad=?",(Ad,Soyad))
         kayıt=cursor.fetchall()
         if kayıt==None:
            print("Verilen Bilgilere Göre Böyle Bir Öğrenci Bulunmamaktadır.\a")
            break
         else:
            print(kayıt)
            break
        elif (ter=="E" or ter=='e'):
            Ad=input("Sorgulamak İstediğiniz Öğrencinin Adını Yazınız: ")
            cursor.execute("Select * From Ogrenci Where Ad=?",(Ad,))
            record=cursor.fetchall()
            if record==None:
                  print("Verilen Bilgilere Göre Böyle Bir Öğrenci Bulunmamaktadır.\a")
                  break
            else:
                for i in record:
                 print(i)
                break

      elif (sec2==2):
        ter2=input("Sadece Öğretmenin Adı Mı Girmek İstiyorsunuz(E/H) ? : ")
        if (ter2=="H" or ter2=="h"):
         Ad=input("Sorgulamak İstediğiniz Öğretmenin Adını Yazınız: ")
         Soyad=input("Sorgulamak İstediğiniz Öğretmenin Soyadını Yazınız: ")
         cursor2.execute("Select * From Ogretmen Where Ad=? and Soyad=?",(Ad,Soyad))
         kayıt2=cursor2.fetchall()
         if kayıt2==None:
            print("Verilen Bilgilere Göre Böyle Bir Öğretmen Bulunmamaktadır.\a")
            break
         else:
            print(kayıt2)
            break
        elif (ter2=='E' or ter2=='e'):
            Ad=input("Sorgulamak İstediğiniz Öğretmenin Adını Yazınız: ")
            cursor2.execute("Select * From Ogretmen Where Ad=?",(Ad,))
            record2=cursor2.fetchall()
            if record2==None:
                print("Verilen Bilgilere Göre Böyle Bir Öğretmen Bulunmamaktadır.\a")
                break
            else:
               print(record2)
               break
      elif (sec2==3):
        ter2=input("Sadece Personelin Adı Mı Girmek İstiyorsunuz(E/H) ? : ")
        if (ter2=="H" or ter2=="h"): 
         Ad=input("Sorgulamak İstediğiniz Personel Adını Yazınız: ")
         Soyad=input("Sorgulamak İstediğiniz Personel Soyadını Yazınız: ")
         cursor3.execute("Select * From personel Where Ad=? and Soyad=?",(Ad,Soyad))
         kayıt3=cursor3.fetchall()
         if kayıt3==None:
            print("Verilen Bilgilere Göre Böyle Bir Personel Bulunmamaktadır.\a")
            break
         else:
            print(kayıt3)
            break
        else:
            Ad=input("Sorgulamak İstediğiniz Personel Adını Yazınız: ")
            cursor3.execute("Select * From personel Where Ad=?",(Ad,))
            record3=cursor3.fetchall()
            if record3==None:
              print("Verilen Bilgilere Göre Böyle Bir Personel Bulunmamaktadır.\a")
              break
            else:
               print(record3)
               break

      else:
        sys.__stderr__.write("\nYanlış Değer Girdiniz...\n")
        sys.__stderr__.flush()

#Güncelleme
 elif (x==3):
      print("---Öğrenci Kategorisinde Kayıtlı Olanlar---")
      cursor.execute("Select * From Ogrenci")
      record6=cursor.fetchall()
      for i in record6:
        print(i)
      print("\n---Öğretmen Kategorisinde Kayıtlı Olanlar---")
      cursor2.execute("Select * From Ogretmen")
      record4=cursor2.fetchall()
      for i in record4:
        print(i)
      print("\n---Personel Kategorisinde Kayıtlı Olanlar---")
      cursor3.execute("Select * From Personel")
      record5=cursor3.fetchall()
      for i in record5:
        print(i)
      Tc=input("Güncelleme Yapmak İstediğiniz Kişinin TC Kimlik Numarasını  Yazınız: ")
      while(1):
       print("""\n---Kategoriler---\n1-Ogrenci\n2-Ogretmen\n3-Personel""")
       print("Çıkmak için 4'e Basınız ...")
       sec3=int(input("Hangi Kategoride Güncelleme İşlemi Yapmak İstiyorsunuz(1/2/3/4) ? : "))
       if (sec3==1):
        while(1):
         
         cursor.execute("Select * From Ogrenci where Tc=?",(Tc,))
         record=cursor.fetchall()
         if record!=None:
          print("""---İşlemler---\n1-Ad\n2-Soyad\n3-Doğum Tarihi\n4-Cep Telefon Numarası\n5-Öğrencinin Branşı \n6-TC Kimlik Numarası\n7-Çıkış""")
          sec5=int(input("Değiştirmek İstediğiniz Öğrencinin Hangi Verisini Güncellemek İstiyorsunuz(1/2/3/4/5/6/7)? : "))
          if (sec5==1):
            New_ad=input("Öğrencinin Yeni Adını Yazınız: ")
            cursor.execute("Update Ogrenci Set Ad=? Where Tc=?",(New_ad,Tc))
            con.commit()
            cursor.execute("Select * From Ogrenci where Tc=?",(Tc,))
            kayıt=cursor.fetchall()
            print(kayıt)
            
          elif (sec5==2):
            New_Soyad=input("Öğrencinin Yeni Soyadını Yazınız: ")
            cursor.execute("Update Ogrenci set Soyad=?  where Tc=?",(New_Soyad,Tc))
            con.commit()
            cursor.execute("Select * From Ogrenci where Tc=?",(Tc,))
            kayıt=cursor.fetchall()
            print(kayıt)
            
          elif (sec5==3):
             New_Dy=input("Öğrencinin Yeni Doğum Tarihini Giriniz: ")
             cursor.execute("Update Ogrenci set Dy=?  where Tc=?",(New_Dy,Tc))
             con.commit()
             cursor.execute("Select * From Ogrenci where Tc=?",(Tc,))
             kayıt=cursor.fetchall()
             print(kayıt)
             
          elif (sec5==4):
            New_Tel=input("Öğrencinin Yeni Telefon Numarasını Giriniz: ")
            cursor.execute("Update Ogrenci set Tel=?  where Tc=?",(New_Tel,Tc))
            con.commit()
            cursor.execute("Select * From Ogrenci where Tc=?",(Tc,))
            kayıt=cursor.fetchall()
            print(kayıt)
            
          elif (sec5==5):
            New_No=input("Öğrencinin Yeni Okul Numarasını Yazınız: ")
            cursor.execute("Update Ogrenci set No=?  where Tc=?",(New_No,Tc))
            con.commit()
            cursor.execute("Select * From Ogrenci where Tc=?",(Tc,))
            kayıt=cursor.fetchall()
            print(kayıt)
            
          elif (sec5==6):
            New_Tc=input("Öğrencinin Yeni Tc Kimlik Numarasını Yazınız: ")
            cursor.execute("Update Ogrenci set Tc=?  where Tc=?",(New_Tc,Tc))
            con.commit()
            cursor.execute("Select * From Ogrenci where Tc=?",(New_Tc,))
            kayıt=cursor.fetchall()
            print(kayıt)
            
          elif (sec5==7):
            break
          else:
            sys.__stderr__.write("\nYanlış Değer Girildi...\n")
            sys.__stderr__.flush()
        else:
            sys.__stderr__.write("\nBu TC Kimlik Numarasına Sahip Öğrenci Bulunmamaktadır.\n")
            sys.__stderr__.flush()
            
       elif (sec3==2):
          while(1):
          
           cursor2.execute("Select * From Ogretmen where Tc=?",(Tc,))
           record2=cursor2.fetchall()
           if record2!=None:
             print("""---İşlemler---\n1-Ad\n2-Soyad\n3-Doğum Tarihi\n4-Cep Telefon Numarası\n5-Öğretmenin Branşı \n6-TC Kimlik Numarası\n7-Çıkış""")
             sec6=int(input("Değiştirmek İstediğiniz Öğretmenin Hangi Verisini Güncellemek İstiyorsunuz(1/2/3/4/5/6/7)? : "))
             if (sec6==1):
                New_ad2=input("Öğretmenin Yeni Adını Yazınız: ")
                cursor2.execute("Update Ogretmen Set Ad= ? Where Tc=?",(New_ad2,Tc))
                con2.commit()
                cursor2.execute("Select * From Ogretmen Where Tc=?",(Tc,))
                kayıt2=cursor2.fetchall()
                print(kayıt2)
                
             elif (sec6==2):
                New_Soyad2=input("Öğretmenin Yeni Soyadını Yazınız: ")
                cursor2.execute("Update Ogretmen Set Soyad= ? Where Tc=?",(New_Soyad2,Tc))
                con2.commit()
                cursor2.execute("Select * From Ogretmen Where Tc=?",(Tc,))
                kayıt2=cursor2.fetchall()
                print(kayıt2)
                
             elif (sec6==3):
                New_Dy2=input("Öğretmenin Yeni Doğum Tarihini Yazınız: ")
                cursor2.execute("Update Ogretmen Set Dy= ? Where Tc=?",(New_Dy2,Tc))
                con2.commit()
                cursor2.execute("Select * From Ogretmen Where Tc=?",(Tc,))
                kayıt2=cursor2.fetchall()
                print(kayıt2)
                
             elif (sec6==5):
                New_Brans2=input("Öğretmenin Yeni Branşını Yazınız: ")
                cursor2.execute("Update Ogretmen Set Brans=? Where Tc=?",(New_Brans2,Tc))
                con2.commit()
                cursor2.execute("Select * From Ogretmen Where Tc=?",(Tc,))
                kayıt2=cursor2.fetchall()
                print(kayıt2)
                
             elif (sec6==4):
                New_Tel2=input("Öğretmenin Yeni Cep Telefon Numarasını  Yazınız: ")
                cursor2.execute("Update Ogretmen Set Tel=? Where Tc=?",(New_Tel2,Tc))
                con2.commit()
                cursor2.execute("Select * From Ogretmen Where Tc=?",(Tc,))
                kayıt2=cursor2.fetchall()
                print(kayıt2)
                
             elif (sec6==6):
                New_Tc2=input("Öğretmenin Yeni TC Kimlik Numarasını Yazınız: ")
                cursor2.execute("Update Ogretmen Set Tc=? Where Tc=?",(New_Tc2,Tc))
                con2.commit()
                cursor2.execute("Select * From Ogretmen Where Tc=?",(Tc,))
                kayıt2=cursor2.fetchall()
                print(kayıt2)
             elif (sec6==7):
                break
                
             else:
                sys.__stderr__.write("\nYanlış Değer Girildi...\n")
                sys.__stderr__.flush()
           else:
                sys.__stderr__.write("Bu Tc Kimlik Numarasına Sahip Olan Öğretmen Bulunmamaktadır.")
                sys.__stderr__.flush()
                
                    
       elif (sec3==3):
           
           cursor3.execute("Select * From Personel where Tc=?",(Tc,))
           record3=cursor3.fetchall()
           if record3!=None:
             print("""---İşlemler---\n1-Ad\n2-Soyad\n3-Doğum Tarihi\n4-Cep Telefon Numarası\n5-Öğretmenin Branşı \n6-TC Kimlik Numarası\n7-Çıkış""")
             sec7=int(input("Değiştirmek İstediğiniz Personelin Hangi Verisini Güncellemek İstiyorsunuz(1/2/3/4/5/6/7)? : "))
             if (sec7==1):
                New_Ad3=input("Personelin Yeni Adını Yazınız: ")
                cursor3.execute("Update Personel Set Ad= ? Where Tc=?",(New_Ad3,Tc))
                con3.commit()
                cursor3.execute("Select * From Personel Where Tc=?",(Tc,))
                kayıt3=cursor3.fetchall()
                print(kayıt3)
                
             elif (sec7==2):
                New_Soyad3=input("Personelin Yeni Soyadını Yazınız: ")
                cursor3.execute("Update Personel Set Soyad= ? Where Tc=?",(New_Soyad3,Tc))
                con3.commit()
                cursor3.execute("Select * From Personel Where Tc=?",(Tc,))
                kayıt3=cursor3.fetchall()
                print(kayıt3)
                
             elif (sec7==3):
                New_Dy3=input("personelin Yeni Doğum Tarihini Yazınız: ")
                cursor3.execute("Update Personel Set Dy= ? Where Tc=?",(New_Dy3,Tc))
                con3.commit()
                cursor3.execute("Select * From Personel Where Tc=?",(Tc,))
                kayıt3=cursor3.fetchall()
                print(kayıt3)
                
             elif (sec7==5):
                New_Gorev3=input("Personelin Yeni Görevini Yazınız: ")
                cursor3.execute("Update Personel Set Gorev=? Where Tc=?",(New_Gorev3,Tc))
                con3.commit()
                cursor3.execute("Select * From Personel Where Tc=?",(Tc,))
                kayıt3=cursor3.fetchall()
                print(kayıt3)
                
             elif (sec7==4):
                New_Tel3=input("Personelin Yeni Cep Telefon Numarasını  Yazınız: ")
                cursor3.execute("Update Personel Set Tel=? Where Tc=?",(New_Tel3,Tc))
                con3.commit()
                cursor3.execute("Select * From Personel Where Tc=?",(Tc,))
                kayıt3=cursor3.fetchall()
                print(kayıt3)
                
             elif (sec7==6):
                New_Tc3=input("Öğretmenin Yeni TC Kimlik Numarasını Yazınız: ")
                cursor3.execute("Update Personel Set Tc=? Where Tc=?",(New_Tc3,Tc))
                con3.commit()
                cursor3.execute("Select * From Personel Where Tc=?",(Tc,))
                kayıt3=cursor3.fetchall()
                print(kayıt3)
             elif (sec7==7):
                break
             else:
                sys.__stderr__.write("\nYanlış Değer Girildi...\n")
                sys.__stderr__.flush()
           else:
                sys.__stderr__.write("Bu Tc Kimlik Numarasına Sahip Olan Öğretmen Bulunmamaktadır.")
                sys.__stderr__.flush()
                break
       elif (sec3==4):
        break
       else:
        sys.__stderr__.write("\nYanlış Değer Girdiniz...\n")
        sys.__stderr__.flush()

#Silme
 elif (x==4):
      while(1):
       print("""\n---Kategoriler---\n1-Ogrenci\n2-Ogretmen\n3-Personel""")
       print("Çıkmak İçin 4'e Basınız...")
       sec4=int(input("Hangi Kategoride Silme İşlemi Gerçekleştirmek İstiyorsunuz(1/2/3/4) ? : "))
       if (sec4==1):
        cursor.execute("Select * From Ogrenci")
        kayıt=cursor.fetchall()
        for i in kayıt:
            print(i)
        Ad=input("Silmek İstediğiniz Öğrencinin Adını Yazınız : ")
        Soyad=input("Silmek İstediğinz Öğrencinin Soyadını Yazınız: ")
        cursor.execute("Delete From Ogrenci Where Ad=? and Soyad=?",(Ad,Soyad))
        con.commit()
        cursor.execute("Select * From Ogrenci")
        kayıt=cursor.fetchall()
        for i in kayıt:
            print(i)
       elif sec4==2:
        cursor2.execute("Select * From Ogretmen")
        kayıt2=cursor2.fetchall()
        for i in kayıt2:
            print(i)
        Ad2=input("Silmek İstediğiniz Öğretmen Adını Yazınız : ")
        Soyad2=input("Silmek İstediğinz Öğretmen Soyadını Yazınız: ")
        cursor2.execute("Delete From Ogretmen Where Ad=? and Soyad=?",(Ad2,Soyad2))
        con2.commit()
        cursor2.execute("Select * From Ogretmen")
        kayıt2=cursor2.fetchall()
        for i in kayıt2:
            print(i)
       elif sec4==3:
        cursor3.execute("Select * From Personel")
        kayıt3=cursor3.fetchall()
        for i in kayıt3:
            print(i)
        Ad3=input("Silmek İstediğiniz Personelin Adını Yazınız : ")
        Soyad3=input("Silmek İstediğinz Personelin Soyadını Yazınız: ")
        cursor3.execute("Delete From Personel Where Ad=? and Soyad=?",(Ad3,Soyad3))
        con3.commit()
        cursor3.execute("Select * From Personel")
        kayıt3=cursor3.fetchall()
        for i in kayıt3:
            print(i)
       elif sec4==4:
        break
       else:
        sys.__stderr__.write("\nYanlış Değer Girdiniz...\n")
        sys.__stderr__.flush()
 else:
      sys.__stderr__.write("\nYanlış Değer Girdiniz...\a\n")
      sys.__stderr__.flush()
 
 while(1):
     sec2=input("Devam Etmek İstiyor Musunuz(E/H) ? : ")
     if (sec2=="E" or sec2=='e'):
        sys.stdout.write("\nDevam Ediliyor...\n")
        sys.stdout.flush()
        time.sleep(3)
        break
     elif (sec2=='H' or sec2=='h'):
        print("Yine Bekleriz...")
        con.close()
        con2.close()
        con3.close()
        time.sleep(4)
        sys.exit()
     else:
        sys.__stderr__.write("\nYanlış Girildi...")
        sys.__stderr__.flush()
        os.abort()

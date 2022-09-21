import sqlite3,time,sys

con=sqlite3.connect("Cat.db")
cursor=con.cursor()
cursor.execute("Create Table If Not Exists Cat(Ad TEXT,Yaş INT,Cins TEXT,KİLO FLOAT)")
con.commit()
cursor.execute("Create Table If Not Exists Dog(Ad TEXT,Yaş INT,Cins TEXT,Kilo FLOAT)")
con.commit()
while(1):
 print("1-Köpek\n2-Kedi")
 z=input("Hangi Hayvan Türünde İşlem Gerçekleştirmek İstiyorsunuz? : ")
 if (z=="Kedi" or z=="kedi" or z=='2'):
  while(1):
   print("---İşlemler---\n1-Ekle\n2-Sorgula\n3-Güncelle\n4-Sil\n5-Göster\n6-Çıkış")
   x=input("Hangi İşlemi Yapmak İstiyorsunuz? : ")
   if (x=='1' or x=="Ekle" or x=="ekle"):
    while(1):
     Ad=input("Kedinizin Adı: ")
     Yaş=int(input("Kedinizin Yaşı: "))
     Cins=input("Kedinizin Cinsi: ")
     Kilo=float(input("Kedinizin Kilosu: "))
     cursor.execute("Insert Into Cat Values(?,?,?,?)",(Ad,Yaş,Cins,Kilo))
     con.commit()
     cursor.execute("Select * From Cat where Ad=?",(Ad,))
     a=cursor.fetchall()
     print(a)
     ter=input("Eklemeye Devam Etmek İstiyor Musunuz(E/H) ? : ")
     if (ter=='e' or ter=="E"):
      print("Devam Ediliyor...")
      time.sleep(2)
     elif (ter=='h' or ter=="H"):
      break
     else:
      print("Yanlış Girdiniz...")
      break
  
   elif (x=='2' or x=="Sorgula" or x=="sorgula"):
    while(1):
     Ad=input("Kedinizin Adı:")
     cursor.execute("Select * From Cat where Ad=?",(Ad,))
     a=cursor.fetchall()
     print(a)
     ter=input("Sorgulamaya Devam Etmek İstiyor Musunuz(E/H) ? : ")
     if (ter=='e' or ter=="E"):
      print("Devam Ediliyor...")
      time.sleep(2)
     elif (ter=='h' or ter=="H"):
      break
     else:
      print("Yanlış Girdiniz...")
      break
   elif (x=='3' or x=="Güncelle" or x=="güncelle"):
    while(1):
     print("1-Adı\n2-Yaşı\n3-Cinsi\n4-Kilosu")
     y=input("Hangi Veriyi Değiştirmek İstiyorsunuz? : ")
     if (y=="2" or y=="Yaşı" or y=="Yaşi" or y=="Yaşı" or y=="yasi"):
      Ad=input("Kedinizin Adı: ")
      New_Yas=int(input("Kedinizin Yeni Yaşı: "))
      Ad=input("Kedinizin Eski Adı: ")
      New_Ad=input("Kedinizin Yeni Adı: ")
      cursor.execute("Update Cat set Ad=? Where Ad=?",(New_Ad,Ad))
      con.commit()
      cursor.execute("Select * From Cat where Ad=?",(New_Ad,))
      a=cursor.fetchall()
      print(a)
     elif (y=='3' or y=="Cinsi" or y=="cinsi"):
      Ad=input("Kedinizin Adı: ")
      New_Cins=input("Kedinizin Yeni Cinsi: ")
      cursor.execute("Update Cat set Cins=? where Ad=?",(New_Cins,Ad))
      con.commit()
      cursor.execute("Select * From Cat where Ad=?",(Ad,))
      a=cursor.fetchall()
      print(a)
     elif (y=='4' or y=="Kilosu" or y=="kilosu"):
      Ad=input("Kedinizin Adı: ")
      New_Kilo=float(input("Kedinizin Yeni Kilosu: "))
      cursor.execute("Update Cat Set KİLO=? where Ad=?",(New_Kilo,Ad))
      con.commit()
      cursor.execute("Select * From Cat where Ad=?",(Ad,))
      a=cursor.fetchall()
      for i in a:
        print(i)
    sec=input("Güncelleme İşlemine Devam Etmek İstiyor Musunuz(E/H)? : ")
    if (sec=='E' or sec=='e'):
       print("Devam Ediliyor...")
       time.sleep(3)
    elif (sec=='H' or sec=='h'):
       break
    else:
       print("Yanlış Girdiniz...")
       break
   elif (x=='4' or x=="Sil" or x=="sil"):
    while(1):
     Ad=input("Kedinizin Adı: ")
     cursor.execute("Delete From Cat Where Ad=?",(Ad,))
     con.commit()
     cursor.execute("Select * From Cat",)
     a=cursor.fetchall()
     for i in a:
        print(i)
     ter=input("Silmeye Devam Etmek İstiyor Musunuz(E/H) ? : ")
     if(ter=="E" or ter=='e'):
        print("Devam Ediliyor...")
        time.sleep(2)
     elif (ter=='H' or ter=='h'):
        break
     else:
        print("Yanlış Girdiniz...")
        break
   elif (x=='5' or x=="Göster" or x=="göster"):
    cursor.execute("Select * From Cat")
    a=cursor.fetchall()
    for i in a:
        print(i)
   elif (x=='6' or x=="Çıkış" or x=="çıkış"):
    break
 elif (z=='1' or z=="Köpek" or z=="köpek"):
  while(1):
   print("---İşlemler---\n1-Ekle\n2-Sorgula\n3-Güncelle\n4-Sil\n5-Göster\n6-Çıkış")
   x=input("Hangi İşlemi Yapmak İstiyorsunuz? : ")
   if (x=='1' or x=="Ekle" or x=="ekle"):
    while(1):
     Ad=input("Köpeğinizin Adı: ")
     Yaş=int(input("Köpeğinizin Yaşı: "))
     Cins=input("Köpeğinizin Cinsi: ")
     Kilo=float(input("Köpeğinizin Kilosu: "))
     cursor.execute("Insert Into Dog Values(?,?,?,?)",(Ad,Yaş,Cins,Kilo))
     con.commit()
     cursor.execute("Select * From Dog where Ad=?",(Ad,))
     a=cursor.fetchall()
     print(a)
     ter=input("Eklemeye Devam Etmek İstiyor Musunuz(E/H) ? : ")
     if (ter=='e' or ter=="E"):
      print("Devam Ediliyor...")
      time.sleep(2)
     elif (ter=='h' or ter=="H"):
      break
     else:
      print("Yanlış Girdiniz...")
      break
  
   elif (x=='2' or x=="Sorgula" or x=="sorgula"):
    while(1):
     Ad=input("Köpeğinizin Adı:")
     cursor.execute("Select * From Dog where Ad=?",(Ad,))
     a=cursor.fetchall()
     print(a)
     ter=input("Sorgulamaya Devam Etmek İstiyor Musunuz(E/H) ? : ")
     if (ter=='e' or ter=="E"):
      print("Devam Ediliyor...")
      time.sleep(2)
     elif (ter=='h' or ter=="H"):
      break
     else:
      print("Yanlış Girdiniz...")
      break
   elif (x=='3' or x=="Güncelle" or x=="güncelle"):
    while(1):
     print("1-Adı\n2-Yaşı\n3-Cinsi\n4-Kilosu")
     y=input("Hangi Veriyi Değiştirmek İstiyorsunuz? : ")
     if (y=="2" or y=="Yaşı" or y=="Yaşi" or y=="Yaşı" or y=="yasi"):
      Ad=input("Köpeğinizin Adı: ")
      New_Yas=int(input("Köpeğinizin Yeni Yaşı: "))
      cursor.execute("Update Dog set Yaş=? Where Ad=?",(New_Yas,Ad))
      con.commit()
      cursor.execute("Select * From Dog where Ad=?",(Ad,))
      a=cursor.fetchall()
      print(a)
     elif (y=="1" or y=="Adı" or y=="adı" or y=="Adi" or y=="adi"):
      Ad=input("Köpeğinizin Eski Adı: ")
      New_Ad=input("Köpeğinizin Yeni Adı: ")
      cursor.execute("Update Dog set Ad=? Where Ad=?",(New_Ad,Ad))
      con.commit()
      cursor.execute("Select * From Dog where Ad=?",(New_Ad,))
      a=cursor.fetchall()
      print(a)
     elif (y=='3' or y=="Cinsi" or y=="cinsi"):
      Ad=input("Köpeğinizin Adı: ")
      New_Cins=input("Köpeğinizin Yeni Cinsi: ")
      cursor.execute("Update Dog set Cins=? where Ad=?",(New_Cins,Ad))
      con.commit()
      cursor.execute("Select * From Dog where Ad=?",(Ad,))
      a=cursor.fetchall()
      print(a)
     elif (y=='4' or y=="Kilosu" or y=="kilosu"):
      Ad=input("Köpeğinizin Adı: ")
      New_Kilo=float(input("Köpeğinizin Yeni Kilosu: "))
      cursor.execute("Update Dog Set Kilo=? where Ad=?",(New_Kilo,Ad))
      con.commit()
      cursor.execute("Select * From Dog where Ad=?",(Ad,))
      a=cursor.fetchall()
      for i in a:
        print(i)
     sec=input("Güncelleme İşlemine Devam Etmek İstiyor Musunuz(E/H)? : ")
     if (sec=='E' or sec=='e'):
       print("Devam Ediliyor...")
       time.sleep(3)
     elif (sec=='H' or sec=='h'):
       break
     else:
       print("Yanlış Girdiniz...")
       break
   elif (x=='4' or x=="Sil" or x=="sil"):
    while(1):
     Ad=input("Köpeğinizin Adı: ")
     cursor.execute("Delete From Dog Where Ad=?",(Ad,))
     con.commit()
     cursor.execute("Select * From Dog",)
     a=cursor.fetchall()
     for i in a:
        print(i)
     ter=input("Silmeye Devam Etmek İstiyor Musunuz(E/H) ? : ")
     if(ter=="E" or ter=='e'):
        print("Devam Ediliyor...")
        time.sleep(2)
     elif (ter=='H' or ter=='h'):
        break
     else:
        print("Yanlış Girdiniz...")
        break
   elif (x=='5' or x=="Göster" or x=="göster"):
    cursor.execute("Select * From Dog")
    a=cursor.fetchall()
    for i in a:
        print(i)
   elif (x=='6' or x=="Çıkış" or x=="çıkış"):
    break
 else:
    print("Yanlış Girdiniz...")
 while(1):
  sec=input("Programa Devam Etmek İstiyor Musunuz(E/H) ? : ")
  if (sec=='E' or sec=='e'):
    print("Devam Ediliyor...")
    time.sleep(3)
    break
  elif (sec=='H' or sec=='h'):
    print("Yine Bekleriz...")
    con.close()
    sys.exit()
  else:
    sys.__stderr__.write("\nYanlış Girdiniz...\n")
    sys.__stderr__.flush()
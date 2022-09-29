import sqlite3,sys,time

class Kentkart():
    def __init__(self,Balance):
      self.Balance=Balance

    def OzelKayıtEkleme(self,Balance):
      Name=input("Name: ")
      Surname=input("Surname: ")
      Tc=input("Number of Your TC identify: ")
      No=input("Number of Your Card: ")
      cursor.execute("Insert Into Ozel Values(?,?,?,?,?)",(Name,Surname,Tc,No,Balance))
      con.commit()
      cursor.execute("Select * From Ozel Where TC=? and Kart=? ",(Tc,No))
      result=cursor.fetchall()
      if result!=0:
        print("Your Process Was Realized Successfully.")
      elif result==0:
        print("Your Process Wasn't Realized Successfully.")

    def GenelKayıtEkleme(self,Balance):
       No=input("Number of Your Card: ")
       cursor.execute("Insert Into Genel Values(?,?)",(No,Balance))
       con.commit()
       cursor.execute("Select * From Genel Where Kart=?",(No,))
       result=cursor.fetchall()
       if result!=0:
        print("Your Process Was Realized Successfully.")
        
       elif result==0:
        print("Your Process Wasn't Realized Successfully.")
    
    def OzelKayıtSilme(self):
        No=input("Number of Kentkart: ")
        cursor.execute("Select * From Ozel Where Kart=?",(No,))
        result=cursor.fetchall()
        print(result)
        cursor.execute("Delete From Ozel Where Kart=?",(No,))
        con.commit()
        cursor.execute("Select * From Ozel Where Kart=?",(No,))
        result=cursor.fetchall()
        print(result)
        if result==0:
            print("Register wasn't Deleted Successfully.")
        elif result!=0:
            print("Register was Deleted Successfully.")

    def GenelKayıtSilme(self):
        No=input("Number of Kentkart: ")
        cursor.execute("Delete From Ozel Where Kart=?",(No,))
        con.commit()
        cursor.execute("Select * From Ozel Where Kart=?",(No,))
        result=cursor.fetchall()
        if result!=0:
            print("Register was Deleted Successfully.")
        elif result==0:
            print("Register wasn't Deleted Successfully.")
    
    def OzelKayıtGuncelleme(self):
        No=input("Number of Kentkart which is wanted to change: ")
        Tc=input("Number of Your identity: ")
        cursor.execute("Select * From Ozel Where Kart=? and TC=?",(No,Tc))
        result2=cursor.fetchall()
        if result2==0:
            print("Register Not Found")
        elif result2!=0:
          print("1-Name\n2-Surname\n3-İdentity\n4-Number of Card \n5-Update Your Balance in Card")
          sec=int(input("Which Informations Do You Want To Change(1/2/3/4/5)? : "))
          if (sec==4):
            New_No=input("Number of Kentkart which is wanted to change: ")
            cursor.execute("Update Ozel set Kart=? Where Kart=?",(New_No,No))
            con.commit()
            cursor.execute("Select * From Ozel Where Kart=? ",New_No)
            result=cursor.fetchall()
            if result!=0:
                print("Your Process was realized Successfully.")
            elif result==0:
                print("Your Process wasn't realized Successfully.")
          elif (sec==1):
            New_Name=input("New Name: ")
            cursor.execute("Update Ozel set Name=? Where Kart=?",(New_Name,No))
            con.commit()
            cursor.execute("Select * From Ozel Where Kart=? ",No)
            result=cursor.fetchall()
            if result!=0:
                print("Your Process was realized Successfully.")
            elif result==0:
                print("Your Process wasn't realized Successfully.")
          elif (sec==2):
            New_Surname=input("New Surname: ")
            cursor.execute("Update Ozel set Surname=? Where Kart=?",(New_Surname,No))
            con.commit()
            cursor.execute("Select * From Ozel Where Kart=? ",No)
            result=cursor.fetchall()
            if result!=0:
                print("Your Process was realized Successfully.")
            elif result==0:
                print("Your Process wasn't realized Successfully.")
          elif (sec==3):
            New_identity=input("Number of new identity: ")
            cursor.execute("Update Ozel set TC=? Where Kart=?",(New_identity,No))
            con.commit()
            cursor.execute("Select * From Ozel Where Kart=? ",No)
            result=cursor.fetchall()
            if result!=0:
                print("Your Process was realized Successfully.")
            elif result==0:
                print("Your Process wasn't realized Successfully.")
          elif (sec==5):
            New_Balance=input("New Balance: ")
            cursor.execute("Update Ozel set Balance=? Where Kart=?",(New_Balance,No))
            con.commit()
            cursor.execute("Select * From Ozel Where Kart=? ",(No,))
            result=cursor.fetchall()
            if result!=0:
                print("Your Process was realized Successfully.")
            elif result==0:
                print("Your Process wasn't realized Successfully.")
          else:
            pass
          cursor.execute("Select * From Ozel Where Kart=? and TC=?",(No,Tc))
          data=cursor.fetchall()
          for i in data:
            print(i)

    def GenelKayıtGuncelleme(self):
        No=input("Number of Kentkart which is wanted to change: ")
        cursor.execute("Select * From Genel Where Kart=? ",(No,))
        result2=cursor.fetchall()
        if result2==0:
            print("Register Not Found")
        elif result2!=0:
          print("1-Number of Card\n2-Update Your Balance in Card")
          sec=int(input("Which Informations Do You Want To Change(1/2)? : "))
          if (sec==1):
            New_No=input("Number of Kentkart which is wanted to change: ")
            cursor.execute("Update Genel set Kart=? Where Kart=?",(New_No,No))
            con.commit()
            cursor.execute("Select * From Genel Where Kart=? ",New_No)
            result=cursor.fetchall()
            if result!=0:
                print("Your Process was realized Successfully.")
            elif result==0:
                print("Your Process wasn't realized Successfully.")
          elif (sec==2):
            New_Balance=input("New Balance: ")
            cursor.execute("Update Genel set Balance=? Where Kart=?",(New_Balance,No))
            con.commit()
            cursor.execute("Select * From Genel Where Kart=? ",(No,))
            result=cursor.fetchall()
            if result!=0:
                print("Your Process was realized Successfully.")
            elif result==0:
                print("Your Process wasn't realized Successfully.")
          else:
            pass
          cursor.execute("Select * From Genel Where Kart=?",(No,))
          data=cursor.fetchall()
          for i in data:
            print(i)
    def OzelBakiyeYukleme(self,Balance):
        No=input("Number of Kentkart: ")
        Tc=input("Number of Your identity: ")
        cursor.execute("Select Balance From Ozel Where Kart=? and TC=?",(No,Tc))
        balance=cursor.fetchone()
        Balance=balance[0]
        cursor.execute("Select * From Ozel where Kart=? and TC=?",(No,Tc))
        result2=cursor.fetchall()
        if result2==0:
            print("Register Not Found")
        elif result2!=0:
         while(1):
          amount=float(input("What is the amount which wanted to deposit by you ? : "))
          if amount>0:
            break

         Balance +=amount
         cursor.execute("Update Ozel set Balance=? Where Kart=?",(Balance,No))
         con.commit()
         cursor.execute("Select * From Ozel Where Balance=? and Kart=?",(Balance,No))
         result=cursor.fetchall()
         if result!=0:
            print("Your Process was realized successfully.")
            cursor.execute("Select Balance From Ozel Where Kart=? ",(No,))
            balance=cursor.fetchone()
            print("Yeni Bakiyeniz: {}".format(balance[0]))
         elif result==0:
            print("Your Process wasn't realized successfully.")
            cursor.execute("Select Balance From Ozel Where Kart=? ",(No,))
            balance=cursor.fetchone()
            print("Bakiyeniz: {}".format(balance[0]))

    def GenelBakiyeYukleme(self,Balance):
        No=input("Number of Kentkart: ")
        cursor.execute("Select Balance From Genel Where Kart=?",(No,))
        balance=cursor.fetchone()
        Balance=balance[0]
        cursor.execute("Select * From Genel Where Kart=?",(No,))
        result2=cursor.fetchall()
        if result2==0:
            print("Register Not Found")
        elif result2!=0:
         while(1):
          amount=float(input("What is the amount which wanted to deposit by you ? : "))
          if amount>0:
            break
         Balance +=amount
         cursor.execute("Update Genel set Balance=? Where Kart=?",(Balance,No))
         con.commit()
         cursor.execute("Select * From Genel Where Balance=? and Kart=?",(Balance,No))
         result=cursor.fetchall()
         if result!=0:
            print("Your Process was realized successfully.")
            cursor.execute("Select Balance From Genel Where Kart=? ",(No,))
            balance=cursor.fetchone()
            print("Yeni Bakiyeniz: {}".format(balance[0]))
         elif result==0:
            print("Your Process wasn't realized successfully.")
            cursor.execute("Select Balance From Genel Where Kart=? ",(No,))
            balance=cursor.fetchone()
            print("Bakiyeniz: {}".format(balance[0]))

    def UsageKentkart(self,sayac):
      No=input("Number of Kentkart: ")
      cursor.execute("Select * From Ozel Where Kart=? ",(No,))
      result2=cursor.fetchall()
      if result2==0:
        print("Register Not Found")
      elif result2!=0:
        cursor.execute("Select Balance From Ozel Where Kart=? ",(No,))
        balance=cursor.fetchone()
        balance=list(balance)
        
        if (balance[0]<2.20) and sayac==0:
          print("Not Enough Balance")
          sayac -=1
          cursor.execute("Select Balance From Ozel Where Kart=? ",(No,))
          balance=cursor.fetchone()
          print("Bakiyeniz: {}".format(balance[0]))
        elif (balance[0]>=2.20) and sayac==0:
          balance[0] -=2.20          
          cursor.execute("Update Ozel Set Balance=? Where Kart=? ",(balance[0],No))
          con.commit()
          cursor.execute("Select Balance From Ozel Where Kart=? ",(No,))
          balance=cursor.fetchone()
          print("Bakiyeniz: {}".format(balance[0]))
        elif sayac!=0:
          cursor.execute("Select Balance From Ozel Where Kart=? ",(No,))
          balance=cursor.fetchone()
          print("{}. Transfer".format(sayac))
          print("Bakiyeniz: {}".format(balance[0]))
          

    def UsageKentkart2(self,sayac2):
      No=input("Number of Kentkart: ")
      cursor.execute("Select * From Genel Where Kart=? ",(No,))
      result2=cursor.fetchall()
      if result2==0:
        print("Register Not Found")
      elif result2!=0:
        cursor.execute("Select Balance From Genel Where Kart=? ",(No,))
        balance=cursor.fetchone()
        balance=list(balance)
        if (balance[0]<6.5) and sayac2==0:
          print("Not Enough Balance")
          sayac2 -=1
          cursor.execute("Select Balance From Genel Where Kart=? ",(No,))
          balance=cursor.fetchone()
          print("Bakiyeniz: {}".format(balance[0]))
        elif (balance[0]>=6.5) and sayac2==0:
          balance[0] -=6.5
          cursor.execute("Update Genel Set Balance=? Where Kart=? ",(balance[0],No))
          con.commit()
          cursor.execute("Select Balance From Genel Where Kart=? ",(No,))
          balance=cursor.fetchone()
          print("Bakiyeniz: {}".format(balance[0]))

        elif (balance[0]>=1.20) and sayac2==1:
          balance[0] -=1.20
          print("{}. Transfer".format(sayac2))
          cursor.execute("Update Genel Set Balance=? Where Kart=? ",(balance[0],No))
          con.commit()
          cursor.execute("Select Balance From Genel Where Kart=? ",(No,))
          balance=cursor.fetchone()
          print("Bakiyeniz: {}".format(balance[0]))
          
        elif (balance[0]>=0.9) and sayac2==2:
          balance[0] -=0.90
          print("{}. Transfer".format(sayac2))
          cursor.execute("Update Genel Set Balance=? Where Kart=? ",(balance[0],No))
          con.commit()
          cursor.execute("Select Balance From Genel Where Kart=? ",(No,))
          balance=cursor.fetchone()
          print("Bakiyeniz: {}".format(balance[0]))
        elif (sayac2>=3):
          cursor.execute("Select Balance From Genel Where Kart=? ",(No,))
          balance=cursor.fetchone()
          print("{}. Transfer".format(sayac2))
          print("Bakiyeniz: {}".format(balance[0]))
          

con=sqlite3.connect("kentkart.db")
cursor=con.cursor()
cursor.execute("Create Table IF Not Exists Ozel(Name TEXT,Surname TEXT,TC TEXT,Kart TEXT,Balance FLOAT)")
con.commit()
cursor.execute("Create Table IF Not Exists Genel(Kart TEXT,Balance FLOAT)")
con.commit()

while(1):
 cursor.execute("Select * From Ozel")
 result=cursor.fetchall()
 cursor.execute("Select * From Genel")
 result2=cursor.fetchall()
 Balance=0

 if result!=1 or result2 !=1:
  kentkart=Kentkart(Balance)
  print("---Processes---\n\n\r1-Kayıt Ekleme\n\r2-Kayıt Silme\n\r3-Kayıt Güncelleme\n\r4-Exit\n\r5-Loading Cash To Your Card\n\r6-Using Your Card")
  sec=int(input("Which Process Would You Like To do ? : "))
  if (sec==1):
    while(1):
     print("1-Private : Student,Teacher,Disable,Old,Health Staff,Police\n2-General")
     ter=int(input("Which Categories Will You add register(1/2): "))
     if (ter==1):
       kentkart.OzelKayıtEkleme(Balance)
       break
     elif (ter==2):
        kentkart.GenelKayıtEkleme(Balance)
        break
  elif (sec==2):
    while(1):
     print("1-Private : Student,Teacher,Disable,Old,Health Staff,Police\n2-General")
     ter=int(input("Which Categories Will You delete register(1/2): "))
     if (ter==1):
       kentkart.OzelKayıtSilme(Balance)
       break
     elif (ter==2):
        kentkart.GenelKayıtSilme(Balance)
        break 
  elif (sec==4):
    break
  elif (sec==3):
     while(1):
      print("1-Private : Student,Teacher,Disable,Old,Health Staff,Police\n2-General")
      ter=int(input("Which Kinds of Register Will You Update (1/2): "))
      if (ter==1):
       kentkart.OzelKayıtGuncelleme()
       break
      elif (ter==2):
        kentkart.GenelKayıtGuncelleme()
        break 
  elif (sec==5):
     while(1):
      print("1-Private : Student,Teacher,Disable,Old,Health Staff,Police\n2-General")
      ter=int(input("Which Kinds of Register Will You deposit Money (1/2): "))
      if (ter==1):
       kentkart.OzelBakiyeYukleme(Balance)
       break
      elif (ter==2):
        kentkart.GenelBakiyeYukleme(Balance)
        break 
  elif (sec==6):
    print("1-Private : Student,Teacher,Disable,Old,Health Staff,Police\n2-General")
    sayac=0
    sayac2=0
    start=time.perf_counter()
    while (1):
     print("\nYou can write 0 for exit")
     genre=int(input("Which kinds of Your Card(1/2) ? "))
     if (genre==1):
       kentkart.UsageKentkart(sayac)
       sayac +=1
       
     elif (genre==2):
      kentkart.UsageKentkart2(sayac2)
      sayac2 +=1

     elif (genre==0):
      break

     else:
      sys.stderr.write("You wrote Wrong Value...")
      sys.stderr.flush()

     stop=time.perf_counter()
     if (stop-start)>7_200_000_000_000:
       sayac=0
       sayac2=0
     
   
    
else:
    sys.__stderr__.write("\nSigned Card Not Found")
    sys.__stderr__.flush()

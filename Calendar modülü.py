import calendar,time,sys
from datetime import datetime
print("Programa Hoşgeldiniz...\n "+time.ctime(datetime.timestamp(datetime.now())))
while(1):
 year=int(input("Yılı Giriniz: "))
 month=input("Ayı Yazınız: ")
 month=month.capitalize()
 print(month)
 x={"Ocak":1 ,"Şubat":2,"Mart":3,"Nisan":4,"Mayıs":5,"Haziran" :6,"Temmuz":7,"Ağustos":8,"Eylül":9,"Ekim":10, "Kasım":11,"Aralık":12}
 for i,e in x.items():
    if i==month:
        print(calendar.month(year,e))
 while(1):
  sec=input("Devam Etmek İstiyor Musunuz(E/H) ? : ")
  if (sec=='E' or sec=='e'):
    time.sleep(2)
    break
  elif (sec=='H' or sec=='h'):
    print("Yine Bekleriz...")
    sys.exit()
  else:
    sys.__stderr__.write("\nYanlış Girdiniz...\a")
    sys.__stderr__.flush()





         
        
      
  
from datetime import datetime
import requests,time,sys,os
from bs4 import BeautifulSoup

response=requests.get("https://kur.doviz.com/isbankasi")
context=response.content
soup=BeautifulSoup(context,"html.parser")
sayac=0
while(1):
  
  Ad=soup.find_all("span",{"class":"name"})
  Kur=soup.find_all("span",{"class":"value"})
  Degisim=soup.find_all("div",{"class":"change-rate status down"})
  Amount=soup.find_all("div",{"class":"change-amount"})
    
  for i,e,k,l in zip(Ad,Kur,Degisim,Amount):
    print(str(datetime.ctime(datetime.now())),"\n","{}/TL: {}".format(i.text,e.text))
    print("Değişim Oranı: {}\nDeğişim Miktarı:{}".format(k.text,l.text))
    print("**************************************************************************************")

  while(1):
    sec=input("\nDevam Etmek İstiyor Musunuz(E/H) ? : ")
    if (sec=='e' or sec=='E'):
     print("Devam Ediliyor...\n")
     print("*******************")
     time.sleep(3)
     break
    elif (sec=='H' or sec=='h'):
     print("Yine Bekleriz...")
     sys.exit()
    else:
     sys.__stderr__.write("\nYanlış Girildi...")
     sys.__stderr__.flush()
     os.abort()





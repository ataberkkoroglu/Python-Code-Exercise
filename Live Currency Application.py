from tkinter import Label,Tk
from bs4 import BeautifulSoup
import pandas as pd,requests

def Currency():
 url="https://www.bloomberght.com/doviz"
 currency=list()
 response=requests.get(url)
 Content=response.content
 response2=requests.get("https://kur.doviz.com/serbest-piyasa/sterlin")
 Content2=response2.content
 soup2=BeautifulSoup(Content2,"html.parser")
 soup=BeautifulSoup(Content,"html.parser")
 currency.append(soup.find("span",{"class":"value dolar-bid"}).text) #DOLAR-TL ALIŞ: 
 currency.append(soup.find("span",{"class":"value dolar-ask"}).text) #DOLAR-TL Satış: 
 currency.append(soup.find("span",{"class":"value euro-bid"}).text) #EURo-TL Alış: 
 currency.append(soup.find("span",{"class":"value euro-ask"}).text) #EURO-TL Satış: 
 currency.append(soup.find("span",{"class":"value eur-usd-bid"}).text) #STERLIN-TL Alış: 
 currency.append(soup.find("span",{"class":"value eur-usd-ask"}).text) #DOLAR-EUR Satış: 
 currency.append(soup2.find("span",{"data-socket-key":"GBP","data-socket-attr":"bid"}).text.strip().replace("\n","")) #STERLIN-TL Alış: 
 currency.append(soup2.find("span",{"data-socket-key":"GBP","data-socket-attr":"ask"}).text.strip().replace("\n","")) #STERLIN-TL Satış: """
 
 
 for i in currency:
    i=str(i)
    i.strip()
    i.replace("\n","")
    
 x=["DOLAR-TL Alış: ","DOLAR-TL Satış: ","EURO-TL Alış: ","EURO-TL Satış: ","DOLAR-EURO Alış: ","DOLAR-EURO Satış","STERLIN-TL Alış: ","STERLIN-TL Satış: "]

 data=pd.DataFrame(currency,index=x,columns=[""])
 print(pd.DataFrame.to_string(data))
 label.config(text=pd.DataFrame.to_string(data))
 label.after(100,Currency)
 

app=Tk()
app.title("Currency")
app.geometry("640x480")
app.resizable(1,1)
app.config(background="Black")
label=Label(app,font=("arial",24,"bold"),foreground="White",background="Black")
label.grid(row=5,column=5)
app.maxsize(480,400)
Currency()
app.mainloop()
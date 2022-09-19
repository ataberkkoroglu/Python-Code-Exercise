import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
mesaj=MIMEMultipart()
with open ("Mail.txt","r+",encoding="utf-8") as file:
    
    x=file.readlines()
    for i in x:
      mesaj["From"]=x[0]
      mesaj["to"]=x[1]
      mesaj["Subject"]="STMP KULLANARAK MAİL GÖNDERME"
      yazı="""
        Günaydın Nü Nü,
         Nasılsın?
    
        """

    mesaj_govdesi=MIMEText(yazı,"plain")
    mesaj.attach(mesaj_govdesi)
try:
    mail= smtplib.SMTP("stmp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("ataberkkoroglu@gmail.com","2606Atam")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj["Subject"],mesaj.as_string())
    print("Mailiniz Başarıyla Gönderildi.")
    mail.close()
except:
    sys.stderr.write("Mailiniz Gönderilemedi")
    sys.stderr.flush()

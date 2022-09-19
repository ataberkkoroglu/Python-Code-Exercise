import sqlite3 

con=sqlite3.connect("kütüphane.db")
cursor= con.cursor()
def Tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Car(model TEXT,Yıl INT,Hp INT,Motor_Kapasitesi FLOAT)")
    con.commit()
def Veri_ekleme():
    cursor.execute("INSERT INTO Car VALUES('Caddy' ,2016,92,1.6)")
    con.commit()
Tablo_olustur()
Veri_ekleme()
con.close()
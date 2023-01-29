import pandas as pd,os,docx
from sqlalchemy import create_engine

con=create_engine('sqlite:///Ogrenci.db').connect()

data=pd.read_sql_table("Ogrenci",con)
os.chdir("C:/Users/asus/Desktop")
with pd.ExcelWriter("Ogrenci.xlsx",engine='openpyxl',mode='w') as writer:
    data.to_excel(writer,'Ogrenci')
    
with open("Ogrenci.txt",mode='w',encoding='utf-8') as fp:
    fp.write(pd.DataFrame.to_string(data))
    

world=docx.Document()
world.add_heading("Ogrenci Listesi",5)
world.add_paragraph(pd.DataFrame.to_string(data))
world.save("Ogrenci.docx")


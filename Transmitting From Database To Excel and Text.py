import pandas as pd
from sqlalchemy import create_engine
con=create_engine('sqlite:///Ogrenci.db').connect()

data=pd.read_sql_table("Ogrenci",con)
with pd.ExcelWriter("Ogrenci.xlsx",engine='openpyxl',mode='w') as writer:
    data.to_excel(writer,'Ogrenci')
    
with open("Ogrenci.txt",mode='w',encoding='utf-8') as fp:
    fp.write(pd.DataFrame.to_string(data))
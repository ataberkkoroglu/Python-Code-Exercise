import pandas as pd,os
os.chdir("C:/Users/asus/Desktop")

try:
 os.mkdir("Exercise")
except:
    pass
    
data=pd.read_excel("C:\\Users\\asus\\Desktop\\School\\computer\\5.Week\\1_MaasOdemesiExcel_Examples.xlsx")

os.chdir("C:/Users/asus/Desktop/Exercise")
with pd.ExcelWriter('Excel.xlsx',engine='openpyxl',mode='w') as writer:
    data.to_excel(writer,sheet_name="Salary")

fp=open("ExcelTxt.txt","w",encoding="utf-8")

fp.write(pd.DataFrame.to_string(data))

fp.close()

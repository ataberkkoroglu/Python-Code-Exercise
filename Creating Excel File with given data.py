import pandas as pd,os,time,sys,sqlite3
from datetime import datetime
from sqlalchemy import create_engine

os.chdir("C:/Users/asus/Desktop")
print("Welcome To Program...\n",datetime.strftime(datetime.now(),"%H:%M:%S %d / %m / %Y "))

con=sqlite3.connect("Staff.db")
cursor=con.cursor()
cursor.execute("Create Table If Not Exists staff(Person TEXT,Salary INT, Age INT,Department TEXT)")
con.commit()

while 1:
  
  while 1:
      
    counter=0
    Ch=int(input("1-Add Staff to List\n2-Delete Staff From List\n3-Create New List\nWhich one Do You Want To Do ? : "))
    
    if Ch==1:
     num=int(input("How Many Staff Do You Want To Add ? : "))
     
     while counter<num:
         
      person=input(f"{counter+1}. Write Your Staff's Name and Surname: ")
    
      salary=int(input(f"{counter+1}. Write Your Staff's Salary : "))
   
      age=int(input(f"{counter+1}. Write Your Person's Age: "))
    
      department=input(f"{counter+1}. Write Your Person's Department: ")
      cursor.execute("Select * From staff Where Person=?",(person,))
      result=cursor.fetchall()
      
      if result==[]:
       cursor.execute("Insert Into staff Values(?,?,?,?)",(person,salary,age,department))
       con.commit()
       
      else:
        cursor.execute("Update staff set Salary=?,Age=?,Department=? Where Person=?",(salary,age,department,person))   
        con.commit()
      counter +=1
     break
 
    elif Ch==2:
        person=input("Write Your Staff's Name and Surname: ")
        cursor.execute("Delete From staff Where Person=? ",(person,))
        con.commit()
        break
    
    elif Ch==3:
        cursor.execute("Delete From Staff")
        con.commit()
        num=int(input("How Many Staff Do You Want To Add For New List ? : "))
        
        while counter<num:
            
         person=input(f"{counter+1}. Write Your Staff's Name and Surname: ")
     
         salary=int(input(f"{counter+1}. Write Your Staff's Salary : "))
   
         age=int(input(f"{counter+1}. Write Your Person's Age: "))
    
         department=input(f"{counter+1}. Write Your Person's Department: ")
         cursor.execute("Select * From staff Where Person=?",(person,))
         result=cursor.fetchall()
         
         if result==[]:
          cursor.execute("Insert Into staff Values(?,?,?,?)",(person,salary,age,department))
          con.commit()
          
         else:
          cursor.execute("Update staff set Salary=?,Age=?,Department=? Where Person=?",(salary,age,department,person))   
          con.commit()
         counter +=1
        break
    
    else:
        print("Invalid Process")
        
  while 1:
      
        ch=input("Would You Like To Contunie(Y/N) ? : ")
        if ch=='Y' or ch=='y':
            time.sleep(3)
            break
        
        elif ch=='N' or ch=='n':
            data=pd.read_sql_table("staff",create_engine("sqlite:///Staff.db").connect())
            data2=pd.DataFrame(data)
            print(data2)
            data2.set_index("Person",inplace=True)
            data2.to_excel("Staff.xlsx","Employees' Informations")
            print("Have a Good Days...")
            sys.exit()
            
        else:
            print("Wrong Input...\a")
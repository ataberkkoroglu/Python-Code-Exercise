import pandas as pd,os,time,sys
from datetime import datetime
os.chdir("C:/Users/asus/Desktop")
print("Welcome To Program...\n",datetime.strftime(datetime.now(),"%H:%M:%S %d / %m / %Y "))
Person=list()
Salary=list()
Age=list()
Department=list()
while 1:
    person=input("Write Your Staff's Name and Surname: ")
    Person.append(person)
    salary=int(input("Write Your Staff's Salary : "))
    Salary.append(salary)
    age=int(input("Write Your Person's Age: "))
    Age.append(age)
    department=input("Write Your Person's Department: ")
    Department.append(department)
    while 1:
        ch=input("Would You Like To Contunie(Y/N) ? : ")
        if ch=='Y' or ch=='y':
            time.sleep(3)
            break
        elif ch=='N' or ch=='n':
          
            a=pd.DataFrame([[Salary,Age,Department]],index=Person,columns=["Salary","Age","Department"])
            a.to_excel("Staff.xlsx",sheet_name="Employees' Informations")
            print(a)
            sys.exit()
        else:
            print("Wrong Input...\a")
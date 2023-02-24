from datetime import datetime
import sys,time

def Program(num,base):
    remainder=list()
    digit=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    while 1:
        rem=int(num%base)
        num=num/base
        remainder.append(digit[rem])
        if num<=1 and num>=0:
            print(remainder)
            break
        
print("Welcome To Program...\n"+datetime.strftime(datetime.now()," %H : %M : %S  %d . %m . %Y"))
while 1:
 num=int(input("Write a Decimal Number: "))
 base=int(input("Which base Do You Want To Convert Your Number : "))
 Program(num,base)
 while 1:
     ch=input("Would You Like To Contunie (Y/N) ? : ")
     if ch=='Y' or ch=='y':
         time.sleep(2)
         break
     elif ch=='N' or ch=='n':
         print("Have a Good Days...\n"+datetime.strftime(datetime.now()," %H : %M : %S  %d . %m . %Y"))
         sys.exit()
     else:
         print("Wrong Character...\nPlease Write Again...")
         
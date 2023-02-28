from colorama import ansi
import time,sys
from datetime  import datetime
print(ansi.Style.BRIGHT)
print("Welcome To Program...",datetime.strftime(datetime.now(),"%H : %M : %S  %d.%m.%Y"),sep='\n')
while(1):
  text=input("Write a Text: ")
  while(1):
    print("""Colours:\n1-Black\n2-Blue\n3-Cyan\n4-Magenta\n5-Green\n6-LightMagenta\n7-Red\n8-LightCyan\n9-White""")
    colour=int(input("Write Your Choice(1/2/3/4/5/6/7/8/9): "))
    
    if colour==1:
     print(ansi.Fore.BLACK,text)
     print(ansi.Fore.RESET)
     break
    elif (colour==2):
        print(ansi.Fore.BLUE,text)
        print(ansi.Fore.RESET)
        break
    elif(colour==3):
        print(ansi.Fore.CYAN,text)
        print(ansi.Fore.RESET)
        break
    elif(colour==4):
        print(ansi.Fore.MAGENTA,text)
        
        print(ansi.Fore.RESET)
        break
    elif (colour==5):
        print(ansi.Fore.GREEN,text)
        print(ansi.Fore.RESET)
        break
    elif (colour==6):
        print(ansi.Fore.LIGHTMAGENTA_EX,text)
        print(ansi.Fore.RESET)
        break
    elif (colour==7):
        print(ansi.Fore.RED,text)
        print(ansi.Fore.RESET)
        break
    elif colour==8:
        print(ansi.Fore.LIGHTCYAN_EX,text)
        print(ansi.Fore.RESET)
        break
    elif colour==9:
        print(ansi.Fore.WHITE,text)
        print(ansi.Fore.RESET)
        break
    else:
        print("Invalid Process...\nPlease Write Again...")
        
  while(1):
        ch=input("Would  You Like To Contunie(Y/N) ? : ")
        if ch=='Y' or ch=='y':
            time.sleep(3)
            break
        elif ch=='N' or ch=='n':
            print("Have a Good Days...\n"+datetime.strftime(datetime.now(),"%H : %M : %S %d.%m.%Y"))
            sys.exit()
            
        else:
            print("Wrong Character...\nPlease Write Again...")
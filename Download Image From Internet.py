import requests,time,sys,shutil,urllib
from datetime import datetime

print("Welcome To Program...\n",datetime.strftime(datetime.now(),"%H : %M : %S  %d . %m . %Y"))
while(1):
    url=input("Paste Link of The Image Which You Want To Download : ")
    name=input("Write Name of Image Which Will Download To Computer  : ")
    response=requests.get(url,stream=True)
    
    if(response.status_code==200):
     with open(f"{name}.jpg","wb") as file:
        shutil.copyfileobj(response.raw,file)
    else:
        print("Image Couldn't Be Downloaded Successfully")
    
    
    while(1):
        ch=input("Would  You Like To Contunie(Y/N) ? : ")
        if ch=='Y' or ch=='y':
            time.sleep(3)
            break
        elif ch=='N' or ch=='n':
            print("Have a Good Days...")
            sys.exit()
        else:
            print("Wrong Character...\nPlease Write Again...")
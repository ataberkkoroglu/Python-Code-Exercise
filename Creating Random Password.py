import random,sys

s=['A','B','C','D','E','F','G','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','X','W','V','Y','Z']
c=list()
for i in range(0,len(s)):
    a=s[i].lower()
    c.append(a)
    
p=['!','\'','^','+','%','&','/','?','-','*']
while 1:
 while 1:
  x=int(input('How Many Character Do You Want To Create For Your Password ? : '))
  if x<8 or x>15:
     print("Your Password's Length must be the least eight character.\nPlease, Write Again...")
  else:
     break
 
 password=list()
 counter=0
 while counter<x:
  sc=random.randint(1,4)
  if sc==1:
     password.append(random.choice(s))
  elif sc==2:
     password.append(random.choice(c))
  elif sc==3:
     password.append(str(random.randint(0,9)))
  else:
     password.append(random.choice(p))
  counter +=1
 password=''.join(password)
 print(f"Your Password: {password}")
 while 1:
     sc=input('Would You Like To Contunie(Y/N) ? : ')
     if (sc=='Y' or sc=='y'):
         break
     elif sc=='N' or sc=='n':
         sys.stderr.write('\nHave a Good Days...')
         sys.stderr.flush()
         sys.exit()
     else:
         sys.stderr.write('\nWrong Character...\nPlease Write Again...\n')
         sys.stderr.flush()
     
 
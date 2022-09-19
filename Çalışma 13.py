from datetime import datetime

now=datetime.now()

print("programa Hoşgeldiniz..."),
print(datetime.ctime(now))
i=3
while(i<5):
   print(i*"*"+((11-(2*i))*" "+(i-i)*" "+i*"*"))
   i+=1
k=3
while (k>2):
   print(k*"*"+(11-(2*k))*" "+k*"*")
   k -=1
e=11
while(e>5):
   print(11*"*")
   e -=1
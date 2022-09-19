x=list()
def Asal_sayı():
 for i in range(2,1001):
    x.append(i)
    if (i==4):
        x.remove(i)
    if(i==997):
      break
    for e in range(3,1000):
     if (i>e):
      if i%e==0:  
         x.remove(i)
         break
      elif i%e!=0:
        pass
      else:
        break
 for i in x:
     yield i
 
generator=Asal_sayı()
iteration=iter(generator)
print(next(iteration))
"""print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))"""
"""while True:
       try: 
        print(next(iteration))
       except StopIteration:
        break
 """  
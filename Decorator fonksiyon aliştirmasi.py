def func(function):
  def wrapper(a):
     
     print("1000'e kadar mükemmel Sayılar Bunlardır:{}".format(a))
  return wrapper
x=list()
for i in range(2,1001):
  x.append(i)
  for e in range(3,1000):
    if (i>e):
      if i%e==0:
          
        #print("{} Sayısı Asal Sayı Değildir.".format(i))
        x.remove(i)
        break
      elif i%e!=0:
        pass
      else:
        break   
a=list()  

toplam=0
for u in range(1,1000):
  toplam +=u
  if toplam in x:
    a.append(toplam)    
@func
def function(a):
  
  pass    
 
 
func(function(a))
    

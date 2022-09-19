import sys
def Sayi():
    for i in range(0,5,1):
       yield i
Generator=Sayi()
Iterator=iter(Generator)
while(1):
  try:
   print(next(Iterator))
  except:
    sys.__stderr__.write("Aralığın dışına çıkıldı...")
    sys.__stderr__.flush()
    break
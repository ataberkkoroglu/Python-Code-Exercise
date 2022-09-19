class Kareler():
    
    def __init__(self,maksimum):
        self.maksimum = maksimum
        
        self.sayı = 1
        
    def __iter__(self):
        return self
    def __next__(self):
        
        if (self.sayı <= self.maksimum):
            
            sonuc =  self.sayı ** 2
            self.sayı += 1
            return sonuc
        else:
            self.sayı = 1
            raise StopIteration
    
       
y=int(input("Karelerini Bulmak İstediğiniz Sayıya Kadar Giriniz= "))
kareler=Kareler(y)
iterator=iter(kareler)

while True:
   print(next(iterator))
    

 
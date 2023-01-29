from barcode import EAN13,writer
import random

def CreatingBarcode(sayi=0):
 a=list()
 for i in range(0,13):
  a.append(str(random.randint(0,9)))
 number="".join(a)

 Barcode=EAN13(number,writer=writer.ImageWriter("PNG","RGB"))
 if sayi==0:
  Barcode.save("barcode")
 else:
     Barcode.save(f"barcode({sayi})")
 
n=int(input("How Many Barcode Do You Want To Create ? : "))
counter=0

while counter<n:
    CreatingBarcode(counter)
    counter +=1

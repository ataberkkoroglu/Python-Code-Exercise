class Dosya():
 def __init__(Self):
    with open("siir.txt","r",encoding="utf-8")as Siir:
        dosya_icerigi=Siir.read()
        kelimeler=dosya_icerigi.split(" ")
        Self.sadece_kelimeler=list()
        for i in kelimeler:
            i=i.strip("\n")
            i=i.strip(" ")
            i=i.strip(",")

            Self.sadece_kelimeler.append(i)
        
        while True:
            for i in Self.sadece_kelimeler:
                print(i)
                
            break

            
     
file=Dosya()
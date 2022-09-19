isim=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
isim.sort()
numara=[1,2,3,4,5,6,7]
soyisim=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
for d,i,e in zip(numara,isim,soyisim):
    print(d,i,e)
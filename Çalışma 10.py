import sys
sys.stdout.write("Programa Hoşgeldiniz...\n")
benzin=23.28
vergi_oranı=25
vergi=(benzin*1)/4
x=float(input("Kaç Litre Yakıt Almak İstiyorsunuz: "))
print("Ödeyeceğiniz Tutar : {}\nÖdeyeceğiniz Vergi: {}\nVergisiz Tutarı: {}".format(x*benzin,x*vergi,(x*benzin)-(x*vergi)))

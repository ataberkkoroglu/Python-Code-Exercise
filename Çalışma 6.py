import sys
sys.stdout.write("Programa Hoşgeldiniz...\n")
x= int(input("1. Sayıyı Giriniz: "))
y=int(input("2. Sayıyı Giriniz: "))
toplam=x+y
if(toplam>=40 and toplam<=50):
    sys.stdout.write("Genç Yazılımcı")
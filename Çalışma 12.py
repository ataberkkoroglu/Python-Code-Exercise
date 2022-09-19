from datetime import datetime
import sys,os,time
now=datetime.now()
print("Programa Hoşgeldiniz...",datetime.ctime(now),sep="\n")
print("""
   1 - Celsius
   2 - Fahrenheit
   3 - Kelvin""")
while(1):
 sec1=int(input("Giriş Yapacağınız Sıcaklık Değerinin Birimini Seçiniz: "))
 if (sec1==1):
    x=float(input("Girmek İstediğiniz Sıcaklığı Yazınız: "))
    print("""Dönüştürmek istediğiniz birimi seçiniz:
   1 - Celsius
   2 - Fahrenheit
   3 - Kelvin""")
    sec2=int(input("Dönüştürmek İstediğiniz Birimi Seçiniz: "))
    if (sec2==1):
        print("Celsius Cinsinden Sıcaklık: {}".format(x))
    elif (sec2==2):
        print("Fahrenheit Cinsinden Sıcaklık: {}".format(float(x*1.8+32)))
    elif (sec2==3):
        print("Kelvin Cinsinden Sıcaklık: {}".format(x+273.15))
    else:
        sys.stderr.write("HATA - Giriş yaptığınız birim değerine dönüştürme yapılamaz.\n")
        sys.stderr.flush()

 elif (sec1==2):
    x=float(input("Girmek İstediğiniz Sıcaklığı Yazınız: "))
    print("""Dönüştürmek istediğiniz birimi seçiniz:
   1 - Celsius
   2 - Fahrenheit
   3 - Kelvin""")
    sec2=int(input("Dönüştürmek İstediğiniz Birimi Seçiniz: "))
    if (sec2==1):
        print("Celsius Cinsinden Sıcaklık: {}".format((x-32)/1.8))
    elif (sec2==2):
        print("Fahrenheit Cinsinden Sıcaklık: {}".format(x))
    elif (sec2==3):
        print("Kelvin Cinsinden Sıcaklık: {}".format(((x-32)/1.8 + 273.15)))
    else:
        sys.stderr.write("HATA - Giriş yaptığınız birim değerine dönüştürme yapılamaz.\n")
        sys.stderr.flush()
 elif (sec1==3):
    x=float(input("Girmek İstediğiniz Sıcaklığı Yazınız: "))
    print("""Dönüştürmek istediğiniz birimi seçiniz:
   1 - Celsius
   2 - Fahrenheit
   3 - Kelvin""")
    sec2=int(input("Dönüştürmek İstediğiniz Birimi Seçiniz: "))
    if (sec2==1):
        print("Celsius Cinsinden Sıcaklık: {}".format((x-273.15)))
    elif (sec2==2):
        print("Fahrenheit Cinsinden Sıcaklık: {}".format(((x-273.15)*1.8+32 )))
    elif (sec2==3):
        print("Kelvin Cinsinden Sıcaklık: {}".format(x))
    else:
        sys.stderr.write("HATA - Giriş yaptığınız birim değerine dönüştürme yapılamaz.\n")
        sys.stderr.flush()
 else:
    sys.stderr.write("Yanlış Yazıldı")
    sys.stderr.flush()
    os.abort()
 sec3=input("Devam Etmek İstiyor Musunuz(E/H) ? : ")
 if(sec3=="E" or sec3=="e"):
    print("Devam Ediliyor...")
    time.sleep(3)
 elif (sec3=="H" or sec3=="h"):
    print("Uygulamadan Çıkış Yapıyorsunuz...")
    time.sleep(5)
    print("Yine Bekleriz...")
    break
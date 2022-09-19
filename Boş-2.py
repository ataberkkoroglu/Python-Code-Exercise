x=125
toplam=0
while True:
    c=int(x%10)
    toplam +=c
    x /=10
    if x>=0 and x<1:
        print(toplam)
        break

def Func(x,a):
    wovel=0
    consonant=0
    for i in x:
        if i in a:
            wovel +=1
        elif i==' ':
          pass
        else:
            consonant +=1
    return wovel,consonant
a=['a','A','E','e','i','İ','I',"ı","ö","Ö","U","u","Ü","ü","O",'o']
while(1):
  x=input("Write Your Text: ")
  b=Func(x,a)
  print("Vowels: {}\nConsonant:{}".format(b[0],b[1]))
  while(1):
   sec=input("Would You Like To Contunie: ")
   if(sec=='e' or sec=='E'):
    print("Be Contunied...")
    break
   elif (sec=='H' or sec=='h'):
    print("Have a Good Days...")
    exit(3)
   else:
    print("Wrong Answer...")
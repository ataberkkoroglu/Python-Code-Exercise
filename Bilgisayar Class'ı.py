from turtle import delay


class Computer():
    def __init__(Self,model,ram,graphic_card,harddisk):
        Self.model = model
        Self.ram = ram
        Self.graphic_card = graphic_card
        Self.harddisk= harddisk
    
    def __str__(Self):
        print(" Be Showing Computer's model...")

        print("Model of Computer:{}\nRam of Computer: {}\nGraphic_card of Computer:{}\nHarddisk of Computer:{}".format(Self.model,Self.ram,Self.graphic_card,Self.harddisk))
    
    
    
    def Raise_Voice (Self):
        v=0
        while True:         
         v +=1
         Reduce_Sound=v
         if v>=100:
            print("Reached The Lowest Voice Of Computer",100)
            Reduce_Sound=v
            break
         elif v<100:
            print("Voice of Computer:",v)
         k=input("Please Write 'q' here for Finish Process or Write 'a' Here For Keeping Process= ")
         if k=="q":
            Reduce_Sound=v
            break
         elif k=="a":
            print("Being Kept Process")
         else:
            k=input("Please Write 'q' here for Finish Process or Write 'a' Here For Keeping Process= ")
            if k=="q":
                break
            elif k=="a":
                print("Being Kept Process")

         
             
    def  Reduce_Voice(Self):
        v=100
        while True:     
         v -=1
         Raise_Sound=v
         if v<=0:
            print("Reached The Lowest Voice Of Computer",0)
            Raise_Sound=v
            break
         elif v>0:
            print("Voice of Computer:",v)
         s=input("Please Write 'q' here for Finish Process or Write 'a' Here For Keeping Process= ")
         if s=="q":
            Raise_Sound=v
            break
         elif s=="a":
            print("Being Kept Process")
         else:
            s=input("Please Write 'q' here for Finish Process or Write 'a' Here For Keeping Process= ")
            if s=="q":
                break
            elif s=="a":
                print("Being Kept Process")
        
    
    def Shine_of_Screen(Self):
        g=input("Write As increasing Voice 'w' ,As decreasing Voice 'r'= ")
        
        a=0
        Shine=100
        if g=="w":
            while True:
             a +=1
             t=input("Write 'q' For Complete process= ")
             if t=="q":
                print("Shine{}".format(a))
                break
             else:
              if a>=100:
                a==100
                print("Reached The highest Shine= ",100)
                break
              elif a<100:
                print("Shine:",a)
          
        elif g=="r":
           while True:  
            Shine -=1
            t=input("Write 'q' For Complete process= ")
            if t=="q":
                print("Shine{}".format(Shine))
                if Shine<=0:
                 print("Shine: ",0)
                 break
                elif Shine>0:
                    print("Shine: ",Shine)
                    break
            else:
                if Shine<=0:
                 Shine==0
                 print("Reached The Lowest Shine= ",0)
                 break
                elif Shine>0:
                  print("Shine{}".format(Shine))

    def Turn_off_Microphone(Self):
        while True:
         s=input("Write 'y' for Turning Off Microphone= ")
         if s=="y":
            print("Your Microphone is Being Turned Off...")
            delay(10)
            u=int(input("Do You Want To Turn Microphone off? Yes=1 or No=2 ="))
            if u==1:
               print(" TMicrophone is being Turned On...")
               delay(2) 
            elif u==2:
                print("Microphone has already been Closed.")
            break
         else:
            print("You Wrote Wrong...")
            break

    def Loading_Again(Self):
        while True:
         s=input("Write 'y' for Loading Again= ")
         if s=="y":
            print(" being Loaded again...")
            delay(2)
            print("Loaded...")
            break
         else:
            print("You Wrote Wrong...")
            break
    
    def Turn_Off_Touch_Screen(Self):
        while True:
         s=input("Write 'y' for Turning Off Touch Screen= ")
         if s=="y":
            print(" Touch Screen is being Switched Off...")
            delay(2)
            u=int(input("Do You Want To Turn Touch Screen off? Yes=1 or No=2 ="))
            if u==1:
               print(" Touch Screen is being Turned On...")
               delay(2) 
            elif u==2:
                print("Touch Screen has already been Closed.")
            else:
             print("You Wrote Wrong...")
             break

    def Run_Flight_Mode(Self):
        while True:
         s=input("Write 'y' for Running FLight Mode= ")
         if s=="y":
            print(" Flight Mode is being Switched On..")
            delay(2)
            u=int(input("Do You Want To Turn Flight Mode off? Yes=1 or No=2 ="))
            if u==1:
               print(" Flight Mode is being Turned Off..")
               delay(2) 
            elif u==2:
                print("Flight Mode has already been opened")
            break
            
         else:
            print("You Wrote Wrong...")
            break
    def Turn_Off_Camera(Self):
        while True:
         s=input("Write 'y' for Turning Off Camera= ")
         if s=="y":
            print(" Camera is being Turned Off..")
            delay(2)
            u=int(input("Do You Want To Turn Camera on? Yes=1 or No=2 = "))
            if u==1:
               print(" Camera is being Turned On..")
               delay(2) 
            elif u==2:
                print("Camera has already been closed")
            break
         else:
            print("You Wrote Wrong...")
            break
   
    def Lock_Screen(Self):
        while True:
         s=input("Write 'y' for Locking Screen= ")
         if s=="y":
            print("Screen is being Locked..")
            delay(2)
            u=int(input("Do You Want To Open Screen?  Yes=1 or No=2 = "))
            if u==1:
               print(" Screen is being Unfastened...")
               delay(2) 
               print("Your Screen was Opened...")
               break
            elif u==2:
                print("Screen has already been locked")
                break
         else:
            print("You Wrote Wrong...")
            break

    def Write_Screen(Self):
        while True:
            s=input("Write y for Writing things= ")
            if s=='y':
                x=input("You can write here = ")
                e=input("If you finish your writing,write 'q' = ")
                if e=="q":
                    print("Process is being Ceased...")
                    delay(2)
                    print("Your process was finished...")
                    break
                else:
                    print("You Wrote Wrong...")
                    break

    def Page_Up(Self):
       while True:
            s=input("Write y for Page Up= ")
            if s=='y':
                print("Page Up is running...")
                e=input("If you finish Page Up,write 'q' = ")
                if e=="q":
                    print("Page Up is being Ceased...")
                    delay(2)
                    print("Your Process was finished...")
                    break
                else:
                    print("You Wrote Wrong...")
                    break
    
    def Page_Down(Self):
       while True:
            print("Page Down is running...")
            s=input("Write y for Page Down= ")
            if s=='y':
                e=input("If you finish Page Down,write 'q' = ")
                if e=="q":
                    print("Page Down is being Ceased...")
                    delay(2)
                    print("Your Process was finished...")
                    break
                else:
                    print("You Wrote Wrong...")
                    break
    def Home(Self):
        while True:
            s=input("Write y for Return Previous Things= ")
            if s=='y':
                print("Home Process is running...")
                e=input("If you finish returning Previous Things,write 'q' = ")
                if e=="q":
                    print("Home is being Ceased...")
                    delay(2)
                    print("Your Process was finished...")
                    break
                else:
                    print("You Wrote Wrong...")
                    break
    def End(Self):
        while True:
            s=input("Write y for Passing  Next Things= ")
            if s=='y':
                print("End Process is running...")
                e=input("If you finish passing next things ,write 'q' = ")
                if e=="q":
                    print("End is being Ceased...")
                    delay(2)
                    print("Your Process was finished...")
                    break
                else:
                    print("You Wrote Wrong...")
                    break
    def Exit(Self):
        print("You are making exit this program...")
        delay(50)
        print("Program Was Turned Off...")
    
    
    a=[]
         
    def Add_Application(Self):
        global a 
        while True: 
          a=["Control Panel","CMD","Microsoft Office 365","Discord","Visual Studio Code","Ardunio","Anaconda"] 
          s=input("Write application here you want to install= ")
          print("Application is being  added...")
          delay(50)
          a.append(s)
          print("Application was installed.",a)
          f=int(input("Do you want to install another application Yes=1 , No=2= "))
          if f==1:
             print("Process is being Kept Running")
          elif f==2:
             print("Process is being ceased...")
             delay(2)
             print("Your Process is Finished...")
             break
          else:
             print("You Wrote Wrong...")
             break
         
    
    def remove_application(Self): 
         global a
         print("Application List: ",a)
         while True:
          s=input ("Write Application's index ,which start from zero, here you want to remove= ")
          print("Application is being removed")
          delay(50)
          a.remove(s)
          print("Application was removed.",a)
          f=int(input("Do you want to remove another application Yes=1 , No=2= "))
          if f==1:
            print("Process is being Kept Running")
          elif f==2:
             print("Process is being ceased...")
             delay(2)
             print("Your Process is Finished...")
             break
          else:
             print("You Wrote Wrong...")
             break
    
    def len(Self):
        global a
        print("Application List: ",a)
        delay(2)
        print(len(a))
    

    def Using_of_Computer (Self):
        print("""
        Closed Computer= 18  

        Opened Computer=20
        
        Shut voice=0

        Switch On Computer = 1

        Switch Off Computer = 2

        Raise Voice = 3

        Reduce Voice = 4

        Change Shine of Screen = 5

        Turn off Microphone=6

        Loading again=7

        Turn Off Touch screen= 8

        Run Flight Mode=9

        Turn off Camera=10

        Lock Screen=11

        Write Screen=12

        Page Up=13

        Page Down=14

        Home=15

        End=16

        Exit=17

        Show Informations of Computer=19

        (Firstly You have to start with Adding Application for Application Functions.)

        Adding Application =21

       Removing Application =23

        Showing Application=22

        """)

while True :
    computer= Computer("Lenovo Idea C340",8,"Nvidia GTE Force 630",1000)
    
    print(computer.Using_of_Computer())
    x=int(input("Is Your Computer Open? = "))
    if x==18:
        print("Please Turn On This Device For You Can Use As You Want")
        y=int(input("Enter your process for turning on Computer"))
        if y==1:
            print("Be Opening Computer")
            delay(30)
            break
    
        elif y!=1:
            print("Your Process is Wrong About Turning On Computer.")
    elif x==20:
        print("Be continued")
        break
while True:
    z=int(input("Enter process which you want to make= "))
    if z==2:
        print("Be Switched Off Computer...")
        delay(30)
        while True:
         c=int(input("Do you want to open this device ? For yes = 30 ,For No=31 = "))
         if c==30:
            print("Be Turning On The Computer...")
            break
         elif c==31:
            print("Not Be Turning On The Computer")
            break
         else:
            print("Your Answers Wrote Wrong...")

    elif z==3:
      computer.Raise_Voice()
    elif z==4:
        computer.Reduce_Voice()
    elif z==5:
        computer.Shine_of_Screen()
    elif z==6:
        computer.Turn_off_Microphone()
    elif z==7:
        computer.Turn_off_Microphone()
    elif z==8:
        computer.Turn_Off_Touch_Screen()
    elif z==9:
        computer.Run_Flight_Mode()
    elif z==10:
        computer.Turn_Off_Camera()
    elif z==11:
        computer.Lock_Screen()
    elif z==12:
        computer.Write_Screen()
    elif z==13:
        computer.Page_Up()
    elif z==14:
        computer.Page_Down()
    elif z==15:
        computer.Home()
    elif z==16:
        computer.End()
    elif z==17:
        computer.Exit()
        break
    elif z==19:
        computer.__str__()
    elif z==21:
        computer.Add_Application()
    elif z==22:
         computer.len()
    elif z==23:
        computer.remove_application()
  
   
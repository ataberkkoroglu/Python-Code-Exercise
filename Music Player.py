from tkinter import filedialog,Tk,Label,Button,PhotoImage,Listbox
from pygame import mixer
import os

mixer.init()

def Start():
    
    for i in PlayList.curselection():
     Music_Name = PlayList.get(i)
     print(Music_Name[0:-4])
     mixer.music.load(PlayList.get(i))
     mixer.music.play()
   
    
def Stop():
    print("Pause")
    mixer.music.pause()

def Load():
    
    path=filedialog.askdirectory()
    os.chdir(path)
    counter=0
    
    for song in os.listdir(path):
        if song.endswith(".mp3"):
            PlayList.insert(counter,song)
            counter +=1
app=Tk()
app.title("Music Player")
app.geometry("640x480")
app.resizable(True,True)
app.iconphoto(True,PhotoImage("Music Player",file="C:\\Users\\asus\\Desktop\\Sample Picture\\Music.png"))
app.config(background="Black")

Text=Label(app,font=('Arial',18,'bold'),foreground="White",text="Welcome To Music Player Application",background="Black")
Text.place(x=20,y=20)



start=Button(app,font=('Arial',18,'bold'),text='Start',foreground="White",background="Green",command= lambda : Start())
start.place(x=130,y=400)

stop=Button(app,text="Stop",font=('Arial',18,'bold'),foreground="White",background="red",command= lambda :Stop())
stop.place(x=260,y=400)

PlayList=Listbox(app,font=('Times',12,'bold'),foreground="White",background="Black")
PlayList.place(x=150,y=120)
folder=Button(app,text="Open the Folder",font=('Arial',18,'bold'),foreground="White",background="Orange",command= lambda : Load())
folder.place(x=60,y=60)
app.minsize(width=480,height=450)
app.maxsize(width=480,height=480)
app.mainloop()
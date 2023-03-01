import pywhatkit as py,time
from tkinter import Tk,Entry,Button,Label,PhotoImage

app=Tk()
app.geometry('640x480')
app.resizable(True,True)
app.config(background="black")
app.title("Youtube Video Player")
app.iconphoto(True,PhotoImage(name="VideoPlayer",file="C:/Users/asus/Desktop/Sample Picture/youtube.png"))

def Program(text):
   try:
      py.playonyt(text)
      while 1:
       print("PLAYING...")
       time.sleep(3)
   except:
      print("Network Error Occurred")

label=Label(app,font=("Arial",24,'bold'),foreground="White",text="Write Name of Video",background="black")
label.grid(row=3,column=10)
text=Entry(app,background="White",font=('Arial',24,'bold'))
text.grid(row=5,column=10)

button=Button(app,font=('Arial',24,'bold'),foreground='Black',background='Blue',text="Enter",command= lambda : Program(text.get()),width=10)
button.grid(row=9,column=10)
app.wm_maxsize(450,200)

app.mainloop()

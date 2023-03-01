from tkinter import Label,Tk,PhotoImage
import time,os
app=Tk()
app.title("Digital Clock")
os.chdir("C:/Users/asus/Desktop/")
#app.geometry("1220x830")
app.resizable(1,1)

app.iconphoto(True,PhotoImage(file="C:/Users/asus/Desktop/Sample Picture/Clock.png"))

#app.iconphoto(True,PhotoImage(file='Clock.jpg'))
label=Label(app,font=("Boulder",68,'bold'),foreground='White',background="Black",borderwidth=30,border=50)
label.grid(row=1,column=1)
app.maxsize(450,200)
def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)
    
digital_clock()
app.mainloop()

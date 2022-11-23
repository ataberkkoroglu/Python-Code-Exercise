from tkinter import Label,Tk,PhotoImage
import time
app=Tk()
app.title("Digital Clock")

#app.geometry("1220x830")
app.resizable(1,1)

#app.iconphoto(True,PhotoImage(file='Clock.jpg'))
label=Label(app,font=("Boulder",68,'bold'),foreground='#ffffff',background="#000000",borderwidth=30,border=50)
label.grid(row=1,column=1)
app.maxsize(450,200)
def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(300,digital_clock)
    
digital_clock()
app.mainloop()

from tkinter import Tk,Label,Button
import time
app=Tk()
app.title('StopWatch')

Ms=0
Second=0
Minute=0

def StopWatch():
    global kr,Second,Minute,Ms
    Ms +=1
    if Ms==100:
        Ms=0
        Second +=1
    if Second==60:
        Second=0
        Minute +=1
    kr=f"{Minute}:{Second}.{Ms}"
    a.config(text=str(kr))
    app.after(60,StopWatch)
   
def StopWatch2():
    global Ms,Minute,Second
    Ms=0
    Minute=0
    Second=0
    a.config(text=f"{Minute}:{Second}.{Ms}")
    app.after(1,StopWatch2) 
  

def StopWatch3():
    global Minute,Second,Ms
    a.config(text=f"{Minute}:{Second}.{Ms}")
    time.sleep(100000)
    
    Minute=0
    Second=0
    Ms=0
    a.config(text=f"{Minute}:{Second}.{Ms}")
    app.after(1,StopWatch3)
    
  
app.resizable(1,1)
a=Label(app,font=('Boulder',68,'bold'),foreground="white",background='Black',border=50,borderwidth=30,text="0:0.0")
start=Button(app,font=('Arial',20,"bold"),foreground="black",background="lightblue",text="Start",command=lambda: StopWatch())
reset=Button(app,font=('Arial',20,"bold"),foreground="black",background="Green",text="Reset",command=lambda: StopWatch2())
finish=Button(app,font=('Arial',20,'bold'),foreground="black",background="red",text="finish",command=lambda: StopWatch3())

a.grid(row=1,column=1)
start.grid(row=2,column=2)
reset.grid(row=3,column=2)
finish.grid(row=4,column=2)
app.maxsize(410,335)

app.mainloop()

from tkinter import Entry,Button,Label,Tk,PhotoImage
import pywhatkit,pyautogui as py
from datetime import datetime

def Send():
 pywhatkit.sendwhatmsg(number.get(),message.get(),time_hour=int(datetime.strftime(datetime.now(),"%H")),time_min=int(datetime.strftime(datetime.now(),"%M"))+1,wait_time=10) 
 py.click()
 
app=Tk()
app.config(background="Black")
app.resizable(1,1)
app.geometry("640x480")
app.title("Message")

app.iconphoto(True,PhotoImage(file="C:/Users/asus/Desktop/Sample Picture/message.jpeg"))
text2=Label(app,text="Write Number With Country Code",font=("Arial",24,'bold'),foreground="white",background="black")
text2.grid(row=3,column=10)
text=Label(app,text="Write Text",font=("Arial",24,"bold"),foreground="white",background="black")
text.grid(row=7,column=10)
#messagebox.showinfo("Information","Information for user")
number=Entry(app,font=("Arial",24,'bold'),background="White")
number.grid(row=5,column=10)
message =Entry(app,font=('Arial',24,'bold'),background="White")
message.grid(row=9,column=10)
print(message.get())
button=Button(app,text="Send Your Message",font=('Arial',11,'normal'),command=Send)
button.grid(row=11,column=10)
app.wm_maxsize(630,250)
app.mainloop()

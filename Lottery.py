from tkinter import Label,Tk,Button,PhotoImage
import random,time,os
from PIL import Image,ImageTk
os.chdir('C:/Users/asus/Desktop')
app=Tk()
app.geometry('640x480')
app.resizable(1,1)
app.title('Lottery Machine')

"""image=ImageTk.PhotoImage(Image.open('Clock.jpg'))
app.iconwindow(image)"""
counter=0
app.config(background='Black')
a=list()
def Lottery():
   a.append(random.randint(0,9))
   return a

def Reset():

    global a
    a.clear()
    label.config(text='0')
    label2.config(text='0')
    label3.config(text='0')
    label4.config(text='0')
    label5.config(text='0')
    label6.config(text='0')
    label7.config(text='0')
    label8.config(text='0')

    
def Lottery2():
    Reset()
    Lottery()
    label.config(text=str(Lottery()[0])+' - ')
    label2.config(text=str(Lottery()[1])+' - ')
    label3.config(text=str(Lottery()[2])+' - ')
    label4.config(text=str(Lottery()[3])+' - ')
    label5.config(text=str(Lottery()[4])+' - ')
    label6.config(text=str(Lottery()[5])+' - ')
    label7.config(text=str(Lottery()[6])+' - ')
    label8.config(text=str(Lottery()[7]))
    app.after(25,Lottery2)
    
def Stop():
    label.config(text=str(a[0])+' - ')
    label2.config(text=str(a[1])+' - ')
    label3.config(text=str(a[2])+' - ')
    label4.config(text=str(a[3])+' - ')
    label5.config(text=str(a[4])+' - ')
    label6.config(text=str(a[5])+' - ')
    label7.config(text=str(a[6])+' - ')
    label8.config(text=str(a[7]))
    time.sleep(10)
    
    
label=Label(app,font=("Arial",48,'bold'),foreground='White',background='Black',text='0-')
label.grid(row=1,column=1)

label2=Label(app,font=("Arial",48,'bold'),foreground='White',background='Black',text='0- ')
label2.grid(row=1,column=2)

label3=Label(app,font=("Arial",48,'bold'),foreground='White',background='Black',text='0- ')
label3.grid(row=1,column=3)

label4=Label(app,font=("Arial",48,'bold'),foreground='White',background='Black',text='0- ')
label4.grid(row=1,column=4)

label5=Label(app,font=("Arial",48,'bold'),foreground='White',background='Black',text='0- ')
label5.grid(row=1,column=5)

label6=Label(app,font=("Arial",48,'bold'),foreground='White',background='Black',text='0- ')
label6.grid(row=1,column=6)

label7=Label(app,font=("Arial",48,'bold'),foreground='White',background='Black',text='0- ')
label7.grid(row=1,column=7)

label8=Label(app,font=("Arial",48,'bold'),foreground='White',background='Black',text='0')
label8.grid(row=1,column=8)

button=Button(app,font=('Arial',20,'bold'),foreground='Black',background='lightblue',command= lambda : Lottery2(),text='START')
button.grid(row=10,column=3)

button2=Button(app,font=('Arial',20,'bold'),foreground='Black',background='Red',command= lambda: Stop(),text='STOP')
button2.grid(row=10,column=6)
app.minsize(760,150)
app.wm_maxsize(760,150)

app.mainloop()
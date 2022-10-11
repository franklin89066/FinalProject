########import modules############
from tkinter import *
import tkinter as tk
from tkinter import ttk, Tk, StringVar
import datetime as dt
import time as tm
from time import strftime
import random
import pip 

#from PIL import Image, ImageTk
#########################
####time and date########
localtime1 = tm.strftime('%I:%M:%p')
date = dt.datetime.now()
########################
####Create window instance######
root=Tk()
root.title("Orch-to-Door")
root.geometry("700x700")
root.configure(background="lightblue")
###Header labels
Label1=tk.Label(root,text=f" Orch-to-Door \n {date:%A, %B %d, %Y} ", background="white", font="helvetica 20 bold")
Label1.place(x=350,y=50,anchor="center",height=70, width = 800)
time=tk.Label(root,text=localtime1, background="white", font="helvetica 12 bold")
time.place(x=350,y=90,anchor="center",height=13, width = 800)
#img1 = ImageTk.PhotoImage(Image.open(froont_image.jpg))
#img.label = Label(root,image = img1 )
#img.label.place (x=350, y = 100)
###############
##new window instance###
def open(): #button clicked function
    global var1, var2, var3, var4 #Allows for the variables to be used here
    #configures new window 
    top = Toplevel()
    top.title("-Order-")
    top.configure(background="lightblue")
    top.geometry("250x250")
    name=tk.Label(top,text="Name: ")
    name.grid(row=0,column=0) #grid used
    UserName=tk.Label(top, text= entry1.get())#Get username
    UserName.grid(row=0,column=1)
    instPrice=tk.Label(top, text="Instrument Rental: $")
    instPrice.grid(row=1,column=0)
    lbl =tk.Label(top, text=r.get()) #instrument
    lbl.grid(row=1,column=1)
    tot = int(round(r.get() + var1.get() + var2.get()+ var3.get()+ var4.get(),2)) #total
    lbl2 =tk.Label(top, text=tot)
    lbl2.grid(row=4,column=1)
    TotalCost=tk.Label(top, text="Total Cost: $")
    TotalCost.grid(row=4,column=0)

#Variables needed for checkboxes
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()  
def open2():#new window instance 
    global clicked, var1, var2, var3, var4
    top1 = Toplevel()
    top1.title("-Order-")
    top1.configure(background="lightblue")
    ####Checkboxes#####
   
    acc =tk.Label(top1, text="Accessories:",foreground='black', font="times 12", background= 'white')
    acc.grid(row=0,column=0)

    a = Checkbutton(top1, text ="Strings    $100.00", variable=var1, onvalue=100,offvalue=0)
    a.grid(row=0,column=1)
    b = Checkbutton(top1, text ="Rosin      $10.00", variable=var2, onvalue=10,offvalue=0)
    b.grid(row=1,column=1)
    c = Checkbutton(top1, text ="Chin Rest  $20.00", variable=var3, onvalue=20,offvalue=0)
    c.grid(row=2,column=1)
    d = Checkbutton(top1, text ="Bow Holder $5.00", variable=var4, onvalue=5,offvalue=0)
    d.grid(row=3,column=1)
    btn = Button(top1, text = "Continue", command = open)
    btn.grid(row=5,column=2)

    
############################
########buttons##########
btn = Button(root, text = "Continue", command = open2)
btn.place(relx=0.8, rely=0.6)
##############################
######LABELS##############
name=tk.Label(root, text='Name: ', foreground='black', font="times 20", background='white')
name.place(relx=.45, rely=.14)
inst=tk.Label(root, text = "Instrument: " , foreground='black', font="times 12", background= 'white')
inst.place(relx=.1,rely=0.3)
#################
####ENTRIES##########
entry1 = tk.Entry(root, background="white", font="times 20")
entry1.place(relx=0.3, rely=0.19)
#######Radio Buttons########
r = IntVar()
r.get()
def clicked(value):
    money = Label(root, text="$")
    money.place(relx=0.08,rely=.357)
    myLabel = Label(root, text=value)
    myLabel.place(relx=0.099, rely=0.357)
myrad1=Radiobutton(root, text ="Violin", variable=r, value =25, command=lambda: clicked(r.get()))
myrad1.place(relx=.3, rely =.25)
myrad2=Radiobutton(root, text ="Viola", variable=r, value =28, command=lambda: clicked(r.get()))
myrad2.place(relx=.3, rely =.30)
myrad3=Radiobutton(root, text ="Cello", variable=r, value =35, command=lambda: clicked(r.get()))
myrad3.place(relx=.3 ,rely=.35)
myrad4=Radiobutton(root, text ="Bass", variable=r, value =40, command=lambda: clicked(r.get()))
myrad4.place(relx=.3, rely=0.4)

ttk.Separator(#horizontal line
    master=root,
    orient=HORIZONTAL,
    style='TSeparator',
    class_= ttk.Separator,
    takefocus= 1,
    cursor='plus'    
).pack(fill=X, padx=10, expand=True)


#Rainbow button! HOW COOL IS THIS?! https://stackoverflow.com/questions/66155807/im-trying-to-make-a-rainbow-tkinter-button
rainbow_colors = ['red','orange','yellow','green','lightblue',
                  'blue','purple','red','orange','yellow','green','lightblue',
                  'blue','purple','red','orange','yellow','green','lightblue',
                  'blue','purple','red','orange','yellow','green','lightblue',
                  'blue','purple',]
color_iterator = iter(rainbow_colors)

def ButtonUpdate():
    try:
        color = next(color_iterator)
        btn.config(bg=color)
    except StopIteration:
        return
    root.after(500, ButtonUpdate)
    

ButtonUpdate()


mainloop()
########import modules############
from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime as dt
import time as tm
from time import strftime
#########################
#time
localtime1 = tm.strftime('%I:%M:%p')

top=Tk()
top.title=("Orch-to-Door")
top.geometry("700x400")
top.configure(background="lightblue")

def open_win():
    new = Toplevel(top)
    new.geometry("750x250")
    new.title ("- Order -")


Label1=tk.Label(master=top,text=f" Orch-to-Door \n {date:%A, %B %d, %Y} ", background="white", font="helvetica 20 bold")
Label1.place(x=350,y=50,anchor="center",height=70, width = 800)
time=tk.Label(master=top,text=localtime1, background="white", font="helvetica 12 bold")
time.place(x=350,y=90,anchor="center",height=13, width = 800)



date = dt.datetime.now()
top=tk.Tk()
top.mainloop()
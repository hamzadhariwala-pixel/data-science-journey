import tkinter as tk #imports
from tkinter import *
window= tk.Tk() #gui interaction
window.title("My Calculator")
window.geometry("500x500")
e= Entry(window, width=56, borderwidth=5)# adding inputs
e.place(x =0, y=0)

#buttons:
def click(num):
    result= e.get()
    e.delete(0, END)
    e.insert(0, str(result)+str(num))

b= Button(window, text="1", width=12, command=lambda:click(1))
b.place(x=10,y=60)

b= Button(window, text="2", width=12, command=lambda:click(2))
b.place(x=100,y=60)

b= Button(window, text="3", width=12, command=lambda:click(3))
b.place(x=190,y=60)

b= Button(window, text="4", width=12, command=lambda:click(4))
b.place(x=100,y=120)

b= Button(window, text="5", width=12, command=lambda:click(5))
b.place(x=190,y=120)

b= Button(window, text="6", width=12, command=lambda:click(6))
b.place(x=10,y=120)

b= Button(window, text="7", width=12, command=lambda:click(7))
b.place(x=10,y=180)

b= Button(window, text="8", width=12, command=lambda:click(8))
b.place(x=100,y=180)

b= Button(window, text="9", width=12, command=lambda:click(9))
b.place(x=190,y=180)

b= Button(window, text="0", width=12, command=lambda:click(0))
b.place(x=10,y=240)

#operators
def add():
    n1= e.get()
    global math
    math ="addition"
    global i
    i=int(n1)
    e.delete(0, END)

b= Button(window, text="+", width=12, command=add)
b.place(x=100,y=240)

def sub():
    n1= e.get()
    global math
    math ="subtraction"
    global i
    i=int(n1)
    e.delete(0, END)
b= Button(window, text="-", width=12, command = sub)
b.place(x=190,y=240)

def Clear():
    e.delete(0, END)

b= Button(window, text="Clear", width=12, command = Clear)
b.place(x=280,y=60)

def mult():
    n1= e.get()
    global math
    math ="multiplication"
    global i
    i=int(n1)
    e.delete(0, END)
b= Button(window, text="*", width=12, command=mult)
b.place(x=280,y=120)

def div():
    n1= e.get()
    global math
    math ="division"
    global i
    i=int(n1)
    e.delete(0, END)
b= Button(window, text="/", width=12, command=div)
b.place(x=280,y=180)

def equals():
    n2=e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))

b= Button(window, text="=", width=12, command= equals)
b.place(x=280,y=240)






window.mainloop()
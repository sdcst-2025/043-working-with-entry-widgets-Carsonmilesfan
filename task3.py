#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk

w = tk.Tk()
w.attributes("-topmost",True)

def run(k):
    data1 = e[0].get()
    data2 = e[1].get()
    num1 = float(data1)
    num2 = float(data2)
    data = num1 * num2
    sanders = round(data, 2)
    e[2].delete(0,tk.END)
    e[2].insert(0,sanders)

def sun(k):
    data3 = e[0].get()
    data4 = e[1].get()
    num3 = float(data3)
    num4 = float(data4)
    dataa = num3 + num4
    sanders = round(dataa, 2)
    e[2].delete(0,tk.END)
    e[2].insert(0,sanders)

def tun(k):
    data5 = e[0].get()
    data6 = e[1].get()
    num5 = float(data5)
    num6 = float(data6)
    dataaa = num5 - num6
    sanders = round(dataaa, 2)
    e[2].delete(0,tk.END)
    e[2].insert(0,sanders)

def lun(k):
    data7 = e[0].get()
    data8 = e[1].get()
    num7 = float(data7)
    num8 = float(data8)
    dataaaa = num7 / num8
    sanders = round(dataaaa, 2)
    e[2].delete(0,tk.END)
    e[2].insert(0,sanders)


miles = tk.StringVar

l = []
l.append( tk.Label(w,text="Number 1"))
l.append( tk.Label(w,text="Number 2"))
l.append( tk.Label(w,text="Number Calculator"))


e = []
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text="answer", textvariable = miles))
b=[]
b.append(tk.Button(w,text="x"))
b.append(tk.Button(w,text="+"))
b.append(tk.Button(w,text="-"))
b.append(tk.Button(w,text="÷"))
b[0].bind("<Button>", run)
b[1].bind("<Button>", sun)
b[2].bind("<Button>", tun)
b[3].bind("<Button>", lun)

l[2].grid(row=1,column=1,columnspan=4)
l[0].grid(row=2,column=1,columnspan=2)
l[1].grid(row=2,column=3,columnspan=2)
e[0].grid(row=3,column=1, columnspan=2)
e[1].grid(row=3,column=3, columnspan=2)
b[0].grid(row=4,column=1)
b[1].grid(row=4,column=2)
b[2].grid(row=4,column=3)
b[3].grid(row=4,column=4)
e[2].grid(row=5,column=1,columnspan=4)

w.mainloop()

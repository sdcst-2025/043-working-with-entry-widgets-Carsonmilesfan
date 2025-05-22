#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk
import math
def run(e):

    data1 = e1.get()
    data2 = e2.get()
    num1 = float(data1)
    num2 = float(data2)
    data = math.sqrt((num1**2) + (num2**2))
    miles = round(data, 3)
    eoutput.insert(0,miles)



win=tk.Tk()

sanders = tk.StringVar()

e1 = tk.Entry(win, width = 15)
e2 = tk.Entry(win, width = 15)
eoutput = tk.Entry(win, width = 15, textvariable=sanders)
l1 = tk.Label(win, width = 15, text = "side 1")
l2 = tk.Label(win, width = 15, text = "side 2")
l3 = tk.Label(win, width = 15, text = "hypotneuse")
b1 = tk.Button(win, width = 15, text = "paste information")
b1.bind("<Button>",run)


l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()
l3.pack()
eoutput.pack()


win.mainloop()
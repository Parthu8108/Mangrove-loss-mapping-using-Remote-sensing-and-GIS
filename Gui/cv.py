import Tkinter
import tkMessageBox
from Tkinter import *
top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
   
#C = Tkinter.Canvas(top, bg="White", height=1000, width=1000)


B = Tkinter.Button(top, text ="Browser image 1", command = helloCallBack)
B.grid(row=0, column=0)
B1 = Tkinter.Button(top, text ="Browser image 2", command = helloCallBack)
B1.grid(row=1, column=0)
B.pack(padx=100, pady=100)
B1.pack()
#C.pack()
top.mainloop()
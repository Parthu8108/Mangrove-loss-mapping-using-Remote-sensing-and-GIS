
from tkinter import *
top = tkinter.Tk()
var = StringVar()
label = Label( top, textvariable=var, relief=RAISED )
var.set("Layout")
C = tkinter.Canvas(top, bg="White", height=1000, width=1000)

label.pack()
C.pack()
# Code to add widgets will go here...
top.mainloop()
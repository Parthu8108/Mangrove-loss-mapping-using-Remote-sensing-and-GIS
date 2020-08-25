import Tkinter
import tkMessageBox,tkFileDialog
from PIL import Image,ImageTk
from Tkinter import *
import os

def askopenfilename():
        return tkFileDialog.askopenfile()
		
def demo():
		x=askopenfilename()
		img = x.read()
		canvas = Canvas(top,bg="blue", width = 300, height = 300)      
		canvas.create_image((10, 20), img)
		canvas.pack()
		
		
top = Tkinter.Tk() 
#C = Tkinter.Canvas(top, bg="White", height=1000, width=1000)
B = Tkinter.Button(top, text ="Browser image 1", command = demo)
#B.place(bordermode=OUTSIDE, height=100, width=100)
B1 = Tkinter.Button(top, text ="Browser image 2", command = askopenfilename)
B2 = Tkinter.Button(top, text ="Browser image 3", command = askopenfilename)
B3= Tkinter.Button(top, text ="Browser image 4", command = askopenfilename)  

#B.pack(padx=100, pady=100)
B.pack(padx=5, pady=10, side=LEFT)
B1.pack(padx=5, pady=20, side=LEFT)
B2.pack(padx=5, pady=30, side=LEFT)
B3.pack(padx=5, pady=40, side=LEFT)			


#C.pack()
top.mainloop()
import Tkinter
import tkMessageBox,tkFileDialog
from PIL import Image,ImageTk
from Tkinter import *
def askopenfilename():
        return tkFileDialog.askopenfile()
def helloCallBack():
			rot = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
			img = ImageTk.PhotoImage(rot)
			label2 = Label(self, image=img)
			label2.image = img
			label2.place(x=40, y=160)   
top = Tkinter.Tk()

   
#C = Tkinter.Canvas(top, bg="White", height=1000, width=1000)
  

B = Tkinter.Button(top, text ="Browser image 1", command = helloCallBack)
#B.place(bordermode=OUTSIDE, height=100, width=100)
B1 = Tkinter.Button(top, text ="Browser image 2", command = helloCallBack)
B2 = Tkinter.Button(top, text ="Browser image 3", command = helloCallBack)
B3= Tkinter.Button(top, text ="Browser image 4", command = helloCallBack)
#B.pack(padx=100, pady=100)
B.pack(padx=5, pady=10, side=LEFT)
B1.pack(padx=5, pady=20, side=LEFT)
B2.pack(padx=5, pady=30, side=LEFT)
B3.pack(padx=5, pady=40, side=LEFT)
#C.pack()
top.mainloop()
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
self=Tk()
frame = Frame(self)


def loadtemplate(self): 
	filename = tkFileDialog.askopenfilename()                
		
				
tk.Button(frame, text = "Browse", command = self.loadtemplate, width = 10)

frame.pack()
self.mainloop()



 
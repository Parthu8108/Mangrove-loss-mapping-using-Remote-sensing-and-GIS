from Tkinter import *
import Tkinter as tk
def askopenfile():
        return tkFileDialog.askopenfile()
self=tk.Tk()
self.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

self.mainloop()

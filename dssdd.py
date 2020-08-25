import Tkinter as tk
import tkFileDialog

def openfile():
    global filename
    filename = tkFileDialog.askopenfilename(title="Open file")

def printfile():
    print(filename)

def printspinbox():
    print(spinbox.get())

window = tk.Tk()

filename = "" # global variable

tk.Button(window, text='Browse', command=openfile).pack()
tk.Button(window, text='Print filename', command=printfile).pack()

spinbox = tk.Spinbox(window, from_=0, to=10)
spinbox.pack(pady=10)
tk.Button(window, text='Print spinbox value', command=printspinbox).pack()

window.mainloop()
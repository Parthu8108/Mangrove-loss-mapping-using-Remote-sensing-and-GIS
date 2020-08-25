import sys
import tkinter as tk
from PIL import Image,ImageTk,ImageFilter,ImageOps


global fname
fname = "Example.tif"


def browse_file():
    fname = tk.filedialog.askopenfilename(filetypes=(("Bitmap files", "*.bmp"), ("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*")))
    print(fname)
    return

def classify_obj():
    print("In Development")
    return


root = tk.Tk()
root.wm_title("Classify Image")

broButton = tk.Button(master=root, text='Browse', height=2, width=8, command=browse_file).grid(row=0, column=0, padx=2, pady=2)

frame1 = tk.Frame(root, width=500, height=400, bd=2).grid(row=1, column=0)
im = Image.open(fname)
photo = ImageTk.PhotoImage(im)
cv = tk.Canvas(frame1, height=390, width=490, background="white", bd=1, relief=tk.RAISED).grid(row=1,column=0)
cv.create_image(0, 0, image=photo, anchor='nw')

claButton = tk.Button(master=root, text='Classify', height=2, width=10, command=classify_obj).grid(row=0, column=1, padx=2, pady=2)

frame2 = tk.Frame(root, width=500, height=400, bd=1).grid(row=1, column=1)
cv = tk.Canvas(frame2, height=390, width=490, bd=2, relief=tk.SUNKEN).grid(row=1,column=1)

tk.mainloop()
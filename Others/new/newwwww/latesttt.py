import sys
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
from tkinter import filedialog as fd


def select_image():
	# grab a reference to the image panels
	global filename
 
	# open a file chooser dialog and allow the user to select an input
	# image
	#filename=tkFileDialog.askopenfilename(title="band 2 image")
	filename = fd.askopenfilename()
	print(filename)
	
		
def showimg():
	global panelA
	file
	if len(filename) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(filename)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		
		image = image.resize((230, 230), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		
		
	if panelA is None:
			# the first panel will store our original image
		panelA = Label(image=image)
		panelA.image = image
		panelA.place(x=10,y=10)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelA.configure(image=image)
		panelA.image = image
		
def showimg1():
	global panelA1
	file
	if len(filename) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image1 = cv2.imread(filename)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image1 = Image.fromarray(image1)
		
		image1 = image1.resize((230, 230), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image1 = ImageTk.PhotoImage(image1)
		
		
	if panelA1 is None:
			# the first panel will store our original image
		panelA1 = Label(image=image1)
		panelA1.image = image1
		panelA1.place(x=320,y=10)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelA1.configure(image=image1)
		panelA1.image = image1		
		
root = Tk()
panelA = None
panelA1 = None

 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn1 = Button(root, text="Band 2", command=select_image)
btn1.place(x=100,y=280)
btn11 = Button(root, text="Show", command=showimg)
btn11.place(x=150,y=280)
btn2 = Button(root, text="Band 3", command=select_image)
btn2.place(x=425,y=280)
btn22 = Button(root, text="Show", command=showimg1)
btn22.place(x=475,y=280)



root.mainloop()

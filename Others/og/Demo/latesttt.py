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
def select_image1():
	# grab a reference to the image panels
	global filename1
 
	# open a file chooser dialog and allow the user to select an input
	# image
	#filename=tkFileDialog.askopenfilename(title="band 2 image")
	filename1 = fd.askopenfilename()
	print(filename1)
def select_image11():
	# grab a reference to the image panels
	global filename2
 
	# open a file chooser dialog and allow the user to select an input
	# image
	#filename=tkFileDialog.askopenfilename(title="band 2 image")
	filename2 = fd.askopenfilename()
	print(filename2)
def select_image111():
	# grab a reference to the image panels
	global filename3
 
	# open a file chooser dialog and allow the user to select an input
	# image
	#filename=tkFileDialog.askopenfilename(title="band 2 image")
	filename3 = fd.askopenfilename()
	print(filename3)
	
		
def showimg():
	global panelA
	
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

	if len(filename1) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image1 = cv2.imread(filename1)
		
 
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

def showimg2():
	global panelA11
	file
	if len(filename2) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image11 = cv2.imread(filename2)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image11 = cv2.cvtColor(image11, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image11 = Image.fromarray(image11)
		
		image11 = image11.resize((230, 230), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image11 = ImageTk.PhotoImage(image11)
		
		
	if panelA11 is None:
			# the first panel will store our original image
		panelA11 = Label(image=image11)
		panelA11.image = image11
		panelA11.place(x=630,y=10)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelA11.configure(image=image11)
		panelA11.image = image11

def showimg3():
	global panelA111
	file
	if len(filename3) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image111 = cv2.imread(filename3)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image111 = cv2.cvtColor(image111, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image111 = Image.fromarray(image111)
		
		image111 = image111.resize((230, 230), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image111 = ImageTk.PhotoImage(image111)
		
		
	if panelA111 is None:
			# the first panel will store our original image
		panelA111 = Label(image=image111)
		panelA111.image = image111
		panelA111.place(x=950,y=10)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelA111.configure(image=image111)
		panelA111.image = image111		
		
root = Tk()
panelA = None
panelA1 = None
panelA11 = None
panelA111 = None

 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn1 = Button(root, text="Band 2", command=select_image)
btn1.place(x=80,y=280)
btn11 = Button(root, text="Show", command=showimg)
btn11.place(x=130,y=280)
btn2 = Button(root, text="Band 3", command=select_image1)
btn2.place(x=405,y=280)
btn22 = Button(root, text="Show", command=showimg1)
btn22.place(x=455,y=280)
btn3 = Button(root, text="Band 4", command=select_image11)
btn3.place(x=700,y=280)
btn33 = Button(root, text="Show", command=showimg2)
btn33.place(x=750,y=280)
btn4 = Button(root, text="Band 5", command=select_image111)
btn4.place(x=1030,y=280)
btn44 = Button(root, text="Show", command=showimg3)
btn44.place(x=1080,y=280)
btn5 = Button(root, text="Stack")
btn5.place(x=400,y=480)


root.mainloop()

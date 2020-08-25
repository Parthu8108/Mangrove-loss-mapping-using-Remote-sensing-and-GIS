import sys
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2

def select_image():
	# grab a reference to the image panels
	global panelA
 
	# open a file chooser dialog and allow the user to select an input
	# image
	path=tkFileDialog.askopenfilename(title="band 2 image")
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		
		image = image.resize((150, 150), Image.ANTIALIAS)
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
		

	
root = Tk()
panelA = None

 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn1 = Button(root, text="Band 2", command=select_image)
btn1.place(x=50,y=200)
#btn1.pack(side="top", fill="both", expand="yes", padx="10", pady="10")

#btn2.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

# kick off the GUI
root.mainloop()

pathabc=select_image1
print(pathabc)

import sys
from Tkinter import *
import Tkinter as tk    
import tkFont as tkfont 
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
import numpy as np;
from cv2 import *;
import matplotlib.pyplot as plt;
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FirstPage):
            page_name = F.__name__
            frame = F(parent=container,controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class FirstPage(tk.Frame):
	
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
       

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("FirstPage"))
       
        button1.pack()
      
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
			
	def select_image1():
		# grab a reference to the image panels
		global panelB
	 
		# open a file chooser dialog and allow the user to select an input
		# image
		path2 = tkFileDialog.askopenfilename(title="band 3 image")
		if len(path2) > 0:
			# load the image from disk, convert it to grayscale, and detect
			# edges in it
			image2 = cv2.imread(path2)
			
	 
			# OpenCV represents images in BGR order; however PIL represents
			# images in RGB order, so we need to swap the channels
			image2= cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
	 
			# convert the images to PIL format...
			image2 = Image.fromarray(image2)
			image2 = image2.resize((230, 230), Image.ANTIALIAS)
	 
			# ...and then to ImageTk format
			image2 = ImageTk.PhotoImage(image2)
			
		if panelB is None:
				# the first panel will store our original image
			panelB = Label(image=image2)
			panelB.image = image2
			panelB.place(x=320,y=10)
	 
				# while the second panel will store the edge map
			
			# otherwise, update the image panels
		else:
				# update the pannels
			panelB.configure(image=image2)
			panelB.image = image2
		return path2

	def select_image2():
		# grab a reference to the image panels
		global panelC
	 
		# open a file chooser dialog and allow the user to select an input
		# image
		path3 = tkFileDialog.askopenfilename(title="band 4 image")
		if len(path3) > 0:
			# load the image from disk, convert it to grayscale, and detect
			# edges in it
			image3 = cv2.imread(path3)
			
	 
			# OpenCV represents images in BGR order; however PIL represents
			# images in RGB order, so we need to swap the channels
			image3= cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
	 
			# convert the images to PIL format...
			image3 = Image.fromarray(image3)
			image3 = image3.resize((230, 230), Image.ANTIALIAS)
	 
			# ...and then to ImageTk format
			image3 = ImageTk.PhotoImage(image3)
			
		if panelC is None:
				# the first panel will store our original image
			panelC = Label(image=image3)
			panelC.image = image3
			panelC.place(x=630,y=10)
	 
				# while the second panel will store the edge map
			
			# otherwise, update the image panels
		else:
				# update the pannels
			panelC.configure(image=image3)
			panelC.image = image3
		return path3

	def select_image3():
		# grab a reference to the image panels
		global panelD
	 
		# open a file chooser dialog and allow the user to select an input
		# image
		path4 = tkFileDialog.askopenfilename(title="band 4 image")
		if len(path4) > 0:
			# load the image from disk, convert it to grayscale, and detect
			# edges in it
			image4 = cv2.imread(path4)
			
	 
			# OpenCV represents images in BGR order; however PIL represents
			# images in RGB order, so we need to swap the channels
			image4= cv2.cvtColor(image4, cv2.COLOR_BGR2RGB)
	 
			# convert the images to PIL format...
			image4 = Image.fromarray(image4)
			image4 = image4.resize((230, 230), Image.ANTIALIAS)
	 
			# ...and then to ImageTk format
			image4 = ImageTk.PhotoImage(image4)
			
		if panelD is None:
				# the first panel will store our original image
			panelD = Label(image=image4)
			panelD.image = image4
			panelD.place(x=950,y=10)
	 
				# while the second panel will store the edge map
			
			# otherwise, update the image panels
		else:
				# update the pannels
			panelD.configure(image=image4)
			panelD.image = image4
		return path4
		panelA = None
		panelB = None
		panelC = None
		panelD = None
		 
		# create a button, then when pressed, will trigger a file chooser
		# dialog and allow the user to select an input image; then add the
		# button the GUI
		btn1 = Button(text="Band 2", command=select_image)
		btn1.place(x=100,y=280)

		#btn1.pack(side="top", fill="both", expand="yes", padx="10", pady="10")
		btn2 = Button(text="Band 3", command=select_image1)
		btn2.place(x=425,y=280)
		#btn2.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
		btn3 = Button(text="Band 4", command=select_image2)
		btn3.place(x=720,y=280)
		btn4 = Button(text="Band 5", command=select_image3)
		btn4.place(x=1050,y=280)
		btn5 = Button(text="Stack")
		btn5.place(x=400,y=480)
		btn6 = Button(text="Next", command=nextWindow)
		btn6.place(x=1100,y=600)

			
			
class page2(tk.Frame):		

### init fn???
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
			image = image.resize((230, 230), Image.ANTIALIAS)
			# ...and then to ImageTk format
			image = ImageTk.PhotoImage(image)
		if panelA is None:
				# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.place(x=250,y=150)
	 				# while the second panel will store the edge map
						# otherwise, update the image panels
		else:
				# update the pannels
			panelA.configure(image=image)
			panelA.image = image
	def generate_image():
		# grab a reference to the image panels
		global panelB
# kick off the GUI		
		

root = Tk()

root=SampleApp()
root.mainloop()
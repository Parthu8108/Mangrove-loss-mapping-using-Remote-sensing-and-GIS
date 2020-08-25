import sys
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
import numpy as np;
from cv2 import *;
import matplotlib.pyplot as plt;
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support

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
	
		
		
root = Tk()
panelA = None
panelB = None
pathabc=select_image
print(pathabc)
btn1 = Button(root, text="ANN")
btn1.place(x=100,y=100)
btn2 = Button(root, text="KNN")
btn2.place(x=100,y=300)
btn3 = Button(root, text="Decision Tree")
btn3.place(x=80,y=500)
btn4 = Button(root, text="Upload Image", command=select_image)
btn4.place(x=320,y=420)
btn5 = Button(root, text="Generate Classified Image", command=generate_image)
btn5.place(x=600,y=420)
btn6 = Button(root, text="Accuracy")
btn6.place(x=1000,y=100)
btn7 = Button(root, text="Kappa Value")
btn7.place(x=1000,y=300)
root.mainloop()


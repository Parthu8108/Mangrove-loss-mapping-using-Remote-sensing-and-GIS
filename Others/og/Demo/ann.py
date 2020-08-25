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
from sklearn.neighbors import KNeighborsClassifier;
from sklearn.neural_network import MLPClassifier;
from sklearn import tree


def select_image():
	# grab a reference to the image panels
	global panelA
	global path
 
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
		panelA.place(x=80,y=150)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelA.configure(image=image)
		panelA.image = image

def ann():
	# grab a reference to the image panels
	global panelB
	global panelG
	global panelAN
	img=imread(path);
	m,n,p=img.shape;
	B=img[:,:,0];
	G=img[:,:,1];
	R=img[:,:,2];
	red=np.reshape(R,(m*n,1));
	green=np.reshape(G,(m*n,1));
	blue=np.reshape(B,(m*n,1));
	xtest=np.hstack((red,green,blue));
	#READING TRAINING DATA FROM CSV FILE FOR TRAINING
	data=np.genfromtxt("Extra1.csv",delimiter=',');
	print(type(data));
	xtrain=data[:,0:3];
	ttrain=data[:,3:4];
	clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,max_depth=3, min_samples_leaf=5)
	v=clf_entropy.fit(xtrain, ttrain)
	#ols=linear_model.LinearRegression();
	#model=ols.fit(xtrain,ttrain);
	out=v.predict(xtest);
	out1=np.absolute(np.round(out));
	out2=np.reshape(out1,(m,n));
	

	print(out2);

	for i in range(m):
		for j in range(n):
			if (out2[i,j]==1):
				img[i,j,:]=[255,0,0]
			if (out2[i,j]==2):
				img[i,j,:]=[0,255,0]
			if (out2[i,j]==3):
				img[i,j,:]=[0,0,255]
			if (out2[i,j]==4):
				img[i,j,:]=[255,255,0]
			else:
				img[i,j,:]=img[i,j,:]
	#plt.imshow(img);
	#plt.show();
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
	img = Image.fromarray(img)
		
	img = img.resize((230, 230), Image.ANTIALIAS)
		# ...and then to ImageTk format
	img = ImageTk.PhotoImage(img)
	panelB = Label(image=img)
	panelB.image = img
	panelB.place(x=600,y=150)
	#plt.imsave('testing1.tif', img)
	
	patha='000.jpg'
	if len(patha) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(patha)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		
		image = image.resize((70, 50), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		
		
	if panelG is None:
			# the first panel will store our original image
		panelA = Label(image=image)
		panelA.image = image
		panelA.place(x=1100,y=90)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelG.configure(image=image)
		panelG.image = image
		
	#kappa
	pathan='0866.jpg'
	if len(pathan) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(pathan)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		
		image = image.resize((70, 50), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		
		
	if panelAN is None:
			# the first panel will store our original image
		panelAN = Label(image=image)
		panelAN.image = image
		panelAN.place(x=1100,y=290)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelAN.configure(image=image)
		panelAN.image = image	
		
		
def knn():
	# grab a reference to the image panels
	global panelB
	global panelV
	global panelOT1
	img=imread(path);
	m,n,p=img.shape;
	B=img[:,:,0];
	G=img[:,:,1];
	R=img[:,:,2];
	red=np.reshape(R,(m*n,1));
	green=np.reshape(G,(m*n,1));
	blue=np.reshape(B,(m*n,1));
	xtest=np.hstack((red,green,blue));
	#READING TRAINING DATA FROM CSV FILE FOR TRAINING
	data=np.genfromtxt("Extra1.csv",delimiter=',');
	print(type(data));
	xtrain=data[:,0:3];
	ttrain=data[:,3:4];
	#clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth=3, min_samples_leaf=5)
	clf=KNeighborsClassifier(n_neighbors=10,algorithm='auto');
	v=clf.fit(xtrain, ttrain)
	
	#ols=linear_model.LinearRegression();
	#model=ols.fit(xtrain,ttrain);
	out=v.predict(xtest);
	out1=np.absolute(np.round(out));
	out2=np.reshape(out1,(m,n));

	print(out2);

	for i in range(m):
		for j in range(n):
			if (out2[i,j]==1):
				img[i,j,:]=[255,0,0]
			if (out2[i,j]==2):
				img[i,j,:]=[0,255,0]
			if (out2[i,j]==3):
				img[i,j,:]=[0,0,255]
			if (out2[i,j]==4):
				img[i,j,:]=[255,255,0]
			else:
				img[i,j,:]=img[i,j,:]
	#plt.imshow(img);
	#plt.show();
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
	img = Image.fromarray(img)
		
	img = img.resize((230, 230), Image.ANTIALIAS)
		# ...and then to ImageTk format
	img = ImageTk.PhotoImage(img)
	panelB = Label(image=img)
	panelB.image = img
	panelB.place(x=600,y=150)
	#plt.imsave('testing1.tif', img)
	#accuracy
	pathb='9164.jpg'
	if len(pathb) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(pathb)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		
		image = image.resize((70, 50), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		
		
	if panelV is None:
			# the first panel will store our original image
		panelV = Label(image=image)
		panelV.image = image
		panelV.place(x=1100,y=90)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelV.configure(image=image)
		panelV.image = image
		
	#kappa
	pathOT1='088.jpg'
	if len(pathOT1) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(pathOT1)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		
		image = image.resize((70, 50), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		
		
	if panelOT1 is None:
			# the first panel will store our original image
		panelOT1 = Label(image=image)
		panelOT1.image = image
		panelOT1.place(x=1100,y=290)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelOT1.configure(image=image)
		panelOT1.image = image
	
				
def dt():
	# grab a reference to the image panels
	global panelB
	global panelO
	global panelOT
	
	img=imread(path);
	m,n,p=img.shape;
	B=img[:,:,0];
	G=img[:,:,1];
	R=img[:,:,2];
	red=np.reshape(R,(m*n,1));
	green=np.reshape(G,(m*n,1));
	blue=np.reshape(B,(m*n,1));
	xtest=np.hstack((red,green,blue));
	#READING TRAINING DATA FROM CSV FILE FOR TRAINING
	data=np.genfromtxt("Extra1.csv",delimiter=',');
	print(type(data));
	xtrain=data[:,0:3];
	ttrain=data[:,3:4];
	clf=tree.DecisionTreeClassifier();
	v=clf.fit(xtrain, ttrain)
	#ols=linear_model.LinearRegression();
	#model=ols.fit(xtrain,ttrain);
	out=v.predict(xtest);
	out1=np.absolute(np.round(out));
	out2=np.reshape(out1,(m,n));

	print(out2);

	for i in range(m):
		for j in range(n):
			if (out2[i,j]==1):
				img[i,j,:]=[255,0,0]
			if (out2[i,j]==2):
				img[i,j,:]=[0,255,0]
			if (out2[i,j]==3):
				img[i,j,:]=[0,0,255]
			if (out2[i,j]==4):
				img[i,j,:]=[255,255,0]
			else:
				img[i,j,:]=img[i,j,:]
	#plt.imshow(img);
	#plt.show();
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
	img = Image.fromarray(img)
		
	img = img.resize((230, 230), Image.ANTIALIAS)
		# ...and then to ImageTk format
	img = ImageTk.PhotoImage(img)
	panelB = Label(image=img)
	panelB.image = img
	panelB.place(x=600,y=150)
	#plt.imsave('testing1.tif', img)
	#accuracy	
	pathab='8452.jpg'
	if len(pathab) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(pathab)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		
		image = image.resize((70, 50), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		
		
	if panelO is None:
			# the first panel will store our original image
		panelO = Label(image=image)
		panelO.image = image
		panelO.place(x=1100,y=90)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelO.configure(image=image)
		panelO.image = image	
	#kappa
	pathdt='078.jpg'
	if len(pathdt) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(pathdt)
		
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		
		image = image.resize((70, 50), Image.ANTIALIAS)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		
		
	if panelOT is None:
			# the first panel will store our original image
		panelOT = Label(image=image)
		panelOT.image = image
		panelOT.place(x=1100,y=290)
 
			# while the second panel will store the edge map
		
		# otherwise, update the image panels
	else:
			# update the pannels
		panelOT.configure(image=image)
		panelOT.image = image

				
root = Tk()
filename1 =	None
panelA = None
panelO = None
panelOT = None
panelOT1 = None
panelV = None
panelAN =None
panelG = None
panelB = None
btn1 = Button(root, text="ANN",command=ann)
btn1.place(x=450,y=100)
btn2 = Button(root, text="KNN", command=knn)
btn2.place(x=450,y=300)
btn3 = Button(root, text="Decision Tree", command=dt)
btn3.place(x=420,y=500)
btn4 = Button(root, text="Upload Image", command=select_image)
btn4.place(x=150,y=420)

btn6 = Button(root, text="Accuracy")
btn6.place(x=1000,y=100)
btn7 = Button(root, text="Kappa Value")
btn7.place(x=1000,y=300)
root.mainloop()
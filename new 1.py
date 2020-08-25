import Tkinter as tk
import sys
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
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

class Page2(Page):
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
	img=imread('Example.tif');
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
	clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
	 max_depth=3, min_samples_leaf=5)
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
	panelB.place(x=550,y=150)
	#plt.imsave('testing1.tif', img)
		



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       # p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        #b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
       # b3.pack(side="left")

        p1.show()

root = tk.Tk()
panelA = None
panelB = None
panelC = None
panelD = None
	 
	# create a button, then when pressed, will trigger a file chooser
	# dialog and allow the user to select an input image; then add the
	# button the GUI
btn1 = Button(root, text="Band 2", command=select_image)
btn1.place(x=100,y=280)
	#btn1.pack(side="top", fill="both", expand="yes", padx="10", pady="10")
btn2 = Button(root, text="Band 3", command=select_image1)
btn2.place(x=425,y=280)
#btn2.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
btn3 = Button(root, text="Band 4", command=select_image2)
btn3.place(x=720,y=280)
btn4 = Button(root, text="Band 5", command=select_image3)
btn4.place(x=1050,y=280)
btn5 = Button(root, text="Stack")
btn5.place(x=400,y=480)
btn6 = Button(root, text="Next")
btn6.place(x=1100,y=600)
# kick off the GUI
	
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
root.wm_geometry("400x400")
root.mainloop()
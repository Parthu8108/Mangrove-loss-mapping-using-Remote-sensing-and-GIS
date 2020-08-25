#IMPORTING PACKAGES FOR COMPUTING
import numpy as np;
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from cv2 import *;
import matplotlib.pyplot as plt;
from sklearn.neural_network import MLPClassifier;

#READING SATELLITE IMAGE FOR PROCESSING
img=imread('Example1.tif');
m,n,p=img.shape;
print(m,n,p);
B=img[:,:,0];
G=img[:,:,1];
R=img[:,:,2];
red=np.reshape(R,(m*n,1));
green=np.reshape(G,(m*n,1));
blue=np.reshape(B,(m*n,1));
xtest=np.hstack((red,green,blue));
#print(xtest);
#READING TRAINING DATA FROM CSV FILE FOR TRAINING
#Original wala dataset
data=np.genfromtxt("1000wala.csv",delimiter=',');
#print(type(data));
xtrain=data[:,0:3];
ttrain=data[:,3:4];
#READING TESTING DATASET
#Testing wala dataset
data1=np.genfromtxt("300wala.csv",delimiter=',');
xtest=data1[:,0:3];
ttest=data1[:,3:4];
#DEFINING MODEL
clf=MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(25,), random_state=1);
#FITTING MODEL
model=clf.fit(xtrain,ttrain);
#PREDICTING CLASSES
out=np.ravel(clf.predict(xtest));
#m1,n1=out.size;
#outnew=np.reshape(out,
con=confusion_matrix(out,ttest);
print(con);
correctly_classidied_value=np.sum(np.diagonal(con));
total=np.sum(con);
accuracy=float(correctly_classidied_value)/float(total);
print('accuracy=',accuracy);
a11=con.item((0,0));
a12=con.item((0,1));
a13=con.item((0,2));
a14=con.item((0,3));
a21=con.item((1,0));
a22=con.item((1,1));
a23=con.item((1,2));
a24=con.item((1,3));
a31=con.item((2,0));
a32=con.item((2,1));
a33=con.item((2,2));
a34=con.item((2,3));
a41=con.item((3,0));
a42=con.item((3,1));
a43=con.item((3,2));
a44=con.item((3,3));
users_accuracy1=float(a11)/float(a11+a21+a31+a41)
users_accuracy2=float(a22)/float(a12+a22+a32+a42)
users_accuracy3=float(a33)/float(a13+a23+a33+a43)
users_accuracy4=float(a44)/float(a14+a24+a34+a44)
print('users_accuracy1=',users_accuracy1*100);
print('users_accuracy2=',users_accuracy2*100);
print('users_accuracy3=',users_accuracy3*100);
print('users_accuracy4=',users_accuracy4*100);
producers_accuracy1=float(a11)/float(a11+a12+a13+a14)
producers_accuracy2=float(a22)/float(a21+a22+a23+a24)
producers_accuracy3=float(a33)/float(a31+a32+a33+a34)
producers_accuracy4=float(a44)/float(a41+a42+a43+a44)
print('producers_accuracy4=',producers_accuracy1*100);
print('producers_accuracy4=',producers_accuracy2*100);
print('producers_accuracy4=',producers_accuracy3*100);
print('producers_accuracy4=',producers_accuracy4*100);


print('cohen kappa score=',cohen_kappa_score(out,ttest));





#import zone
import math,os,sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
#________________________

# Zadanie 1
print("This is part 1")
u=[]
c=[]
lnU=[]
lnC=[]
def linfunc (x, a, b):
	return a*x+b

#IMPORT Z1
print("Importing DATA z1")
DATA1 = open('z1.txt', 'r')
for line in DATA1:
	data=line.split(' ')
	u.append(float(data[0]))
	c.append(float(data[1]))
	lnU.append(float(data[2]))
	lnC.append(float(data[3]))
DATA1.close
#____________________


#FIT
p0 = [-0.5, 5]                 # guessed params
w, _ = opt.curve_fit(linfunc, lnU, lnC, p0=p0) 
#print("Estimated Parameters", w)


#GRAPH lnC lnU
print("Making GRAPH z1")
fig, ax = plt.subplots()             
ax.plot(lnU, lnC,'ro' )
x=np.linspace(0,5,50)
ax.plot(x,linfunc(x,w[0],w[1]))
ax.legend()
plt.xlabel('ln U', fontsize=15, color='blue')
plt.ylabel('ln C', fontsize=15, color='blue')
plt.text(3,5.4,"y=ax+b, a=-0.35, b=5.53")
plt.grid(True)   
#plt.show()

#Obrabotka
print("Refactoring of DATA")
d=[]
e0=1/(4*math.pi*9)
for k in c:
	d.append(round((12*1000000/(4*math.pi*9))/k)/10)
#print(d[17])

R=round(10*d[17]*d[17]/(e0*24*0.1350*(u[17]+0.5)))/10
#print("Rho = ", R)




print("End of lab")

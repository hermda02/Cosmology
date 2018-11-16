import numpy as np
import matplotlib.pyplot as plt
import pylab

plt.style.use("ggplot")

x_ = np.arange(-15,15,0.01)

R = 5
harmonics = 5

tic = np.array([-R,0,R])
tick = ['-R','0','R']


def topHat(x):
	global R
	if R>=abs(x):  
		return 1
	else:
	 return 0

def b(n):
	n = int(n)
	if (n%2 != 0):
		return 4/(np.pi*n)
	else:
		return 0

def hatFourier(n,x):
	global R
	fourier = 0

	freq = (2*np.pi/(4*R))

	for i in range(1,n):
		fourier = fourier + b(i)*np.sin(freq*i*(x+5))
		
	return fourier

def fwhm(x,y):
	d = y - (max(y)/2)
	indexes = np.where(d>0)[0]
	return abs(x[indexes[-1]]-x[indexes[0]])


y = np.zeros(len(x_))

for i in range(len(x_)):
	y[i] = topHat(x_[i])

width = fwhm(x_,hatFourier(harmonics,x_))

print 'The full width half maximum is:', width, 'with', harmonics, 'harmonics'



plt.title("Top Hat Smoothing Function")
plt.xlabel('Radius')
plt.xticks(tic,tick)
plt.text(-13,1.25, 'Harmonics: 5, FWHM: 8.42')
plt.ylim(-0.05,2)
plt.plot(x_,y,x_,hatFourier(harmonics,x_),'b')
pylab.show()



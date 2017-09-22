import numpy as np
import matplotlib.pyplot as plt
import pylab

def rtemp(a):
	return 1.*(1./a)

def mtemp(a):
	return 1.*(1./a)**2

t = np.arange(0.0001,1,0.0001)

plt.figure(1)
plt.subplot(211)
plt.title('Radiation Temperature')
plt.plot(t,rtemp(t), 'bx')
plt.ylabel('Temperature')
plt.xscale('log')

plt.subplot(212)
plt.title('Gas Temperature')
plt.xscale('log')
plt.plot(t, mtemp(t), 'rx')
plt.xlabel('log(a)')
plt.ylabel('Temperature')
pylab.show()

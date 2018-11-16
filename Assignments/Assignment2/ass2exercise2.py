import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab
import scipy.integrate as integrate
from scipy.integrate import quad

def stepper():

	epsil = 0.003
	k = 0.65
	Sc = 2*np.pi/k
	N = int((Sc - 1) / epsil)

	
	Sn = np.zeros(N+1)
	delta = np.zeros(N+1)
	vari = np.zeros(N+1)
				
	#initialize the Gaussian

	Sn[0] = Sc					#initial smoothing size
	vari[0] = np.pi / Sc**4 	#initial variance of the GRF

	mu, sigma = 0, np.sqrt(vari[0])
	s = np.random.normal(mu,sigma,1)

	delta[0] = s

	for i in range(N):
		Sn[i+1] = Sn[i] - epsil
		vari[i+1] = np.pi / Sn[i+1]**4

		newvari = vari[i+1] - vari[i]
		newsigma = np.sqrt(newvari)

		step = np.random.normal(mu,newsigma,1)
		delta[i+1] = delta[i] + step

		# print(Sn[i+1])

	# print delta[N]
	return delta, delta[N]


M = 10000

tdelts = np.zeros(4200)
deltas = np.zeros(M)
noncrit = []
count = 0

for i in range(M):
	tdelts, deltas[i] = stepper()

	if all(d < 1 for d in tdelts):
		noncrit.append(deltas[i])
	
delmin = min(deltas)
delmax = max(deltas)
sig = np.sqrt(np.pi)

x = np.linspace(delmin,delmax,1000)

ncmin = min(noncrit)
ncmax = max(noncrit)

x2 = np.linspace(ncmin,ncmax,1000)

#plotting my histograms with PDFs

#norming = quad((mlab.normpdf(x2,0,sig)-mlab.normpdf(x2,2,sig)),ncmin,ncmax)

plt.hist(deltas, bins=40, normed=True, color = 'goldenrod')
plt.plot(x, mlab.normpdf(x,0,sig), color = 'black')
plt.title("Histogram of overdensities")
plt.xlabel("Overdensity")
plt.ylabel("Probability")

plt.show()

plt.hist(noncrit,bins=40, normed=True, color = 'goldenrod')
plt.title("Histogram of overdensities that \n remain less than critical density")
plt.plot(x2,(2.34*(mlab.normpdf(x2,0,sig)-mlab.normpdf(x2,2,sig))), color='black')
plt.xlabel("Overdensity")
plt.ylabel("Probability")

plt.show()


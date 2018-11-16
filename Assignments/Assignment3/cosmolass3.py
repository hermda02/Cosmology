import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

sigma_t = 6.65*10**(-25) # [cm2]
c = 29979245800. #[cm/s]

x = np.linspace(0,10,10000)
#mpc2km = 3.08567758e+19 

def H(z):
	omega_m = 0.308 #[1]
	omega_l = 0.692 #[1]
	H0 = 2.197e-18 #[1/s]
	# h0 = 67.8 #[km/s/Mpc]
	# h0 /= mpc2km #[1/s]
	return H0*np.sqrt(omega_l + omega_m*(1+z)**3) #Hubble constant as a function of redshift [1/s]

def nh(z):
	return 1.9*10**(-7)*(1+z)**3 # number density of hydrogen as a function of redshift [cm-3]

def inty(z):
	return (nh(z)*sigma_t)/((1+z)*H(z)) # integrand for the optical depth [s cm-1]

def taue(z):
	res = np.zeros_like(z) #create array equal to the number of z's we're calculating
	for i,z in enumerate(z): #for loop for integrating for each z
		result,err = integrate.quad(inty, 0, z)
		res[i]=result
	return c*res # multiply by the speed of light to end up with optical depth

plt.title("Optical Depth of the Ionized IGM")
plt.xlabel("Redshift (z)")
plt.ylabel("Optical Depth")
plt.grid(True)
plt.plot(x,taue(x))
plt.show()


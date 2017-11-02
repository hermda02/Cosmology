import numpy as np
import matplotlib.pyplot as plt
import pylab

def diff(Omega_m,Omega_l):
	print(Omega_m,Omega_l)
	
	# want to solve d^2(del)/dt^2 + da/dt*(1/a)*d(del)/dt = 1.5(del)Omega_m*h_0^2

	N = 100000
	C = 1

	h_0 = 1 #normalized Hubble Constant
	dt = 1e-4
	
	rho_c = (3*h_0**2)/(8*np.pi)	
	rho_0 = Omega_m*rho_c

	t = np.zeros(N+1)

	at = np.zeros(N+1)
	adt = np.zeros(N+1)

	delta = np.zeros(N+1)
	deltad = np.zeros(N+1)
	deltadd = np.zeros(N+1)

	rho = np.zeros(N+1)

	at[0] = np.exp(-3)
	adt[0] = h_0*np.sqrt(Omega_m/(at[0]**3)+Omega_l)*at[0]

	delta[0] = np.exp(-3)
	deltad[0] = C*adt[0]
	#def dda(a):
	#	da = h_0*np.sqrt(Omega_m/(a**3)+Omega_l)*a[0]
	#	return da
	#for i in range(0,N-1):
	#	deltat[i] = dt*i
	#	a = at[i]
	#	dad = dda(a)	
	#	print at[i]
	#	at[i+1] = (dad +a)
			


		# print(at[i])
	for i in range(N):
		
		if at[i] <= 1:
			t[i+1] = t[i] + dt
			at[i+1] = at[i] + dt*adt[i]
			adt[i+1] = at[i+1]*h_0*np.sqrt(Omega_m/(at[i+1]**3)+Omega_l)

			rho[i] = rho_0/(at[i]**3)

			deltadd[i] = -2*(adt[i]/at[i])*deltad[i] + 4*np.pi*rho[i]*delta[i]
			deltad[i+1] = deltad[i] + dt*deltadd[i]
			delta[i+1] = delta[i] + dt*deltad[i+1]
		C = i
		

	at = at[:C]; delta = delta[:C]
	adt = adt[:C]; deltad = deltad[:C]

	f = at/delta*deltad/adt	
	z = 1./at - 1.

	return at[:i], delta[:i], t[:i], z, f

omega1m = [1., 0.3, 0.8]
omega1delta = [0.,.7,.2]
for i in range(len(omega1m)):
	at1, delta1, t1, z1, f1 = diff(omega1m[i],omega1delta[i])
	plt.plot(np.log(at1),np.log(delta1))
plt.title('Overdensity as a function of the scale factor')
plt.xlabel('log(a)')
plt.ylabel(r'$log(\delta)')
plt.legend(r'$\omega_{m} = ', omega1m)
plt.hold('on')
pylab.show()

print np.log(at1)

for i in range(len(omega1m)):
	at1, delta1, t1, z1, f1 = diff(omega1m[i],omega1delta[i])
	plt.plot(z1,f1)
plt.title('The growth factor as a function of the redshift')
plt.xlabel('z')
plt.ylabel('f')
plt.legend(r'$\omega_{m} = ', omega1m)
plt.hold('on')
pylab.show()





	

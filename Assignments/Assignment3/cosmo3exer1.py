import matplotlib.pyplot as plt
import numpy as np

G = 6.67e-8 #[cm3 g-1 s-2]
k = 1.38e-16 #[erg s-1]
rhoc = 8.64e-30 #[g cm-3]
omegab=0.048
mu=0.588
T = 1e4 #[K]
mp = 1.67e-24 #[g]
omega_m = 0.308 #[1]
omega_l = 0.692 #[1]
H0 = 2.197e-18 #[1/s]
z = 4

lamb_j = 1e-5*np.sqrt(15*k*T/(4*np.pi*G*rhoc*mu*mp*omegab)) #[km]

print(lamb_j)

H = H0*np.sqrt(omega_l + omega_m*(1+z)**3)

v = H*lamb_j*(1+z)**(-3/2)

print(v)

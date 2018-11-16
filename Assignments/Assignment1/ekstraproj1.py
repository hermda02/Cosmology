from numpy import zeros, log, pi, exp, sqrt
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, hold, legend


#_d = derivert
#_dd = dobbelderivert

def adelta(omega_m, omega_lambda):
    N = 1000000
    dt = 1e-4

    H_0 = 1     #hubble parameter
    C = 1 
    rho_crit = (3*H_0**2)/(8*pi)
    rho_0 = omega_m*rho_crit

    t = zeros(N+1)

    a = zeros(N+1)
    a_d = zeros(N+1)

    delta = zeros(N+1)
    delta_d = zeros(N+1)
    delta_dd = zeros(N+1)

    rho = zeros(N+1)

    a[0] = exp(-3)
    a_d[0] = a[0]*H_0*sqrt(omega_m*a[0]**(-3) + omega_lambda)
    delta[0] = exp(-3)
    delta_d[0] = C*a_d[0]


    for i in range(N):
        if a[i] <= 1:
            t[i+1] = t[i] + dt
            a[i+1] = a[i] + dt*a_d[i]
            a_d[i+1] = a[i+1]*H_0*sqrt(omega_m*a[i+1]**(-3) + omega_lambda)

            
            rho[i] = rho_0/(a[i]**3)

            delta_dd[i] = -2*(a_d[i]/a[i])*delta_d[i] + 4*pi*rho[i]*delta[i]
            delta_d[i+1] = delta_d[i] + dt*delta_dd[i]
            delta[i+1] = delta[i] + dt*delta_d[i+1]
        else:
	    C = i
            break

    #strip the trailing zeros since we make N+1 arrays
    a = a[:C]; delta = delta[:C]
    a_d = a_d[:C]; delta_d = delta_d[:C]

    #growth factor of d(ln delta)/d(ln a)
    f = a/delta*delta_d/a_d
    z = 1./a - 1.

    #plot(log(a),log(delta))
    #show()

    #plot(z,f)
    #show()

    return a[:i], delta[:i], t[:i], z, f




omega1m = [1., 0.3, 0.8]
omega1delta = [0.,.7,.2]
for i in range(len(omega1m)):
	a1, delta1, t1, z1, f1 = adelta(omega1m[i],omega1delta[i])
	plot(log(a1),log(delta1))
title('Overdensity as a function of the scale factor')
xlabel('log(a)')
ylabel(r'$log(\delta)')
legend(r'$\omega_{m} = ', omega1m)
hold('on')
show()

for i in range(len(omega1m)):
	a1, delta1, t1, z1, f1 = adelta(omega1m[i],omega1delta[i])
	plot(z1,f1)
title('The growth factor as a function of the redshift')
xlabel('z')
ylabel('f')
legend(r'$\omega_{m} = ', omega1m)
hold('on')
show()

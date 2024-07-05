import matplotlib.pyplot as plt
from numpy import arange


N_x = 100
x_start = 0
x_end = 1
h = (x_end - x_start) / N_x
D = 1
t_max = 1
tau = h**2 / (2*D)
N_t = round(t_max / tau)

k = (tau*D) / (h**2)
T0 = []
T1 = []
x = []

for i in arange(0, x_end + h, h):
    T0.append(0)
    T1.append(0)
    x.append(i)

tt = tau
for n in range(N_t):
    t = n * tau
    for i in range(N_x):
        T1[i]= k * T0[i+1] + (1 - 2*k) * T0[i] + k * T0[i-1]

    T1[0] = 2*h + T1[1]
    T1[N_x] = 1
    T0, T1 = T1, T0
    
    if t == tt:
        plt.plot(x, T0)
        tt *= 2


plt.xlabel('стержень')
plt.ylabel('температура')
plt.grid()
plt.xlim(0, 1)
plt.show()
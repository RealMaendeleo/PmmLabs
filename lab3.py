from math import pi, sin
from numpy import arange
import matplotlib.pyplot as plt

N_x = 100
x_start = 0
x_end = 1
h = (x_end - x_start) / N_x
t = 4
c = 1
tau = h / c
K = round(t / tau)

u = []
u0 = []
u1 = []
x = []

for i in arange(0, N_x + 1, h):
    x.append(i)
    u0.append(0)
    u1.append(tau * sin(2*pi*x[round(i/h)]))
    u.append(0)

u0[0]=0
u0[N_x]=0
u1[0]=0
u1[N_x]=0
u[0]=0
u[N_x]=0

tt=tau

plt.plot(x, u1)
for j in range(1, K):
    for i in range(1, N_x):
        u[i] = 2*u1[i] - u0[i] + ((tau**2) / (h**2)) * (u1[i+1] - 2*u1[i] + u1[i-1])
    u[0] = 0
    u[N_x] = 0
    u0 = u1[:]
    u1 = u[:]
    t = j*tau
    if t == tt:
        plt.plot(x, u1)
        tt=tt*2


plt.grid()
plt.xlim(0, 1)
plt.plot(x, u1)
plt.show()
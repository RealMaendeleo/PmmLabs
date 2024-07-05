import matplotlib.pyplot as plt
from numpy import arange
from math import pi, sin
from matplotlib.animation import FuncAnimation

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

# НУ
for i in arange(0, x_end + 1, h):
    x.append(i)
    u0.append(0)
    u1.append(sin(2*pi*x[round(i/h)])) 
    u.append(0)

u0[0]=0
u1[0]=0
u0[N_x]=0
u1[N_x]=0
u[0]=0
u[N_x]=0

fig, ax = plt.subplots()
chart, = ax.plot(0, 0)

def anim(layer):
    global chart, u, x, u0, u1

    for i in range(1, N_x):
        u[i] = 2*u1[i] - u0[i] + (((c * tau) / h)**2) * (u1[i+1] - 2*u1[i] + u1[i-1])
    u[0] = 0
    u[N_x] = 0
    u0 = u1[:]
    u1 = u[:]
    chart.set_xdata(x)
    chart.set_ydata(u)
    return chart

animat = FuncAnimation(fig, func=anim, interval = 10)
plt.grid()
plt.xlim(0, 1)
plt.ylim(-20, 20)
plt.show()
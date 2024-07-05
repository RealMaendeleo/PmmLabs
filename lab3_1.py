import numpy as np
from math import exp
import matplotlib.pyplot as plt
from copy import deepcopy
from matplotlib.animation import FuncAnimation

U = []
a = 1
h = 0.02
N = round (a / h)
t = 100
tau = 0.01
K =  round(t / tau)

u = []
u0 = []
u1 = []
x = []

for i in range(0, N + 1):
    j = i * h
    x.append(j)
    u0.append(0)
    u1.append(((tau ** 2 )/2) * 0 + u0[i])
    u.append(0)
u0[0] = 0
u1[0] = 0
u0[N] = 0
u1[N] = 0
u[0] = 0
u[N] = 0

tt = tau
plot_count = 0

U.append(deepcopy(u1))
plot_count += 1
for j in range(1, K):
    for i in range(1, N):
        u[i] = 2 * u1[i] - u0[i] + ((tau ** 2) / (h ** 2)) * (u1[i+1]-2*u1[i]+u1[i-1])
    u[0] = 0
    t = j*tau
    u[N] = t*exp(-t)
    u0 = u1[:]
    u1 = u[:]
    # if t == tt:
    U.append(deepcopy(u1))
    plot_count += 1
        # tt *= 2

U.append(deepcopy(u1))
plot_count += 1

fig, ax = plt.subplots()
ax.set_xlim(0.0, 1.0)
ax.set_ylim(-1.0, 1.0)
ax.set_xlabel('Координата X')
ax.set_ylabel('Распределение T')
ln, = ax.plot(0, 0)

def animation_frame(i):
    global U
    global x
    if i >= plot_count - 1:
        animation.event_source.stop()
    ln.set_xdata(deepcopy(x))
    ln.set_ydata(U[i])
    return ln,
animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, plot_count, 1), interval=10)

plt.show()
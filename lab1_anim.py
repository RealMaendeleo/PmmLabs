import matplotlib.pyplot as plt
from numpy import arange
from matplotlib.animation import FuncAnimation

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

fig, ax = plt.subplots()
chart, = ax.plot(0, 0)
ax.set_xlabel('стержень')
ax.set_ylabel('температура')

def anim(layer):
    global chart, T0, T1, x

    for i in range(0, N_x):
        T1[i] = k * T0[i-1] + (1 - 2*k) * T0[i] + k * T0[i+1]

    T1[0] = 2*h + T1[1]
    T1[N_x] = 1
    T0, T1 = T1, T0

    chart.set_xdata(x)
    chart.set_ydata(T0)
    return chart


animat = FuncAnimation(fig, func=anim, interval = 10)
plt.grid()
plt.xlim(0, 1)
plt.ylim(-0.2, 1.2)
plt.show()
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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

A = []
B = []
a = []
b = []
c = []
f = []
T = []

for i in arange(0, x_end + h, h):
    T0.append(0)
    T1.append(0)
    T.append(0)
    A.append(0)
    B.append(0)
    a.append(0)
    b.append(0)
    c.append(0)
    f.append(0)
    x.append(i)

fig, (ax1, ax2) = plt.subplots(1, 2)
chart1, = ax1.plot(0.5, 0, color='red')
ax1.set_ylabel('температура')
ax1.set_xlim(0, 1)
ax1.set_ylim(-0.2, 1.2)
ax1.grid()
chart2, = ax2.plot(0.5, 0, color='green')
ax2.set_xlim(0, 1)
ax2.set_ylim(-0.2, 1.2)
ax2.grid()


def explicit(layer):
    global chart1, T0, T1, x

    for i in range(0, N_x):
        T1[i] = k * T0[i-1] + (1 - 2*k) * T0[i] + k * T0[i+1]

    T1[0] = 2*h + T1[1]
    T1[N_x] = 1
    T0, T1 = T1, T0

    chart1.set_xdata(x)
    chart1.set_ydata(T0)
    return chart1


def implicit(layer):
    global chart1, T0, T1, x
    c[0]=1
    b[0]=1
    f[0]=0
    for i in range (1, N_x):
        a[i] = tau / (h*h)
        b[i] = a[i]
        c[i] = 1 + 2*a[i]
        f[i] = T[i]
    A[0] = b[0] / c[0]
    B[0] = 2*h
    for i in range(1, N_x):
        A[i] = b[i] / (c[i] - a[i]*A[i-1])
        B[i] = (f[i] + a[i]*B[i-1]) / (c[i] - a[i]*A[i-1])
    T[N_x] = 1
    for i in arange ((N_x-1), 0, -1):
        T[i] = A[i]*T[i+1] + B[i]
    T[0] = 2*h + T[1]

    chart2.set_xdata(x)
    chart2.set_ydata(T)
    return chart2


labels = ['явная', 'неявная']
fig.legend([chart1, chart2], labels=labels)
animat1 = FuncAnimation(fig, func=explicit, interval = 10)
animat2 = FuncAnimation(fig, func=implicit, interval = 10)
plt.show()
import matplotlib.pyplot as plt
from numpy import arange
from matplotlib.animation import FuncAnimation

def D(u):
    return 2*u**(1/2)

N_x = 100
x_start = 0
x_end = 1
h = (x_end - x_start) / N_x

#!ГУ
leftBorder = -2 #? 2 рода
rightBorder = 1 #? 1 рода

sizeX = round((x_end-x_start) / h + 1) #! количество шагов
 
#! НУ
T0 = [0 for _ in range(sizeX)] #? текущий
T1 = [0 for _ in range(sizeX)] #? следующий


#! ГУ справа

T0[sizeX-1] = rightBorder
T1[sizeX-1] = rightBorder



#! коэф. теплопроводности
d = []
for i in range (0, sizeX):
    d.append(D(T0[i]))

dt =  (h ** 2) / (2 * max(d)) #! шаг по времени


x = []
for i in arange(0, 1+h, h):
    x.append(i)

fig, ax = plt.subplots()
chart, = ax.plot(0, 0)

def anim(layer):
    global chart, T0, T1, x

    for i in range (0, sizeX):
        d[i] = D(T0[i])
    dt = (h ** 2) / (2 * max(d))  #! пересчётшага по времени для устойчивости
    k = dt / (h ** 2)
    for i in range (1, sizeX-1):
        DL = (D(T0[i-1]) + D(T0[i])) / 2
        DR = (D(T0[i+1]) + D(T0[i])) / 2
        T1[i] = k * DL * T0[i - 1] + (1 - k * (DL + DR)) * T0[i] + k * DR * T0[i + 1]
    
    T1[0] = T1[1] - leftBorder * h

    tmp = T1[:]
    T1 = T0[:]
    T0 = tmp[:]

    chart.set_xdata(x)
    chart.set_ydata(T0)
    return chart


animat = FuncAnimation(fig, func=anim, interval = 10)
plt.grid()
plt.xlim(0, 1)
plt.ylim(-0.2, 1.2)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
from math import cos, pi, atan

def D (u):
    return cos(u*pi)

#!ГУ
leftBorder = -2 #? 2 рода
rightBorder = 1 #? 1 рода


startX = 0
endX = 1

dx = 0.01 #! шаг по пространственной координате

sizeX = round((endX-startX) / dx + 1) #! количество шагов
 
#! НУ
u0 = [0 for _ in range(sizeX)] #? текцщий
u1 = [0 for _ in range(sizeX)] #? следущий


#! ГУ справа

u0[sizeX-1] = rightBorder
u1[sizeX-1] = rightBorder



#! коэф. теплопроводности
d = []
for i in range (0, sizeX):
    d.append(D(u0[i]))

dt =  (dx ** 2) / (2 * max(d)) #! шаг по времени
 

x = []
for i in arange(0, 1+dx, dx):
    x.append(i)
plt.grid()
tt=0
time = 1
for t in arange (0, 1, dt):
    tt=tt+1
    for i in range (0, sizeX):
        d[i] = D(u0[i])
    dt = (dx ** 2) / (2 * max(d))  #! пересчётшага по времени для устойчивости
    k = dt / (dx ** 2)
    for i in range (1, sizeX-1):
        DL = (D(u0[i-1]) + D(u0[i])) / 2
        DR = (D(u0[i+1]) + D(u0[i])) / 2

        u1[i] = k * DL * u0[i - 1] + (1 - k * (DL + DR)) * u0[i] + k * DR * u0[i + 1]
    
    u1[0] = u1[1] - leftBorder * dx

    tmp = u1[:]
    u1 = u0[:]
    u0 = tmp[:]
    if tt == time:
        plt.plot(x, u1)
        time=time*2


plt.plot(x, u1)
plt.show()
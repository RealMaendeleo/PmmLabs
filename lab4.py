import matplotlib.pyplot as plt
import numpy as np
from math import radians, cos, sin
from copy import deepcopy
import matplotlib as mpl


def dM1(dy, dt, p1, i, j, u):
    if u >= 0:
        return dy * dt * p1[i][j] * u
    else:
        return dy * dt * p1[i + 1][j] * u


def dM2(dy, dt, p1, i, j, u):
    if u < 0:
        return dy * dt * p1[i][j] * u
    else:
        return dy * dt * p1[i - 1][j] * u


def dM3(dx, dt, p1, i, j, v):
    if v >= 0:
        return dx * dt * p1[i][j] * v
    else:
        return dx * dt * p1[i][j + 1] * v


def dM4(dx, dt, p1, i, j, v):
    if v < 0:
        return dx * dt * p1[i][j] * v
    else:
        return dx * dt * p1[i][j - 1] * v


def Q(i, j, N_points):
    return int((i == N_points / 2.5) and (j == N_points / 2))

def Q1(i, j, N_points):
    return int((i == N_points / 2) and (j == N_points / 2.5))

dx = 20
dy = 20
dt = 0.5
C = 10

airAngle = radians(150)
D = 2
u = C * cos(airAngle)
v = C * sin(airAngle)

N_points = 50
N_t = 200

p1 = [[0.0 for _ in range(N_points)] for _ in range(N_points)]
p2 = [[0.0 for _ in range(N_points)] for _ in range(N_points)]
pps = []

X = [x * dx for x in range(N_points)]
Y = [y * dy for y in range(N_points)]


for t in range(N_t):
    for i in range(N_points):
        for j in range(N_points):
            if t == 0:
                p1[i][j] = 0
            elif i == 0 or i == N_points - 1 or j == 0 or j == N_points - 1:
                p2[i][j] = 0
            else:
                p2[i][j] = p1[i][j] - (1.0 / (dx * dy)) * (dM1(dy, dt, p1, i, j, u) - dM2(dy, dt, p1, i, j, u) +
                                       dM3(dx, dt, p1, i, j, v) - dM4(dx, dt, p1, i, j, v)) + (dt / (dx * dx)) * (D * C * ((p1[i + 1][j] - p1[i][j]) - (p1[i][j] - p1[i - 1][j]))) + (dt / (dy * dy)) * (D * C * ((p1[i][j + 1] - p1[i][j]) - (p1[i][j] - p1[i][j - 1]))) + dt * Q1(i, j, N_points) + dt * Q(i, j, N_points)

    for j in range(N_points):
       p2[0][j] = p2[1][j]
       p2[N_points - 1][j] = p2[N_points - 2][j]

    for i in range(N_points):
       p2[i][0] = p2[i][1]
       p2[i][N_points - 1] = p2[i][N_points - 2]

    for i in range(N_points):
        for j in range(N_points):
            p1[i][j] = p2[i][j]

    pps.append(deepcopy(p1))

max_pps_value = -1
for ppp in pps:
    maximum = np.amax(ppp)
    if max_pps_value < maximum:
        max_pps_value = maximum

# print(max_pps_value)
plt.ion()
plt.imshow(pps[1], mpl.cm.rainbow, origin='lower')
plt.clim(0, max_pps_value)
for index in range(1, len(pps)):
    plt.clf()
    Xs, Ys = np.meshgrid(X, Y)
    #contourt = plt.contour(Xs, Ys, pps[index], 10, colors='black')
    plt.contourf(Xs, Ys, pps[index], 10, cmap=plt.cm.cool)
   # plt.clabel(contourt, inline=1, fontsize=1)

    plt.colorbar()
    plt.draw()
    plt.gcf().canvas.flush_events()
    plt.pause(0.1)

plt.ioff()
plt.title("Finished")
plt.show()
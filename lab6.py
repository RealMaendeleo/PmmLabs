import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from math import sin

dx = 0.05
dy = 0.05
a = 1.0
b = 1.0

x = np.arange(0,a+dx,dx).round(3)
y = np.arange(0,b+dy,dy).round(3)
nx = len(x)
ny = len(y)


U = np.zeros((nx, ny))
p = np.zeros((nx, ny))

# Граничные условия
for i in range(1, nx):
    U[(nx-1), i] = 2*y[i] # Справа
    U[0, i] = 0.5*sin(np.pi*y[i]) # Слева

for i in range(1, ny):
    U[i, (ny-1)] = 2*x[i] # Сверху
    U[i, 0] = 3*x[i]*(1-x[i]) # Снизу

maxit = 500 # Максимальное количество итераций

for iteration in range(0, maxit):
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            ro = 4*x[i]*x[i]*(y[j]-y[j]*y[j])
            U[i, j] = 0.25 * (U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1]) - dx * dx / 4 * ro

X, Y = np.meshgrid(x, y)
plt.suptitle('Решение уравнения Пуассона')
plt.contourf(X, Y, U, 30, cmap=cm.gist_heat)
plt.colorbar()
plt.show()

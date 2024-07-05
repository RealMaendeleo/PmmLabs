import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры
D = 0.1  # Коэффициент диффузии
V_x = 0.5  # Скорость ветра по оси x

# Задаем пространственную сетку
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
z = np.linspace(0, 1, 100)
X, Y, Z = np.meshgrid(x, y, z)

# Начальное условие (например, равномерное распределение концентрации)
u0 = np.ones_like(X)

# Шаг по времени
dt = 0.01

# Численное решение
for _ in range(100):
    u0 += dt * (D * (np.gradient(np.gradient(u0, axis=0), axis=0) +
                    np.gradient(np.gradient(u0, axis=1), axis=1) +
                    np.gradient(np.gradient(u0, axis=2), axis=2)) +
                V_x * np.gradient(u0, axis=0))

# Визуализация результата
plt.figure()
plt.imshow(u0[:, :, 50], origin='lower', extent=(0, 1, 0, 1))
plt.colorbar(label='Концентрация')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Распределение концентрации в трехмерной системе координат')
plt.show()

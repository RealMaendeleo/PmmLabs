from numpy import arange
import matplotlib.pyplot as plt


N_x = 100
x_start = 0
x_end = 1
h = (x_end - x_start) / N_x 
D = 1
t_max = 1
tau = h**2 / (2*D)
N_t = round(t_max / tau) 

X = []
A = []
B = []
a = []
b = []
c = []
f = []
T = []

for i in arange(0, x_end + h, h):
    T.append(0)
    A.append(0)
    B.append(0)
    a.append(0)
    b.append(0)
    c.append(0)
    f.append(0)
    X.append(i)

tt = tau
for n in range (N_t):
    t = n * tau
    c[0]=1
    b[0]=1
    f[0] = 0
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
    
    if t == tt:
        plt.plot(X, T)
        tt *= 2


plt.grid()
plt.xlim(0, 1)
plt.show()
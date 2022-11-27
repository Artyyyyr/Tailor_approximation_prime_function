import matplotlib.pyplot as plt
import numpy as np
from numpy import log, e, sin, cos
start = -6.
end = 6.
step = 0.000001
x = np.arange(start, end, step)
y = sin(x)
n = 100000
noise = 100
def derivative(x, y):
    new_y = []
    for i in range(len(y) - 1):
        dx = x[i] - x[i + 1]
        dy = y[i] - y[i + 1]
        new_y.append(dy/dx)
    return new_y

def fit_hight_primary(x, y):
    new_y = []
    for i in range(len(y) - 1):
        new_y.append((y[0] * x[i] + (derivative(x, y)[0] * pow(x[i] - x[0], 2))/2 + (derivative(x[0:len(x) - 1], derivative(x, y))[0] * pow(x[i] - x[0], 3))/6))
        # print(i/(len(y) - 1))
    hight = y[0] - new_y[0]
    for i in range(len(new_y)):
        new_y[i] = new_y[i] + hight
    return new_y

def primary(x, y):
    new_y = []
    for i in range(len(y) - 1):
        #new_y.append((y[0] * x[i] +
        #              (derivative(x, y)[0] * pow(x[i] - x[0], 2))/2 +
        #              (derivative(x[0:len(x) - 1], derivative(x, y))[0] * pow(x[i] - x[0], 3))/6))
        d0 = (x[1] - x[0])/(y[1] - y[0])

        if -noise > d0  or d0 > noise:
            new_y.append(y[len(y)-1])
            print("noise reduced")
            continue

        d1 = (x[2] - x[1])/(y[2] - y[1])
        d2 = (x[3] - x[2]) / (y[3] - y[2])
        d3 = (x[4] - x[3]) / (y[4] - y[3])
        dd0 = (d1 - d0)/(x[1] - x[0])
        dd2 = (d3 - d2)/(x[3] - x[2])
        ddd = (dd2 - dd0)/(x[2] - x[0])
        new_y.append(y[0] * x[i] +
                     d0 * pow(x[i] - x[0], 2)/2 +
                     dd0 * pow(x[i] - x[0], 3)/6 +
                     ddd * pow(x[i] - x[0], 4)/24)
        #print(i/(len(y) - 1)) + ddd * pow(x[i] - x[0], 4)/24
    return new_y

def t(x, y, n):
    t = []
    n = int(n)
    for i in range(n):
        d0 = (x[1] - x[0]) / (y[1] - y[0])
        d1 = (x[2] - x[1]) / (y[2] - y[1])
        dd0 = (d1 - d0) / (x[1] - x[0])
        t.append(y[0] +
                 d0 * (x[i] - x[0]) +
                 dd0 * pow(x[i] - x[0], 2) / 2)
    return t


def partial_primary(x, y, n, h):
    new_y = []
    step = int(len(x)/n)
    print("step " + str(step))
    up = 0
    for i in range(n):
        list = primary(x[i*step:(i+1)*step], y[i*step:(i+1)*step])
        der = (list[len(list) - 1] - list[len(list) - 2])
        list.append(list[len(list) - 1] + der)
        if i != 0:
            up = new_y[len(new_y)-1] - list[0] + (new_y[len(new_y)-1] - new_y[len(new_y)-2])
        for j in list:
            new_y.append(j + up)
    for i in range(len(new_y)):
        new_y[i] = new_y[i] + h
    return new_y
# f(x) = f(c) + f(c)' * (x - c) + (f(c)'' * (x - c)^2)/2 + (f(c)''' * (x - c)^3)/6
# F(x) = f(c) * x + (f(c)' * (x - c)^2)/2 + (f(c)'' * (x - c)^3)/6 + (f(c)''' * (x - c)^4)/24

plt.plot(x, y)
py = partial_primary(x, y, n, 0)
print(len(py))
print(len(x))
plt.plot(x[0:len(py)], py)
dx = derivative(x, py)

ta = []

"""ta_step = int(((end - start)/step)/n)
for i in range(n):
    ta.extend(t(x[i*ta_step:(i+1)*ta_step], y[i*ta_step:(i+1)*ta_step], ta_step))
#plt.plot(x[0:len(ta)], ta)
"""
plt.plot(x[0:len(dx)], dx)

res = py[len(py)-1] - py[0]
print("Integral = " + str(res))
plt.show()
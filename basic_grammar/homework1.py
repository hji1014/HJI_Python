import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math

#################################### 실습 1 ####################################
# x 범위 : -10000 ~ 10000
a = 1
p , q = 1, 1

x1 = np.arange(-10000, 10000)
y1 = a * ((x1 - p)**2) + q

# 최소값
min = np.min(y1)
print( '최소값은 : ', min)

# 순간변화율 (x=c 에서의 순간변화율)
c = 100

x, y = sp.symbols('x y')
y = a * ((x-p)**2) + q
yp = sp.diff(y)
answer1 = yp.subs(x, c)
print('X의 미분식은 : ', yp)
print('X = c에서의 미분값은 : ', answer1)

plt.plot(x1, y1)
plt.show()
plt.grid(True)


#################################### 실습 2 ####################################

x2 = np.arange(-0.1, 1.1, 0.001)
y2 = -np.log2(x2)
y3 = -np.log2(1-x2)

plt.plot(x2, y2)
plt.plot(x2, y3)
plt.show()
plt.grid(True)

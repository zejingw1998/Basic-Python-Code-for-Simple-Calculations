import numpy as np
import matplotlib.pyplot as plt
from math import pi, cos

def abs_approx(x, N):
    s = 0
    for k in range(1, N + 1):   # 从 1 到 N
        s += cos((2*k - 1)*x) / (2*k - 1)**2
    f = pi/2 - (4/pi)*s
    return f


x = np.linspace(-pi, pi, 400)

y_exact = np.abs(x)


plt.plot(x, y_exact, 'k', label='|x| (exact)')
for N in [1, 2, 3, 4]:
    y_approx = [abs_approx(xi, N) for xi in x]
    plt.plot(x, y_approx, label=f'N={N}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Approximation of |x| using Fourier series')
plt.legend()
plt.grid(True)
plt.show()
    
  
    
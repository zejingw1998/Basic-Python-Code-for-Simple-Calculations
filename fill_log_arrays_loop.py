import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.0, 10.0, 101)
y = np.log(x)   

for i in range(0, len(x), 20): 
    print(f"x[{i}] = {x[i]:.3f}, y[{i}] = {y[i]:.3f}")


plt.plot(x, y, label='y = ln(x)')
plt.xlabel('x')
plt.ylabel('ln(x)')
plt.title('Plot of ln(x) for x in [1, 10]')
plt.legend()
plt.show()

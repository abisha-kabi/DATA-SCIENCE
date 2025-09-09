import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('test.txt')
x = data[:, 0]
y = data[:, 1]
plt.plot(x, y, color='blue', marker='o', linestyle='-')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Graph from test.txt')
plt.grid(True)
plt.show()

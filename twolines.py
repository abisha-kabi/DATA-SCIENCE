import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y1=x
y2=x**2
y3=np.sin(x)
plt.plot(x,y1,label='y=x',color='blue',linestyle='-')
plt.plot(x,y2,label='y=x^2',color='red',linestyle='--')
plt.plot(x,y3,label='y=sin(x)',color='green',linestyle=':')
plt.xlabel('x-axis')
plt.xlabel('y-axis')
plt.xlabel('multiple lines on same plot')
plt.legend()
plt.grid(True)
plt.show()

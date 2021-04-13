#practice

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5 , 5 , 100)
y = 2*x + 1

plt.plot(x , y , '-r' , label= 'y = 2x+1')
plt.title('Graph of y=2x+1')
plt.xlabel('X' , color = 'r')
plt.ylabel('Y', color='r')
plt.legend(loc='upper right')
plt.grid()
plt.show()
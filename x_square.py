import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(-10,10,0.1)

for i in x:
	y = x*x


plt.plot(x,y)
plt.show()
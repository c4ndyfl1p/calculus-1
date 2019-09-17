import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10,1)
for i in x:
	y = 1/x

plt.plot(x,y)
plt.show()

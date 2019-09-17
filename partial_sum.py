import numpy as np 

x = np.arange(1,6,1)
print("x: ", x)
#d = [1,1,1,1,1]
#a = [1,1,1,1,1]

n = np.arange(1, len(x) + 1, 1)
print("n(no. of terms):" , n)

for i in np.nditer(n):
#   y = n/2  * (2a+(n-1)*d)
	y = (i/2)*((2*1)+(i - 1)*1)
	#y = np.array(y,  dtype=np.float64)
	print("i:", i, "y:", y)

	#y = np.array(((i/2)*((2*1)+(i - 1)*1)), dtype=np.float64)
	
	
	

print("y: ", y)

print(type(y))
print(type(x))
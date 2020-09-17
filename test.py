import numpy as np
  
a = np.array([3, 1, 2, 0])
b = np.argsort(a)
print(b)
print(a[b])
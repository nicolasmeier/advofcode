import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

t1 = np.arange(0, 8, 0.5)
mask_start = len(t1)
t2 = np.arange(10, 14, 0.5)
t = np.concatenate([t1, t2])
c = t*2 # np.cos(t)     # an aside, but it's better to use numpy ufuncs than list comps

mc = ma.array(c)
mc[mask_start] = ma.masked
print(mc)
plt.figure()
plt.plot(t, mc)
plt.title('Using masked arrays')

plt.show()
import numpy as np
import numpy.ma as ma

l = range(1000)
# %timeit [i**2 for i in l]
n = np.arange(1000)
# %timeit [j**2 for j in n]
#L1 = range(1000)
# The execution time when using numpy library is around 20 times faster.

a = np.array([0,1,2,3])
print(".ndim of ([0,1,2,3]) : \n", a.ndim)
print("\n .shape of ([0,1,2,3]) : \n",a.shape)

a = np.array([(0,1,2,3),(7,8,9,4)])
print("\n.ndim of ([(0,1,2,3),(7,8,9,4)]) : \n", a.ndim)
print("\n.shape of ([(0,1,2,3),(7,8,9,4)]) : \n",a.shape)

a = np.array([(0,1,2,3),(7,8,9,4),(8,7,6,5)])
print("\n.ndim of ([(0,1,2,3),(7,8,9,4),(8,7,6,5)]) : \n",a.ndim)
print("\n.shape of ([(0,1,2,3),(7,8,9,4),(8,7,6,5)]) : \n",a.shape)

a = np.linspace(0,1,6)
print("\n.linspace(0,1,6) : ",a)

a=np.ones((3,3))
print("\n.ones((3,3)) \n",a)

print("\n.eye(3) : \n",np.eye(3))

a = np.diag([1,2,3,4,5])
print("\n.diag([1,2,3,4,5]) : \n",a)

a= np.array([1,2,3,4])
print("\nSlicing a[1:] : ",a[1:])

x = np.array([1, 2, 3, -1, 5])
mx = ma.masked_array(x, mask=[0, 0, 0, 1, 0])
print("\nUsing numpy.ma to mask the 4th element of array \nma.masked_array(x, mask=[0, 0, 0, 1, 0]) : ")
print("Array : ",x)
print("Masked array : ",mx)
print("Mean of array : ",x.mean())
print("Mean of masked array : ",mx.mean())
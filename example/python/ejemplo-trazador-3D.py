import scipy
from scipy import interpolate
import numpy as np

# K = Degree of the spline. Cubic splines are recommended. Even values of k should be avoided especially with a small s-value. 1 <= k <= 5, default is 3.
data=np.array([[1, 2, 3], [2, 1, 2], [4, 2, 6], [6, 3, 4]]) # m > k must hold
data = data.transpose() # we need to transpose to get the data in the right format (matriz transpuesta)

#now we get all the knots and info about the interpolated spline
tck, u= interpolate.splprep(data) #Find the B-spline representation of an N-dimensional curve.
#here we generate the new interpolated dataset, 


x = np.linspace(0,1,10) 

# Given the knots and coefficients of a B-spline representation, evaluate the value 
# of the smoothing polynomial and its derivatives. This is a wrapper around the FORTRAN
# routines splev and splder of FITPACK.
new = interpolate.splev(x, tck)

for i in range (len(x)):
    xi = new[0]
    yi = new[1]
    zi = new[2]
    print '(x, y, z) = ('+str(xi[i])+', '+str(yi[i])+', '+str(zi[i])+')'


#now lets plot it!
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(data[0], data[1], data[2], label='originalpoints', lw =2, c='Dodgerblue')
ax.plot(new[0], new[1], new[2], label='fit', lw =2, c='red')
ax.legend()

plt.show()

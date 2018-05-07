# -*- coding: utf-8 -*-

#----------------------------------------------------------------------
# Name:         3D Cartesian space path generator.py
# Propouse:     To do a script to interpolate a given set of points with splines in 3D space 
#
# Autor:        Raúl de Santos Rico
#
# Creation:     25/05/2018
#
# Licencia:        GPL
#----------------------------------------------------------------------

import scipy
from scipy import interpolate
import numpy as np

print("--------------------------------------------")
print("Cartesian Control Path Generator space path generator 1.0")
print("--------------------------------------------")

print("indicate the total number of points which you want to pass through: ")
points = input()

# zeros function for three-dimensional matrix
matrix = np.zeros((points, 3))

# three-dimensional matrix 
for i in range(points):
    print('indicate coordinates (x,y,z) of the point: '+str(i))
    for j in range(3):
        if j == 0: 
            print('x: ')            
        elif j == 1:
            print('y: ')
        else:
            print('z: ')
        matrix[i][j] = input()

print('----------')  
print('Resulting matrix:')
print(matrix)
        
# data=np.array([[1, 2, 3], [2, 1, 2], [4, 2, 6], [6, 3, 4], [3, 7, 0], [8, 9, 4]]) # array de puntos: m > k must hold

data = matrix.transpose() # we need to transpose to get the data in the right format 

print('----------')  
print('Transposed matrix:')
print(data)

print("-------------------------------------------")   
print("Indicate the degree of the spline (1 <= k <= 5) default is 3")
k = input()  

print("-------------------------------------------")   
print("Indicate number of interpolation points (resolution) : ")
res = input() 


# Now we get all the knots and info about the interpolated spline
# - data: [x, y, z]
# - k: Degree of the spline. Cubic splines are recommended. Even values of k should be avoided especially with a small s-value. 1 <= k <= 5, default is 3.
# - tck (tuple) (t,c,k):    * containing the vector of knots
#                           * the B-spline coefficients
#                           * the degree of the spline
# - u: An array of the values of the parameter.
tck, u= interpolate.splprep(data, k=k) #Find the B-spline representation of an N-dimensional curve.

# resolution: evaluate the spline fits for 10 evenly spaced distance values
# res = 10

# An array of points at which to return the value of the smoothed spline or its derivatives. 
x = np.linspace(0,1,res) 

# Here we generate the new interpolated dataset:
# Given the knots and coefficients of a B-spline representation, evaluate the value 
# of the smoothing polynomial and its derivatives. This is a wrapper around the FORTRAN
# routines splev and splder of FITPACK.
new = interpolate.splev(x, tck)

#now lets plot it!
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig)

print("-------------------------------------------")
print("Points resulting from the trajectory: ")
# Print the point values 
for i in range (len(x)):
    xi = new[0]
    yi = new[1]
    zi = new[2]
    print '(x, y, z) = ('+str(xi[i])+', '+str(yi[i])+', '+str(zi[i])+')'
    # Drawing the points
    plt.plot(xi, yi, zi, 'o')

print("-------------------------------------------")

plt.plot(data[0], data[1], data[2], label='original points', lw =2, c='blue')
plt.plot(new[0], new[1], new[2], label='interpolated points', lw =2, c='red')
plt.legend()
plt.show()

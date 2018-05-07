#! /usr/bin/env python

import yarp
import kinematics_dynamics

import scipy
from scipy import interpolate
import numpy as np


yarp.Network.init()

print("--------------------------------------------")
print("Cartesian Control Path Generator 1.0")
print("--------------------------------------------")

# Configurating YARP network

if yarp.Network.checkNetwork() != True:
    print '[error] Please try running yarp server'
    raise SystemExit

options = yarp.Property()
options.put('device','CartesianControlClient')
options.put('cartesianRemote','/teoSim/rightArm/CartesianControl')
options.put('cartesianLocal','/cartesianControlExample')
options.put('transform', 1)
dd = yarp.PolyDriver(options)  # calls open -> connects

if not dd.isValid():
    print 'Cannot open the device!'
    raise SystemExit
    
# Configuring 3D path generator
    
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

# Cartesian control code:
cartesianControl = kinematics_dynamics.viewICartesianControl(dd)  # view the actual interface

print '> stat'
xv = yarp.DVector()
stat = cartesianControl.stat(xv)
print '<',yarp.Vocab.decode(stat),'[%s]' % ', '.join(map(str, xv))

# making the vector position
xi = new[0] # x positions
yi = new[1] # y positions
zi = new[2] # z positions

# empty vector
xd = []

xd.append([0.389496, -0.34692, 0.16769, 1.0, 0.0, 0.0, 0.0] ) # initial pose

#xd[0] = [0.389496, -0.34692, 0.16769, 1.0, 0.0, 0.0, 0.0] # initial pose
#xd[1] = [0.5, -0.34692, 0.16769, 1.0, 0.0, 0.0, 0.0]
#xd[2] = [0.5, -0.4, 0.16769, 1.0, 0.0, 0.0, 0.0]
#xd[3] = [0.5, -0.4, 0.16769, 0.0, 1.0, 0.0, -12.0]
#xd[4] = [0.5, -0.4, 0.16769, 1.0, 0.0, 0.0, -50.0]
#xd[5] = [0.389496, -0.34692, 0.16769, 1.0, 0.0, 0.0, 0.0]
#xd[6] = [0.0, -0.34692, -0.221806, 0.0, 1.0, 0.0, 90.0]

print("-------------------------------------------")
print("Points resulting from the trajectory: ")

# Print the point values 

for i in range (len(x)):
    xd.append([(0.389496+xi[i]), (-0.34692+yi[i]), (0.16769+zi[i]), 1.0, 0.0, 0.0, 0.0])
    
    
for i in range (len(xd)):
    print(xd[i])
    
print("-------------------------------------------")

for i in range(len(xd)):
    print '-- movement '+str(i+1)+':'
    print '> inv [%s]' % ', '.join(map(str, xd[i]))
    xd_vector = yarp.DVector(xd[i])
    qd_vector = yarp.DVector()
    if cartesianControl.inv(xd_vector,qd_vector):
        print '< [%s]' % ', '.join(map(str, qd_vector))
    else:
        print '< [fail]'
        continue
    
    print '> movj [%s]' % ', '.join(map(str, xd[i]))
    xd_vector = yarp.DVector(xd[i])
    if cartesianControl.movj(xd_vector):
        print '< [ok]'
        print '< [wait...]'
        cartesianControl.wait()
    else:
        print '< [fail]'
    

print 'bye!'

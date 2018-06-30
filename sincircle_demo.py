from sincircle import sin_circle, make_xy_list
import numpy as np
import matplotlib.pyplot as plt


r_max=1
modulation=0.05
period= (2*np.pi/50) # period of sin in radians
N=10000 #number of points

def polar_curve(fi):
    return sin_circle(fi, r_max, modulation, period)
    
list_of_points= make_xy_list(polar_curve, N)

x=[]
y=[]
for point in list_of_points:
  x.append(point[0])
  y.append(point[1])
  
plt.plot(x,y)
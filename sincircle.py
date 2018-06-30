import numpy as np
import matplotlib.pyplot as plt

# Generating circle modulated by sin

#Curve parameters
r_max=0.9 # maximal distance from (0,0) point to the curve (between 0 and 1)
modulation=0.05 # amplitude of sin to the average radius of the circle ratio (between 0 and 1)
period= (2*np.pi)/200 # period of sin in radians

number_of_points=10000 # how many points are used in curve approximation

# target curve in polar coordinates

def sin_circle(r_max, modulation, period, fi):
  
    #returns r for the specific angle (fi)
    #r_max, modulation, period- parameters of the curve
    
    r_0 = r_max/(1 + modulation) #average radius
    a = r_0*modulation #amplitude of sin
    freq = (2*np.pi)/period
    
    return r_0 * (1 + a*np.sin(freq*fi))
    
def polar_curve(fi):
    return sin_circle(r_max, modulation, period, fi)
  
def make_xy_list( polar_curve, number_of_points):
    points_xy=[]
    for fi in np.linspace(0, 2*np.pi, number_of_points):
        x , y = polar_curve(fi)*np.cos(fi), polar_curve(fi)*np.sin(fi)
        points_xy.append((x,y))
        
    return points_xy
    

points_xy = make_xy_list(polar_curve, number_of_points)   
    
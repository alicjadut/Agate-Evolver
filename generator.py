import numpy as np
import matplotlib.pyplot as plt

# Generating circle modulated by sin

#Curve parameters
r_max=1 # maximal distance from (0,0) point to the curve (between 0 and 1)
modulation=0.05 # amplitude of sin to the average radius of the circle ratio (between 0 and 1)
period= (2*np.pi)/50 # period of sin in radians

number_of_points=10000 # how many points are used in curve approximation

# target curve in polar coordinates
def sin_circle(fi, r_max=r_max, modulation=modulation, period=period):
  
    #returns r for the specific angle (fi)
    #r_max, modulation, period- parameters of the curve
    
    r_0 = r_max/(1 + modulation) #average radius
    a = r_0*modulation #amplitude of sin
    freq = (2*np.pi)/period
    
    return r_0 * (1 + a*np.sin(freq*fi))
 
def make_xy_list( function=sin_circle, number_of_points=number_of_points):
    points_xy=[]
    for fi in np.linspace(0, 2*np.pi, number_of_points):
        x , y = function(fi)*np.cos(fi), function(fi)*np.sin(fi)
        points_xy.append((x,y))
        
    return points_xy

def polar_curve(modulation = 0.3, freq = 2/3):
    r_0 = 1/(1 + modulation) #average radius
    a = r_0*modulation #amplitude of sin
    f = lambda fi : r_0 * (1 + a*np.sin((freq*fi)**2))
    return make_xy_list(f,1000)
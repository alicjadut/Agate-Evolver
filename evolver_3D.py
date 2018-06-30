#3D- evolver

from shapely.geometry import Polygon, MultiPolygon
import matplotlib.pyplot as plt
from numpy.random import choice



def make_polygon_list(layer_3D):
  
    #transform list of lists of points to list of Multipolygons
    polygons=[]
    for cross in layer_3D:
        polygons.append(MultiPolygon([Polygon(cross)]))
    return polygons
        
        
def make_new_layer_3D(old_layer, layer_width=0.1, l_distance=0.02):
  
    #l_distance- distance between crossections
    #old_layer- list of polygons
    #returns list of polygons
    #layer_width- layer growth in one step
    #returns list of polygons
    
    dist_max=int(np.floor(layer_width/l_distance)) # how many crossections are in the range of one layer
    zsize=len(old_layer) #how many xy layers
    new_layer=[] #list of polygons
    for i in range(zsize):
        crossection=old_layer[i]
        
        # growth of the actual layer
        cross_new=crossection.buffer(-layer_width)
        
        #now adding contribution from other layers
        
        lower_bound=max(0, i-dist_max)
        upper_bound=min(zsize, i+dist_max+1)
        
        #only layers between lower_bound and upper_bound contribute
        for j in range(lower_bound, upper_bound):
            dist = abs((j-i)*l_distance) #distance between i and j layer
            new_width_sq=layer_width**2- dist**2 #effective width of contribution of j layer
            if(new_width_sq>0):
                lj_contribution=old_layer[j].buffer(-np.sqrt(new_width_sq)) # contribution of j layer to i layer
                cross_new=cross_new.intersection(lj_contribution)
        new_layer.append(cross_new)
        
    return new_layer
  
def make_N_layers_3D(first_layer, layer_width=0.1, l_distance=0.02, N=8):

    #makes N layers in 3D
    #first_layer- list of polygons, initial layer
    #layer_width, l_distance- like in make_new_layer_3D
    #returns list of created layers
    
    layers_list = []
    layer = first_layer
    
    for i in range(N):
        layers_list.append(layer)
        layer=make_new_layer_3D(layer, layer_width, l_distance)
        
        
    return(layers_list)

def draw_crossection(layers_list, z):
  
    # draws crossection of list of 3D layers
    # z- number of layer to be drawn
    
    colours=['brown','lightblue','khaki','gold','lavender','tan','wheat','white','darkgray','beige','ivory']
    
    for layer in layers_list:
        mpolygon = layer[z]
        if(mpolygon.__class__.__name__=='Polygon'):
            mpolygon = MultiPolygon([mpolygon])
        for polygon in mpolygon: # z crossection

            x,y = polygon.exterior.xy
            plt.plot(x, y, choice(colours, 1)[0])
            plt.fill(x, y, choice(colours,1)[0])

from shapely.geometry import Polygon,MultiPolygon
import matplotlib.pyplot as plt
from numpy.random import choice

colours=['brown','lightblue','khaki','gold','lavender','tan','wheat','white','darkgray','beige','ivory']

#first_layer = list of points in a start layer[(x1,y1),..]
#N_apexes = number of apexes of polygons aproximating layers; by default same as number of poinst in the first_layer
#min_area: the evolution stops when the area inside the layer is smaller than min_area
def evolve_agat(first_layer, custom_plot=plt, N_apexes=-1,layer_width=0.05,min_area=0.001):
    if(N_apexes==-1): N_apexes=len(first_layer)
    fig = custom_plot.figure(1, figsize=(5,5), dpi=90)
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    ax.set_title('Agate')
    layer=MultiPolygon([Polygon(first_layer)])
    while(layer.area>min_area):
        for polygon in layer:
            x,y=polygon.exterior.xy
            ax.plot(x,y,choice(colours,1)[0])
            ax.fill(x,y,choice(colours,1)[0])
        layer=layer.buffer(-layer_width,N_apexes)
        if(layer.__class__.__name__=='Polygon'):
            layer=MultiPolygon([layer])

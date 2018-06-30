from shapely.geometry import Polygon,MultiPolygon
import matplotlib.pyplot as plt

#first_layer = list of points in a start layer[(x1,y1),..]
#N_apexes = number of apexes of polygons aproximating layers; by default same as number of poinst in the first_layer
#min_area: the evolution stops when the area inside the layer is smaller than min_area

def evolve_agat(first_layer, N_apexes=-1,layer_width=0.05,min_area=0.001):
    if(N_apexes==-1): N_apexes=len(first_layer)
    layer=MultiPolygon([Polygon(first_layer)])
    while(layer.area>min_area):
        for polygon in layer:
            x,y=polygon.exterior.xy
            plt.plot(x,y)
        layer=layer.buffer(-layer_width,N_apexes)


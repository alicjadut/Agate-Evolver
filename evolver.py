
# coding: utf-8

# In[5]:


from shapely.geometry import Polygon
import matplotlib.pyplot as plt


# In[42]:


def evolve_agat(first_layer, N_apexes=-1,layer_width=0.05,min_area=0.001):
    if(N_apexes==-1): N_apexes=len(first_layer)
    layer=Polygon(first_layer)
    while(layer.area>min_area):
        x,y=layer.exterior.xy
        plt.plot(x,y)
        layer=layer.buffer(-layer_width,N_apexes)


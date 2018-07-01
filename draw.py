from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

from evolver import evolve_agat

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

marked_points = []
cid = None

layer_width = 0.005
min_area = 0.001

image_loaded = False

def agate_init(axis):
    axis.cla()
    axis.autoscale(enable=False)
    axis.set_aspect(1)
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)
    global marked_points
    marked_points = []

root = Tk.Tk()
root.wm_title("Agate evolver")

f = Figure(figsize=(10, 10), dpi=90)
a = f.add_subplot(111)

agate_init(a)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()

def on_drag(event):
    if event.xdata is not None and event.ydata is not None:
        a = event.canvas.figure.axes[0]
        a.plot(event.xdata, event.ydata, 'ro')
        marked_points.append((event.xdata, event.ydata))
        event.canvas.draw()

def on_press(event):
    if event.button == 1:
        global image_loaded
        if not image_loaded:
            agate_init(a)
        image_loaded = False
        global cid
        cid = event.canvas.mpl_connect('motion_notify_event', on_drag)

def on_release(event):
    if event.button == 1:
        event.canvas.mpl_disconnect(cid)
        if len(marked_points) >= 3:
            evolve_agat(marked_points, fig=event.canvas.figure, layer_width=layer_width, min_area=min_area)
            event.canvas.draw()

canvas.mpl_connect('button_press_event', on_press)
canvas.mpl_connect('button_release_event', on_release)

frm = Tk.Frame(master=root, height=100)
frm_file = Tk.Frame(master=frm)
frm_load = Tk.Frame(master=frm_file)
frm_save = Tk.Frame(master=frm_file)
frm_params = Tk.Frame(master=frm)

txt_load = Tk.Text(master=frm_load, height=1, width=40)

def load_image():
    agate_init(a)
    name = txt_load.get("1.0", Tk.END)[:-1]
    if len(name) > 0:
        if name[-4:] != ".png":
            name += ".png"
        try:
            img = mpimg.imread(name)
            global image_loaded
            image_loaded = True
            hsize,vsize=np.shape(img)[0:2]
            aspect=hsize/vsize
            if(aspect<1):
                a.imshow(img, extent=[0, 1, 0, aspect])
            else:
                a.imshow(img,extent=[0,1 / aspect,0,1])
            canvas.draw()
        except (ValueError, FileNotFoundError):
            pass


txt_save = Tk.Text(master=frm_save, height=1, width=40)

def save_image():
    try:
        a.axis('off')
        name = txt_save.get("1.0", Tk.END)[:-1]
        if name[-4:] != ".png":
            name += ".png"
        f.savefig(fname=name, transparent=True)
        im = Image.open(name).convert('P')
        box = im.getbbox()
        if box is not None:
            im2 = im.crop(im.getbbox())
            im2.save(name)
    except ValueError:
        pass
    a.axis('on')

frm_layer_width = Tk.Frame(master=frm_params)
frm_min_area = Tk.Frame(master=frm_params)
txt_layer_width = Tk.Text(master=frm_layer_width, height=1, width=10)
txt_min_area = Tk.Text(master=frm_min_area, height=1, width=10)

def set_param(param):
    if param == "layer_width":
        try:
            global layer_width
            layer_width = float(txt_layer_width.get("1.0", Tk.END)[:-1])
        except ValueError:
            pass
    elif param == "min_area":
        try:
            global min_area
            min_area = float(txt_min_area.get("1.0", Tk.END)[:-1])
        except ValueError:
            pass

btn_load = Tk.Button(master=frm_load, text="Load image", command=load_image)
btn_save = Tk.Button(master=frm_save, text="Save image", command=save_image)
btn_layer_width = Tk.Button(master=frm_layer_width, text="Set layer width", command=lambda: set_param("layer_width"))
btn_min_area = Tk.Button(master=frm_min_area, text="Set min area", command=lambda: set_param("min_area"))

canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
frm.place(anchor=Tk.S, relx=0.5, rely=1)
frm_file.pack(side=Tk.TOP, expand=1)
frm_params.pack(side=Tk.BOTTOM, expand=1)
frm_load.pack(side=Tk.LEFT, expand=1)
frm_save.pack(side=Tk.RIGHT, expand=1)
txt_load.pack(side=Tk.LEFT, expand=1)
btn_load.pack(side=Tk.RIGHT, expand=1)
txt_save.pack(side=Tk.LEFT, expand=1)
btn_save.pack(side=Tk.RIGHT, expand=1)
frm_layer_width.pack(expand=1)
frm_min_area.pack(expand=1)
txt_layer_width.pack(side=Tk.LEFT, expand=1)
btn_layer_width.pack(side=Tk.RIGHT, expand=1)
txt_min_area.pack(side=Tk.LEFT, expand=1)
btn_min_area.pack(side=Tk.RIGHT, expand=1)

def check_enter(event, button):
    if event.keysym == 'Return':
        button.invoke()
        return 'break'

txt_load.bind('<Key>', lambda event: check_enter(event, btn_load))
txt_save.bind('<Key>', lambda event: check_enter(event, btn_save))
txt_layer_width.bind('<Key>', lambda event: check_enter(event, btn_layer_width))
txt_min_area.bind('<Key>', lambda event: check_enter(event, btn_min_area))

Tk.mainloop()

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.image as mpimg

from evolver import evolve_agat

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

marked_points = []
cid = None

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
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

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
            evolve_agat(marked_points, fig=event.canvas.figure, layer_width=0.005)
            event.canvas.draw()

canvas.mpl_connect('button_press_event', on_press)
canvas.mpl_connect('button_release_event', on_release)

frm = Tk.Frame(master=root)
frm_load=Tk.Frame(master=frm)
frm_save=Tk.Frame(master=frm)

txt_load = Tk.Text(master=frm_load, height=1, width=50)

def load_image():
    agate_init(a)
    name = txt_load.get("1.0", Tk.END)[:-1]
    try:
        img = mpimg.imread(txt_load.get("1.0", Tk.END)[:-1])
        global image_loaded
        image_loaded = True
        a.imshow(img, extent=[0, 1, 0, 1])
        canvas.draw()
    except (ValueError, FileNotFoundError):
        pass
    global image_loaded
    image_loaded = True
    hsize,vsize,qqqq=np.shape(img)
    aspect=hsize/vsize
    if(aspect<1): a.imshow(img, extent=[0, 1, 0, aspect])
    else: a.imshow(img,extent[0,aspect,0,1])
    canvas.draw()

txt_save = Tk.Text(master=frm_save, height=1, width=50)

def save_image():
    try:
        f.savefig(fname=txt_save.get("1.0", Tk.END)[:-1], transparent=True)
    except ValueError:
        pass

btn_load = Tk.Button(master=frm_load, text="Load image", command=load_image)

btn_save = Tk.Button(master=frm_save, text="Save image", command=save_image)

frm.pack(side=Tk.BOTTOM)
frm_load.pack(side=Tk.LEFT)
frm_save.pack(side=Tk.RIGHT)
txt_load.pack(side=Tk.LEFT)
btn_load.pack(side=Tk.RIGHT)
txt_save.pack(side=Tk.LEFT)
btn_save.pack(side=Tk.RIGHT)

Tk.mainloop()

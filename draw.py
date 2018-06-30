from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from evolver import evolve_agat

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

marked_points = []
cid = None

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

f = Figure(figsize=(15, 15), dpi=90)
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
        agate_init(a)
        global cid
        cid = canvas.mpl_connect('motion_notify_event', on_drag)

def on_release(event):
    if event.button == 1:
        canvas.mpl_disconnect(cid)
        if len(marked_points) >= 3:
            evolve_agat(marked_points, fig=event.canvas.figure, layer_width=0.005)
            event.canvas.draw()

canvas.mpl_connect('button_press_event', on_press)
canvas.mpl_connect('button_release_event', on_release)

def _quit():
    root.quit()
    root.destroy()

Tk.mainloop()

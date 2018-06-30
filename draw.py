from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from evolver import evolve_agat_on

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("Embedding in TK")


f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
a.autoscale(enable=False)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

marked_points = []

def on_drag(event):
    cid = None
    a = event.canvas.figure.get_axes()[0]
    a.plot(event.xdata, event.ydata, 'ro')
    marked_points.append((event.xdata, event.ydata))
    event.canvas.draw()

def on_press(event):
    if event.button == 1:
        on_drag.cid = canvas.mpl_connect('motion_notify_event', on_drag)

def on_release(event):
    if event.button == 1:
        canvas.mpl_disconnect(on_drag.cid)
        evolve_agat_on(marked_points, event.canvas.figure.get_axes()[0])
        event.canvas.draw()

canvas.mpl_connect('button_press_event', on_press)
canvas.mpl_connect('button_release_event', on_release)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.

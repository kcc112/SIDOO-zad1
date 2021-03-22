import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from utils.method import Method
from variants.bisection import bisection
from variants.fibonacci import fibonacci
from utils.eval_math_fn import eval_math_fn
from utils.plot.marker import mark_unimodal_interval
from utils.is_unimodal import is_unimodal
from utils.scipy_optimize import scipy_optimize


def calculate(method):
    # get values from input
    interval_start = float(interval_s.get())
    interval_end = float(interval_e.get())
    fun = fn.get()
    eps = float(epsilon.get())
    iter_c = int(iteration_count.get())

    # calculate plot points
    arrayX = np.arange(interval_start, interval_end + 1, 0.01)
    arrayY = np.array(list(map(lambda x: eval_math_fn(fun, {'x': x}), arrayX)))

    # clear plot
    plot.cla()

    if is_unimodal(interval_start, interval_end, fun, 0.2):
        mark_unimodal_interval(plot, fun, interval_start, interval_end)

        # choose method
        if method == Method.BISECTION:
            bisection(plot, fun, eps, interval_start, interval_end, iter_c)
        elif method == Method.FIBONACCI:
            fibonacci(plot, fun, eps, interval_start, interval_end, iter_c)

        # optimize with scipy
        scipy_optimize(fun, interval_start, interval_end, eps, iter_c)

    # plotting x and y axys
    plot.plot(arrayX, arrayY)

    canvas.draw()


# GUI SETUP

# the main Tkinter window
master = tk.Tk()

# setting the title
master.title('Optymalizacja bisekcja i Fibonacci')

# dimensions of the main window
master.geometry('800x800')

# labels
fn_input_label = tk.Label(master, text='Funkcja')
epsilon_label = tk.Label(master, text='Epsilon')
beginning_of_interval = tk.Label(master, text='Początek przedziału')
end_of_interval = tk.Label(master, text='Koniec przedziału')
iter_count = tk.Label(master, text='Ilość iteracji')

# entry list
fn = tk.Entry(master)
epsilon = tk.Entry(master)
interval_s = tk.Entry(master)
interval_e = tk.Entry(master)
iteration_count = tk.Entry(master)

# place labels and entry in main window
fn_input_label.pack()
fn.pack()

epsilon_label.pack()
epsilon.pack()

beginning_of_interval.pack()
interval_s.pack()

end_of_interval.pack()
interval_e.pack()

iter_count.pack()
iteration_count.pack()

# method choice buttons
buttons = tk.Frame(master)
tk.Button(buttons, command=lambda: calculate(Method.BISECTION), height=2, width=10, text='Bisekcja').pack(
    side=tk.LEFT)
tk.Button(buttons, command=lambda: calculate(Method.FIBONACCI), height=2, width=10,
          text='Fibonacci').pack(side=tk.LEFT)
buttons.pack(pady=10)

# PLOT SETUP

# the figure that will contain the plot
fig = Figure(figsize=(5, 4), dpi=100)

# adding the subplot
plot = fig.add_subplot(111)

# creating the Tkinter canvas containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master)
canvas.draw()

# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# creating the Matplotlib toolbar
toolbar = NavigationToolbar2Tk(canvas, master)
toolbar.update()

# placing the toolbar on the Tkinter window
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# run the gui
master.mainloop()

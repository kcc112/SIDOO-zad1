import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from variants.bisection import bisection
from variants.fibonacci import fibonacci
from utils.eval_math_fn import eval_math_fn


def plot():
    # get value from input
    interval_start = int(a.get())
    interval_end = int(b.get())
    fun = fn.get()
    d = float(delta.get())
    i = int(iteration_count.get())

    # calculate plot points
    arrayX = np.arange(interval_start, interval_end, 0.02)
    arrayY = np.array(list(map(lambda x: eval_math_fn(fun, {"x": x}), arrayX)))

    # clear plot
    plot1.cla()

    # bisection
    # bisection(plot1, fun, d, interval_start, interval_end, i)

    fibonacci(plot1, fun, d, interval_start, interval_end)

    # plotting the graph 
    plot1.plot(arrayX, arrayY)

    canvas.draw()


# GUI SETUP

# the main Tkinter window 
master = tk.Tk()

# setting the title  
master.title('Bisekcja')

# dimensions of the main window 
master.geometry("700x700")

# button that displays the plot 
plot_button = tk.Button(master, command=plot, height=2, width=10, text="Rysuj")

# Labels
fn_input_label = tk.Label(master, text="Funkcja")
delta_label = tk.Label(master, text="Dokładność")
beginning_of_interval = tk.Label(master, text="Początek przedziału")
end_of_interval = tk.Label(master, text="Koniec przedziału")
iter_count = tk.Label(master, text="Ilość iteracji")

# Entry list
fn = tk.Entry(master)
delta = tk.Entry(master)
a = tk.Entry(master)
b = tk.Entry(master)
iteration_count = tk.Entry(master)

# place in main window
fn_input_label.pack()
fn.pack()

delta_label.pack()
delta.pack()

beginning_of_interval.pack()
a.pack()

end_of_interval.pack()
b.pack()

iter_count.pack()
iteration_count.pack()

plot_button.pack()

# PLOT SETUP

# the figure that will contain the plot 
fig = Figure(figsize=(5, 4), dpi=100)

# adding the subplot 
plot1 = fig.add_subplot(111)

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

import tkinter as tk
import numpy as np
from math import sin, pow, sqrt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

def f(x):
  return x ** 3 - x + 1

def bisection(fn, delta, a, b, iter_count):
  start = a
  end = b
  plot1.scatter(start, eval(fn, {"x": start, 'sin': sin, 'sqrt': sqrt, 'pow': pow }), color='blue')
  plot1.scatter(end, eval(fn, {"x": end, 'sin': sin, 'sqrt': sqrt, 'pow': pow }), color='blue')
  x = 0

  for k in range (1, iter_count):
    x = (start + end) / 2

    if abs(eval(fn, {"x": x, 'sin': sin, 'sqrt': sqrt, 'pow': pow })) <= delta:
      print((start + end) / 2) 
      break
    else:
      if eval(fn, {"x": x, 'sin': sin, 'sqrt': sqrt, 'pow': pow }) * eval(fn, {"x": start, 'sin': sin, 'sqrt': sqrt, 'pow': pow }) < 0:
        end = x
      else:
        start = x
    
    plot1.scatter(start, eval(fn, {"x": start, 'sin': sin, 'sqrt': sqrt, 'pow': pow }), color='blue')
    plot1.scatter(end, eval(fn, {"x": end, 'sin': sin, 'sqrt': sqrt, 'pow': pow }), color='blue')

  # root
  plot1.scatter(x, eval(fn, {"x": end, 'sin': sin, 'sqrt': sqrt, 'pow': pow }), color='red')


def plot():
    # get value from input
    interval_start = int(a.get())
    interval_end = int(b.get())
    fun = fn.get()
    d = float(delta.get())
    i = int(iteration_count.get())

    # calculate plot points
    arrayX = np.arange(interval_start, interval_end, 0.02)
    arrayY = np.array(list(map(lambda x: eval(fun, {"x": x, 'sin': sin, 'sqrt': sqrt, 'pow': pow }), arrayX)))

    # clear plot
    plot1.cla()

    # bisection
    bisection(fun, d, interval_start, interval_end, i)
    
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
plot_button = tk.Button(master,  command = plot, height = 2, width = 10, text = "Rysuj")

# Labels
fn_input_label = tk.Label(master, text = "Funkcja")
delta_label = tk.Label(master, text = "Dokładność")
beginning_of_interval = tk.Label(master, text = "Początek przedziału")
end_of_interval = tk.Label(master, text = "Konice przedziału")
iter_count = tk.Label(master, text = "Ilość iteracji")

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
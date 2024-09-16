import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import control as ctrl
import scipy.signal as signal

class ControlSystemSimulator:
    def __init__(self,root):
        self.root = root
        self.root.title('Simulador de sistemas de control')

        ttk.Label(root,text='Coeficientes del numerador (Separados por coma)').grid(column=0,row=0)
        self.num_entry = ttk.Entry(root)
        self.num_entry.grid(column=1,row=0)

        ttk.Label(root,text='Coeficientes del denominador (Separados por coma)').grid(column=0,row=1)
        self.den_entry = ttk.Entry(root)
        self.den_entry.grid(column=1,row=1)

        self.plot_button = ttk.Button(root, text='Actualizar', command=self.update_plot)
        self.plot_button.grid(column=0,row=2,columnspan=2)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(column=0,row=3,columnspan=2)
        self.ax.set_title('Respuesta del sistema')
        self.ax.set_xlabel('Tiempo')
        self.ax.set_ylabel('Respuesta')

    def update_plot(self):
        num_str = self.num_entry.get()
        den_str = self.den_entry.get()

        try:
            num = list(map(float, num_str.split(',')))
            den = list(map(float, den_str.split(',')))

            system = ctrl.TransferFunction(num,den)
            t,y = ctrl.step_response(system)

            self.ax.clear()
            self.ax.plot(t,y)
            self.ax.set_title('Respuesta al escalon unitario')
            self.ax.set_xlabel('Tiempo')
            self.ax.set_ylabel('Respuesta')
            self.canvas.draw()
        except Exception as e:
            print(f"Error: {e}")
            self.ax.clear()
            self.ax.text(0.5,0.5, 'Error en los coeficientes', horizontalalignment = 'center', verticalalignment= 'center')
            self.canvas.draw()
if __name__ == "__main__":
    root = tk.Tk()
    app = ControlSystemSimulator(root)
    root.mainloop()

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import secundaria
import alimpiar
import lista
import diccionarios
import script
import tupla

class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Welcome to Roomba")
        self.configure(background='light grey') # Color de Fondo

        # Variables
        self.var_des = tk.StringVar(self)
        self.var_des.set('Seleccionar...')
        self.var_modo = tk.StringVar(self)
        self.var_est = tk.StringVar(self)
        

        # Caja texto
        label = tk.Label(self, bg="light grey", text='Número de zonas a limpiar:',
                         padx=30, pady=5, width=20
                         )
        label.grid(row=0, column=0)

        # Caja de Opciones
        opciones = ['0','1','2', '3', '4']
        menu = tk.OptionMenu(self, self.var_des, *opciones)
        menu.config(width=20)
        menu.grid(row = 0, column = 1, padx = 30, pady = 30)
        

        # Botones Limpiar y Simular
        boton = tk.Button(self, text="Limpiar", width=20, command=self.valores_limpiar)
        boton.grid(row=3, column=0, padx=20, pady=30)
        boton = tk.Button(self, text="OK", width=20, command=self.valores_simular)
        boton.grid(row=3, column=1, padx=20, pady=30)

    def valores_limpiar(self):
        self.var_des.set('Seleccionar...')

    def valores_simular(self):
        secundaria.VentanaSimulacion(self.parent,
                                     self.var_des.get(),
                                     self.var_modo.get(),
                                     self.var_est.get()
                                     )

if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
















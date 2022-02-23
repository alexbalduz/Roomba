import tkinter as tk


class VentanaSimulacion(tk.Toplevel):
  
    def __init__(self, parent, vent, modo, est, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Dimensiones")
        self.geometry("400x200+0+0")
        self.protocol("WM_DELETE_WINDOW", self.volver)

        tk.Button(self, text="Volver", command=self.volver).pack()
        self.parent.withdraw()

        nb = ttk.Notebook(parent)

    def volver(self):
        self.parent.deiconify()
        self.destroy()
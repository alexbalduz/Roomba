import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import alimpiar
import lista
import diccionarios
import script
import tupla

def abrirventana2():
    ventana.withdraw()
    win= tk.Toplevel()
    win.geometry('500x300')
    win.title('Dimensiones')

    # boton2=tk.Button(win,text='Calcular', command=win.destroy)
    # boton2.pack()

    lbl = tk.Label(win, text= 'Zona 1')
    lbl.pack(side=tk.TOP)
    lbl2 = tk.Label(win, text = 'Introduzca el largo y ancho(cm^2)')
    lbl2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada1 = tk.Entry(win)
    entrada1.pack()
    entrada2 = tk.Entry(win)
    entrada2.pack()

    lbl3 = tk.Label(win, text= 'Zona 2')
    lbl3.pack(side=tk.TOP)
    lbl4 = tk.Label(win, text = 'Introduzca el largo y ancho(cm^2)')
    lbl4.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada3 = tk.Entry(win)
    entrada3.pack()
    entrada4 = tk.Entry(win)
    entrada4.pack()

def cerrarventana():
    ventana.destroy()

ventana = tk.Tk()
ventana.title('Welcome to Roomba')
ventana.geometry('520x300')
label = tk.Label(text="Introduzca el número de zonas a limpiar:")
label.pack()

combo = ttk.Combobox(ventana)

combo['values']= (0, 1, 2, 3, 4)

combo.current(0) #set the selected item

combo.pack()

button =tk.Button(ventana, text = 'OK', command = abrirventana2)
button.pack()

ventana.mainloop()











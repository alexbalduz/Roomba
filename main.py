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
    win.geometry('380x300+1900+100')
    win.title('Dimensiones')
    e3=tk.Label(win, text='Bienvenido a la segunda ventana')
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    boton2=tk.Button(win,text='OK', command=win.destroy)
    boton2.pack(side=tk.TOP)

def cerrarventana():
    ventana.destroy()

ventana = tk.Tk()
ventana.title('Welcome to Roomba')
ventana.geometry('380x300')
label = tk.Label(text="Introduzca el número de zonas a limpiar:")
label.grid(column=0, row=0)

combo = ttk.Combobox(ventana)

combo['values']= (0, 1, 2, 3, 4)

combo.current(0) #set the selected item

combo.grid(column=1, row=0)

button =tk.Button(ventana, text = 'OK', command = abrirventana2)
button.grid(column=2,row=0)
ventana.mainloop()











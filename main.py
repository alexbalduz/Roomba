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

    boton2=tk.Button(win,text='Calcular', command= clicked)
    boton2.pack(side=tk.BOTTOM)

    lbl = tk.Label(win, text= 'Zona 1')
    lbl.pack()
    lbl2 = tk.Label(win, text = 'Introduzca el largo y ancho(cm^2)')
    lbl2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada1 = tk.Entry(win)
    entrada1.pack()
    entrada2 = tk.Entry(win)
    entrada2.pack()

    lbl3 = tk.Label(win, text= 'Zona 2')
    lbl3.pack()
    lbl4 = tk.Label(win, text = 'Introduzca el largo y ancho(cm^2)')
    lbl4.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada3 = tk.Entry(win)
    entrada3.pack()
    entrada4 = tk.Entry(win)
    entrada4.pack()

def cerrarventana():
    ventana.destroy()

def calculoDeLaSuperficieALimpiar(listaDeZonas):
    superficieALimpiar = 0
    for zona in listaDeZonas:
        largo = zona.get("largo")/100
        ancho = zona.get("ancho")/100
        calculo = largo*ancho
        print (str(largo)+" x "+str(ancho)+"= "+str(calculo))
        superficieALimpiar = superficieALimpiar +calculo
    return (superficieALimpiar)

parametros = ("robot_aspirador",2)

zonas = []



def tiempoLimpiezaEnMinutos(superficieALimpiar, tiempoParaUnMetroCuadrado):
    return round(superficieALimpiar*tiempoParaUnMetroCuadrado)

def clicked():
    superficieALimpiar = calculoDeLaSuperficieALimpiar(zonas)

    tiempoEstimado = tiempoLimpiezaEnMinutos(superficieALimpiar,parametros[1])

    if tiempoEstimado > 55:
        print(parametros[0]+" dice: ¡Me parece que esto va a tardar un poco!")

    messagebox.showinfo('Aviso', "La superficie total a limpiar es de "+str(superficieALimpiar)+ " m2")
    messagebox.showinfo('Aviso', "El tiempo estimado es: "+str(tiempoEstimado)+" minutos")
    messagebox.showinfo('Aviso', parametros[0]+" dice: ¡Me parece que esto va a tardar un poco!")

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









from operator import length_hint
import tkinter as tk
from tkinter import LEFT, messagebox
import tkinter.ttk as ttk
import turtle

entries = []

def abrirVentana2():
    ventana.withdraw()
    win= tk.Toplevel()
    win.geometry('500x300')
    win.title('Dimensiones')

    zonesCount = combo.get()

    boton2=tk.Button(win,text='Calcular', command=makeCalculationsForZones)
    boton2.pack(side=tk.BOTTOM)

    for zone in range(1, int(zonesCount) + 1):
        lbl = tk.Label(win, text= 'Zona ' + str(zone))
        lbl.pack()
        lbl2 = tk.Label(win, text = 'Introduzca el largo y ancho(cm^2)')
        lbl2.pack(padx=5, pady=5, ipadx=5, ipady=5)

        lengthEntry = tk.Entry(win)
        lengthEntry.pack()

        widthEntry = tk.Entry(win)
        widthEntry.pack()

        entries.append((lengthEntry, widthEntry))


def getZonesFromEntries(entries):
    zones = []
    for entry in entries:
        length = entry[0].get()
        width = entry[1].get()
        zone = { "largo": int(length), "ancho": int(width) }
        zones.append(zone)

    zonesCount = combo.get()
    t = turtle.Turtle()
    for zone in zones:
        if int(zonesCount) % 2 == 0:
            t.fd(int(length))
            t.rt(90)
            t.fd(int(width))
            t.rt(90)
            t.fd(int(length))
            t.rt(90)
            t.fd(int(width))
        else:
            t.fd(int(length))
            t.rt(90)
            t.fd(int(width))
            t.rt(90)
            t.fd(int(length))
            t.rt(90)
            t.fd(int(width))
    return zones

def cerrarVentana():
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

def tiempoLimpiezaEnMinutos(superficieALimpiar, tiempoParaUnMetroCuadrado):
    return round(superficieALimpiar*tiempoParaUnMetroCuadrado)

def makeCalculationsForZones():
    zones = getZonesFromEntries(entries)

    superficieALimpiar = calculoDeLaSuperficieALimpiar(zones)

    tiempoEstimado = tiempoLimpiezaEnMinutos(superficieALimpiar,parametros[1])

    messagebox.showinfo('Aviso', "La superficie total a limpiar es de "+str(superficieALimpiar)+ " m2")
    messagebox.showinfo('Aviso', "El tiempo estimado es: "+str(tiempoEstimado)+" minutos")

    if tiempoEstimado > 55:
        messagebox.showinfo('Aviso', parametros[0]+" dice: ¡Me parece que esto va a tardar un poco!")
    else:
        messagebox.showinfo('Aviso', parametros[0]+" dice: ¡Esto está en un periquete!")


ventana = tk.Tk()
ventana.title('Welcome to Roomba')
ventana.geometry('520x300')

label = tk.Label(text="Introduzca el número de zonas a limpiar:")
label.pack()

combo = ttk.Combobox(ventana)
combo['values']= (0, 1, 2, 3, 4)
combo.current(0) #set the selected item
combo.pack()

button =tk.Button(ventana, text = 'OK', command = abrirVentana2)
button.pack()

ventana.mainloop()
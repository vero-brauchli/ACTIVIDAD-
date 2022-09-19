#CONTADOR DECRECIENTE 

from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana = Tk()
ventana.geometry("300x200")
ventana.title ("Contador Creciente")
ventana.config(bg="pink")


def Contador():       
        contador.set(int(contador.get())-1) #para restar el contador 

#CREAMOS LA ETIQUETA CONTADOR
etiquetaCon=Label(ventana, text="Contador")
etiquetaCon.grid(row=0, column=0, sticky="w", padx=5, pady=5)

#CREAMOS ENTRY PARA VER EL CONTADOR 
contador=tk.IntVar(ventana,88)
etiquetaNum=ttk.Entry(state="readonly", textvariable=contador)
etiquetaNum.grid (row=0, column=2, padx=10)

#CREAMOS EL BOTON PARA DISMINUIR EL CONTADOR 
boton=Button(ventana, text="-", command=Contador)
boton.grid(row=0, column=3, padx=10, pady=0)

ventana.mainloop()

# CONTADOR CRECIENTE

from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana = Tk()
ventana.geometry("300x200")
ventana.title ("Contador Creciente")
ventana.config(bg="blue")

frameCont = Frame(ventana)
frameCont.place(relx= 0.5, rely=0.3, anchor=CENTER)

def Contador(): #defino funcion 
        contador.set(int(contador.get())+1) #para aumentar el numero del contador 

#CREAMOS LA ETIQUETA CONTADOR
etuqietaCont = Label(frameCont, text="Contador")
etuqietaCont.grid(row=0, column=0, sticky="w", padx=5, pady=5)

#CREAMOS ENTRY PARA VER EL CONTADOR 
contador=tk.IntVar(frameCont,1)
etiquetaNum=ttk.Entry(frameCont, state="readonly", textvariable=contador)
etiquetaNum.grid (row=0, column=2, padx=10, pady=10)

#CREAMOS EL BOTON PARA AUMENTAR EL CONTADOR 
boton=Button(frameCont, text="+", command=Contador) #llamo a funcion 
boton.grid(row=0, column=3, padx=10, pady=0)

ventana.mainloop()



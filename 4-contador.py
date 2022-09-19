from tkinter import *
from tkinter import ttk
import tkinter as tk

#Ventana principal
ventana = Tk()
ventana.geometry("600x200")
ventana.title("CONTADOR")
ventana.config(bg="beige")

frameCont = Frame(ventana)
frameCont.place(relx= 0.5, rely=0.3, anchor=CENTER)

campoNum= StringVar()
campoNum.set(0)

def Botonup(): #defino funcion 
        numero= int (campo.get())
        numero +=1
        campoNum.set(numero)

def BotonDown():
        numero= int (campo.get())
        numero -=1
        campoNum.set(numero)

def BotonReset():
    numero=0
    campoNum.set(numero)

textocont=Label(frameCont, text="Contador" ,width = 8, font= ("TkFixedFont",12))
textocont.grid(row=0,column=0, padx=10, pady=0)

campo= Entry (frameCont, state="readonly", textvariable=campoNum, width = 10, font= ("TkFixedFont",12))
campo.grid(row=0 , column=1, padx=10, pady=0)

#CREAMOS EL BOTON PARA AUMENTAR EL CONTADOR 
boton=Button(frameCont, text="Count Up", command=Botonup, width = 10, font= ("TkFixedFont",12)) #llamo a funcion 
boton.grid(row=0, column=3, padx=10, pady=0)

boton2=Button(frameCont, text="Count Down", command=BotonDown,width = 10, font= ("TkFixedFont",12))
boton2.grid(row=0, column=4, padx=10, pady=0)

boton3=Button(frameCont, text=" Reset ", command=BotonReset, width = 10, font= ("TkFixedFont",12))
boton3.grid(row=0, column=5, padx=10, pady=0)



ventana.mainloop()
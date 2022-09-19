#CALCULADORA

from __future__ import division
from tkinter import *
from tkinter import ttk
import tkinter as tk

#Ventana principal
ventana = Tk()
ventana.geometry("400x400")
ventana.title("CALCULADORA")
ventana.config(bg="beige")

#Creamos la caja contenedora widgt
frameCalcu = Frame(ventana)
frameCalcu.place(relx= 0.5, rely=0.5, anchor=CENTER)

#FUNCION PARA SUMA 
def Suma():
    numero1= int(num1.get())
    numero2= int(num2.get())
    resultado = numero1 + numero2
    resultadovar.set(resultado)

#FUNCION PARA RESTA
def Resta():
    numero1= int(num1.get())
    numero2= int(num2.get())
    resultado = numero1 - numero2
    resultadovar.set(resultado)

#FUNCION PARA MULTIPICACION
def Multiplicacion():
    numero1= int(num1.get())
    numero2= int(num2.get())
    resultado = numero1 * numero2
    resultadovar.set(resultado)

#FUNCION PARA DIVICION 
def Division():
    numero1= int(num1.get())
    numero2= int(num2.get())
    if numero2 == 0:
        mensaje="error"
        resultadovar.set(mensaje)
    else:
        resultado = numero1 / numero2
        resultadovar.set(resultado)

#FUNCION PORCENTAJE 
def Porcentaje():
    numero1= int(num1.get())
    numero2= int(num2.get())
    resultado = numero1 % numero2
    resultadovar.set(resultado) 

#FUNCION PARA RECET
def Reset():
    numero1var.set("")
    numero2var.set("")
    resultadovar.set("")

#CONVERTIR VARIABLES PARA QUE SE VEAN EN ENTRY EN VARIABLE TIPO CADENA
numero1var=StringVar ()
numero2var=StringVar ()
resultadovar=StringVar()
numero1var.set("")
numero2var.set("")
resultadovar.set("")

#CREO ESPACIO PARA SEPARAR DE EL BORDE DE LA VENTANA 

espacio= Label(frameCalcu,text="")
espacio.grid(row=0,column=0)

espacio1= Label(frameCalcu, text="  ")
espacio1.grid(row=0,column=1, padx=10, pady=0)

espacio2= Label(frameCalcu, text="  ")
espacio2.grid(row=0,column=2, padx=10, pady=0)

#ETIQUETA PARA EL PRIMER NUMERO
textnum1=Label(frameCalcu, text= "Primer Numero",font=("Cooper Black",12))
textnum1.grid (row=1,column=0, padx=10, pady=0)

#ETIQUETA PAS EL SEGUNDO NUMERO 
textnum2= Label(frameCalcu, text= "Segundo Numero",font=("Cooper Black",12))
textnum2.grid (row=2,column=0, padx=10, pady=0)

#ETIUQETA PARA EL RESULTADO 
textresultado= Label(frameCalcu, text= "Resultado", font=("Cooper Black",12))
textresultado.grid (row=3,column=0, padx=10, pady=0)

#CAJA PARA INGRESAR PRIMER NUMERO
num1= Entry (frameCalcu,width=18,borderwidth =6,relief="groove",textvariable= numero1var)
num1.grid(row=1,column=1, padx=10, pady=0)

#CAJA PARA INGRESAR SEGUNDO NUMERO 
num2= Entry (frameCalcu,width=18,borderwidth =6,relief="groove",textvariable= numero2var)
num2.grid(row=2,column=1, padx=10, pady=0)

##CAJA PARA VER RESULTADO 
resultado = Entry (frameCalcu,width=18,borderwidth =6,relief="groove",state="readonly",textvariable= resultadovar)
resultado.grid(row=3,column=1, padx=10, pady=0)

#BOTON DE SUMA
suma=Button (frameCalcu,width=8,borderwidth =6,relief="groove", bg="pink",  font= ("Cooper Black",12),text= "+", command= Suma)
suma.grid (row=4,column=0, padx=10, pady=0)

#BOTON DE RESTA
resta=Button (frameCalcu,width=8,borderwidth =6,relief="groove", bg="pink",  font= ("Cooper Black",12),text= "-", command= Resta)
resta.grid (row=4,column=1, padx=10, pady=0)

#BOTON DE MULTIPICACION
multipicacion=Button (frameCalcu,width=8,borderwidth =6,relief="groove", bg="pink",  font= ("Cooper Black",12),text= "x", command= Multiplicacion)
multipicacion.grid (row=5,column=0, padx=10, pady=0)

#BOTON DE DIVISION
division=Button (frameCalcu,width=8,borderwidth =6,relief="groove", bg="pink",  font= ("Cooper Black",12), text= "/", command= Division)
division.grid (row=5,column=1, padx=10, pady=0)

#BOTON DE PORCENTAJE 
porcentaje=Button (frameCalcu,width=8,borderwidth =6,relief="groove", bg="pink",  font= ("Cooper Black",12),text= "%", command= Porcentaje)
porcentaje.grid (row=6,column=0, padx=10, pady=0)

#BOTON DE BORRAR
reset=Button (frameCalcu,width=8,borderwidth =6,relief="groove", bg="pink",  font= ("Cooper Black",12),text= "clear", command= Reset)
reset.grid (row=6,column=1, padx=10, pady=0)

ventana.mainloop()

#ventana,width = 8, borderwidth = 3,relief="ridge",text = "n: ", font= ("TkFixedFont.",14)
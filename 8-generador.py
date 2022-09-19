# GENERADOR NUMERO ALEATORIO

from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

#Ventana principal
ventana = Tk()
ventana.geometry("400x400")
ventana.title("GENRADOR DE NUMEROS")
ventana.config(bg="brown")

#Creamos la caja contenedora widgt
framegenerar = Frame(ventana)
framegenerar.place(relx= 0.5, rely=0.5, anchor=CENTER, width=400, height=200) #width=ancho height=largo

#creamos funcion para ingesar numeros 
def Generar():
    numero1= int(num1.get())
    numero2= int(num2.get())
    if numero1==numero2: #comparamos que no sean iguales los numero 
        mensaje="error los numeros son iguales"
        resultado.set(mensaje)
    elif numero1>numero2: #cromparamos que el numero 1 no sea menor que numero 2
        mensaje= "Primer numero debe ser menor"
        resultado.set(mensaje)
    else: #generamos numero random
        generado = random.randint (numero1,numero2)
        resultado.set(generado)
        
#convertimos variable get en variable de cadena 
resultado=StringVar() 
resultado.set("")

#CREO ESPACIO PARA SEPARAR DE EL BORDE DE LA VENTANA 

espacio= Label(framegenerar,text="")
espacio.grid(row=0,column=0)

espacio1= Label(framegenerar, text="  ")
espacio1.grid(row=0,column=1, padx=10, pady=0)

espacio2= Label(framegenerar, text="  ")
espacio2.grid(row=0,column=2, padx=10, pady=0)

#creamos estiquetas 
tnumero1= Label (framegenerar, text="Primer numero",font=("Algerian",10))
tnumero1.grid(row=1,column=0)

tnumero2= Label (framegenerar, text="Segundo numero",font=("Algerian",10))
tnumero2.grid(row=2,column=0)

tgenerar= Label (framegenerar, text="Numero generado",font=("Algerian",10))
tgenerar.grid(row=3,column=0)

#cremaso cajas de numeros 
num1= Spinbox(framegenerar, from_=0,to=100,width=18,borderwidth =6,relief="ridge",font=("Algerian",10),bg="pink")
num1.grid(row=1,column=1)

num2= Spinbox(framegenerar, from_=0,to=100,width=18,borderwidth =6,relief="ridge",font=("Algerian",10),bg="pink")
num2.grid(row=2,column=1)

#creamos caja donde se ve el resultado
resgenerado=Entry(framegenerar,state="readonly", textvariable=resultado,width=30,borderwidth =6,relief="ridge",font=("Algerian",10)) 
resgenerado.grid(row=3,column=1,)

#creamos botonn
generar=Button(framegenerar,text="Generar", command=Generar,font=("Algerian",10))
generar.grid(row=4,column=1)

ventana.mainloop()








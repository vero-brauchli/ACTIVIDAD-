#CALCULADORA DOS 

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

#Ventana principal
ventana = Tk()
ventana.geometry("400x400")
ventana.title("CALCULADORA 2 ")
ventana.config(bg="brown")

#Creamos la caja contenedora widgt
framecalcu = Frame(ventana)
framecalcu.place(relx= 0.5, rely=0.5, anchor=CENTER, width=400, height=200)

#FUNCION PARA SUMA 
def Suma():
    valor1= int(val1.get())
    valor2= int(val2.get())
    resultado = valor1 + valor2
    resultadovar.set(resultado)

#FUNCION PARA RESTA
def Resta():
    valor1= int(val1.get())
    valor2= int(val2.get())
    resultado = valor1 - valor2
    resultadovar.set(resultado)

#FUNCION PARA MULTIPICACION
def Multiplicacion():
    valor1= int(val1.get())
    valor2= int(val2.get())
    resultado = valor1 * valor2
    resultadovar.set(resultado)

#FUNCION PARA DIVICION 
def Division():
    valor1= int(val1.get())
    valor2= int(val2.get())
    resultado = valor1 / valor2
    if valor2 == 0:
        mensaje="error"
        resultadovar.set(mensaje)
    else:
        resultado = valor1/ valor2
        resultadovar.set(resultado)

#FUNCION PORCENTAJE 
def Porcentaje():
    numero1= int(num1.get())
    numero2= int(num2.get())
    resultado = numero1 % numero2
    resultadovar.set(resultado) 

def Operacione():
    varFunction = int(radio.get())
    if varFunction == 1:
        Suma()
    elif varFunction == 2:
        Resta()
    elif varFunction == 3:
        Multiplicacion()
    elif varFunction == 4:
        Division()
    else:
        messagebox.showwarning("Error","Seleccione una operacion.")


#CONVERTIR VARIABLES PARA QUE SE VEAN EN ENTRY EN VARIABLE TIPO CADENA
val1=StringVar ()
val2=StringVar ()
radio=StringVar()
resultadovar=StringVar()
val1.set("")
val2.set("")

#CREO ESPACIO PARA SEPARAR DE EL BORDE DE LA VENTANA 

espacio= Label(framecalcu, text="       ")
espacio.grid(row=0,column=0)

espacio1= Label(framecalcu, text="  ")
espacio1.grid(row=0,column=1, padx=10, pady=0)

espacio2= Label(framecalcu, text="  ")
espacio2.grid(row=0,column=2, padx=10, pady=0)


#ETIQUETA PARA EL PRIMER NUMERO
textnum1=Label(framecalcu, text= "Valor 1",font=("Cooper Black",12))
textnum1.grid (row=1,column=0, padx=10, pady=0)

#ETIQUETA PAS EL SEGUNDO NUMERO 
textnum2= Label(framecalcu, text= "Valor 2",font=("Cooper Black",12))
textnum2.grid (row=2,column=0, padx=10, pady=0)

#ETIUQETA PARA EL RESULTADO 
textresultado= Label(framecalcu, text= "Resultado", font=("Cooper Black",12))
textresultado.grid (row=3,column=0, padx=10, pady=0)

textresultado= Label(framecalcu, text= "Operaciones", font=("Cooper Black",12))
textresultado.grid (row=1,column=2, padx=10, pady=0)

#CAJA PARA INGRESAR PRIMER NUMERO

num1= Entry (framecalcu,width=18,borderwidth =6,relief="groove",textvariable= val1)
num1.grid(row=1,column=1, padx=10, pady=0)

#CAJA PARA INGRESAR SEGUNDO NUMERO 
num2= Entry (framecalcu,width=18,borderwidth =6,relief="groove",textvariable= val2)
num2.grid(row=2,column=1, padx=10, pady=0)

##CAJA PARA VER RESULTADO 
resultado = Entry (framecalcu,width=18,borderwidth =6,relief="groove",state="readonly",textvariable= resultadovar)
resultado.grid(row=3,column=1, padx=10, pady=0)

#CREAMOS LOS BOTONES RADIO

radioSuma= Radiobutton(framecalcu, text="Sumar", variable=radio, value=1,font=("Algerian",10)) #variable agrupa todas las opciones 
radioSuma.grid(row=2,column=2,sticky="w", padx=5, pady=5)

radioResta= Radiobutton(framecalcu, text="Resta", variable=radio, value=2,font=("Algerian",10))
radioResta.grid(row=3,column=2,sticky="w", padx=5, pady=5)

radioMulti= Radiobutton(framecalcu, text="Multiplicacion", variable=radio, value=3,font=("Algerian",10))
radioMulti.grid(row=4,column=2,sticky="w", padx=5, pady=5)

radioDivicion= Radiobutton(framecalcu, text="Divicion", variable=radio, value=4,font=("Algerian",10))
radioDivicion.grid(row=5,column=2,sticky="w", padx=5, pady=5)

botoncalcu=Button(framecalcu,width=8,borderwidth =6,relief="groove", bg="pink",font=("Algerian",10),text= "Calcular", command = Operacione)
botoncalcu.grid (row=5,column=1, padx=10, pady=0)

ventana.mainloop()


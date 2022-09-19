#FACTORIAL 

from tkinter import *
from tkinter import ttk
import tkinter as tk
import math

ventana = Tk()
ventana.geometry("500x200")
ventana.title ("FACTORIAL")
ventana.config(bg="red")

def Factorial():      
    numF = int(numero.get())+1
    resultado.config(text= math.factorial(numF))
    for i in range(numF):
        numero.set(numF)


#etiqueta para la "n"
etiqueta = Label(ventana,width = 8, borderwidth = 3,relief="ridge",text = "n: ", font= ("TkFixedFont.",14))
etiqueta.grid(row=0,column =0,padx=7,pady=7, ipady = 10 )

#entry para "n"
numero=IntVar(value=0)                                                   
lineEdit = Entry(ventana,width=8,justify = "center", textvariable=numero, state= "readonly", font= ("TkFixedFont",14))
lineEdit.grid (row=0,column = 1, padx=7,pady=7, ipady = 10)

#etiqueta para "factorial n"
etiqueta = Label(ventana,width = 12, borderwidth = 3,relief="raised",text = " Factorial de n: ",font= ("TkFixedFont",14) )
etiqueta.grid(row=0,column =2 )

#entry para "factorial n"
resultado=Label(ventana,text="1", width = 8, font= ("TkFixedFont",12) )
resultado.grid(row=0,column=3, padx=7,pady=7, ipady = 10)

#boton
boton = Button(ventana, text = "Siguiente ", command= Factorial)
boton.grid (row=0, column=4, padx=7,pady=7, ipady = 10)

ventana.mainloop()



# relief = forma de la caja de texto
   #Falt   = plano 
   #Raised = aumento 
   #Sunken = hundido
   #Groove = ranura
   #Ridge  = cresta 
# borderwidth = anchos de los bordes 
# width = ancho 
# font  = tipo de fuente 
# state= "readonly" = solo lectura 
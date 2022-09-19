# PELICULAS 

from tkinter import *
from tkinter import ttk
import tkinter as tk

#Ventana principal
ventana = Tk()
ventana.geometry("400x400")
ventana.title("Peliculas")
ventana.config(bg="purple")

#Creamos la caja contenedora widgt
framePeli = Frame(ventana)
framePeli.place(relx= 0.5, rely=0.5, anchor=CENTER, width=400, height=300) #width=ancho height=largo

def Peliculas():
    a = peli.get()
    listaPeli.insert(END,a)
    peli.delete(0,END)

#CONVERTIR VARIABLES PARA QUE SE VEAN EN ENTRY EN VARIABLE TIPO CADENA 
peli=StringVar()
peli.set("")

#CREO ESPACIO PARA SEPARAR DE EL BORDE DE LA VENTANA 
espacio= Label(framePeli,text="")
espacio.grid(row=0,column=0)

espacio1= Label(framePeli, text="  ")
espacio1.grid(row=0,column=1, padx=10, pady=0)

espacio2= Label(framePeli, text="  ")
espacio2.grid(row=0,column=2, padx=10, pady=0)

#titulo peliculas 
tituloPeli=Label(framePeli,width=18,borderwidth =6,relief="groove",font= ("Cooper Black",10),text= "Titulo de Pelicula",bg="pink")
tituloPeli.grid(row=1, column=0, padx=10,pady=0)

#Peliculas
peliculas=Label(framePeli,width=18,borderwidth =6,relief="groove",font= ("Cooper Black",10),text="Peliculas", bg="light blue")
peliculas.grid(row=1, column=1,padx=10,pady=0)

#caja para ingesar peliculas 
peli=Entry (framePeli, textvariable=Peliculas,width=18,borderwidth =6,relief="groove")
peli.grid(row=2,column=0 ,padx=10,pady=0)

#CREAMOS LA LISTA PARA GUARDAR PELI
listaPeli=Listbox(framePeli,width=18,borderwidth =8,relief="groove")
listaPeli.grid(row=2,column=1, padx=10,pady=0)

#crear boton 
añadir=Button(framePeli,text="Añadir", width=18,borderwidth =6,relief="groove",font=("Cooper Black",10), bg="yellow",command=Peliculas)
añadir.grid(row=3,column=0, padx=10, pady=0)

ventana.mainloop()





#lita Peli = listbox para crear lista para guardar lista de pelicula 
#insert = se insertaa en la lista 
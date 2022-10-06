from site import venv
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
from tkinter import messagebox

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("700x500") #tamaño de la ventana
ventana.title ("Adivinador de número") #título que se muestra en la parte superior de la ventana
ventana.config(bg="aquamarine")
ventana.resizable(0,0)

radio = IntVar()
entryNum1 = StringVar()
entryNum2 = StringVar()
var = StringVar()
entryNum1.set("")
entryNum2.set("")

frameJuego = tkinter.Frame(ventana)
frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=400)

#Frame que aparece en primera instancia para seleccionar el idioma
frame1 = Frame(ventana)
frame1.config(bg="dodgerblue")
frame1.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=400)

etiquetaFrame1 = Label(frame1, text ="Bienvenido a Adivinando el numero que pensaste, \n\nSelecciona el idioma", font= ("Arial.",12),justify="center")
etiquetaFrame1.place(x = 100, y = 30)
etiquetaFrame1.config(bg="dodgerblue")

def boton_siguiente():
    frameJuego = tkinter.Frame(ventana, bg= "dodgerblue", bd = 10, relief="ridge")
    frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=400)
    
def Resetear():
    entryNum1.set("")
    entryNum2.set("")

def OpcioneIdioma():
    varFunction = int(radio.get())
    if varFunction == 1:
        boton_siguiente1()
    elif varFunction == 2:
        boton_siguiente2()
    else:
        messagebox.showwarning("Error","Seleccione un Idioma.")

    
botonRadioIdioma1 = Radiobutton(frame1, text="Español", variable=radio, value=1,font=("Arial.",12))
botonRadioIdioma1.place(x = 230, y = 180)
botonRadioIdioma1.config(bg="dodgerblue")

botonRadioIdioma2 = Radiobutton(frame1, text="Inglés", variable=radio, value=2,font=("Arial.",12))
botonRadioIdioma2.place(x = 230, y = 210)
botonRadioIdioma2.config(bg="dodgerblue")


if botonRadioIdioma1:
    def boton_siguiente1():
        frameJuego = tkinter.Frame(ventana, bg= "dodgerblue", bd = 10, relief="ridge")
        frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=400)
        def calculo1():
            resultado_Resta = int(entryNum1.get())
            resultado_Suma = int(entryNum2.get())
            k = ((resultado_Resta)/9)
            a = ((resultado_Suma - k )/2) 
            b = ((resultado_Suma + k )/2)   
            var=int(a), int(b)
            return messagebox.showerror("Tu numero era: ", var) 

        def validar(char): #funcion para validar datos 
            return char in "0123456789-"
        validatecommand = ventana.register(validar)
        
        etiqueta1 = Label(frameJuego, text ="Estás listo? Comencemos!", font= ("Arial.",12),justify="center")
        etiqueta1.place(x = 150, y = 15)
        etiqueta1.config(bg="dodgerblue")

        etiqueta2 = Label(frameJuego, text="1) Piensa un número de dos cifras que no sean iguales", font= ("Arial",12),justify="center")
        etiqueta2.place(x = 40, y = 50)
        etiqueta2.config(bg="dodgerblue")

        etiqueta3 = Label(frameJuego, text="2) Ahora invierte el número y coloca el resultado de la operación.\n*Si el nuevo n° es mayor, se resta el 1ro(el que pensaste) del 2do \n*Si el nuevo n° es menor, el resultado va en negativo", font= ("Arial",12),justify="center")
        etiqueta3.place(x = 40, y = 85)
        etiqueta3.config(bg="dodgerblue")

        resultado1 = Entry(frameJuego, textvariable=entryNum1) #Resultado de la resta del primer número con el segundo
        resultado1.place(x = 40, y = 155)
        resultado1.config( validate="key", validatecommand=(validatecommand, "%S" ))#validacion de datos  

        etiqueta4 = Label(frameJuego, text="3) Suma los dígitos del número que pensaste y coloca el resultado", font= ("Arial",12))
        etiqueta4.place(x = 40, y = 190)
        etiqueta4.config(bg="dodgerblue")

        resultado2 = Entry(frameJuego,  textvariable=entryNum2) #Resultado de la suma de los dígitos del número pensado
        resultado2.place(x = 40, y = 225)
        resultado2.config( validate="key", validatecommand=(validatecommand, "%S" ))
        
        resultadoBoton = Button (frameJuego, text="Resultado", command=calculo1, bd= 5) #Botón para obtener el resultado
        resultadoBoton.place(x = 40, y = 260)
        
        etiqueta5= Label(frameJuego, text= "4) El número que pensaste es: ", font= ("Arial",12))
        etiqueta5.place(x = 40, y = 295)
        etiqueta5.config(bg="dodgerblue")
        
        btn_Reset = Button (frameJuego, text="Limpiar", command=Resetear, bd = 5) #botón para limpiar los campos
        btn_Reset.place(x = 150, y = 260)
        
    btn_Siguiente = Button (ventana, text="Siguiente", command= OpcioneIdioma, bd= 7)
    btn_Siguiente.place(x = 290, y = 320)

if botonRadioIdioma2:
    def boton_siguiente2():
        frameJuego = tkinter.Frame(ventana, bg= "dodgerblue", bd = 10, relief="ridge")
        frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=400)
        def calculo2():
            resultado_Resta = int(entryNum1.get())
            resultado_Suma = int(entryNum2.get())
            k = ((resultado_Resta)/9)
            a = ((resultado_Suma - k )/2) 
            b = ((resultado_Suma + k )/2)   
            var=int(a), int(b)
            return messagebox.showerror("your number is: ", var)

        def validar(char): #funcion para validar datos 
            return char in "0123456789"
        validatecommand = ventana.register(validar) 
            
        etiqueta1 = Label(frameJuego, text ="Are you ready? Let's start!", font= ("Arial.",12),justify="center")
        etiqueta1.place(x = 150, y = 15)
        etiqueta1.config(bg="dodgerblue")

        etiqueta2 = Label(frameJuego, text="1) Think of a two-digit number that is not the same", font= ("Arial",12),justify="center")
        etiqueta2.place(x = 40, y = 50)
        etiqueta2.config(bg="dodgerblue")

        etiqueta3 = Label(frameJuego, text="2) Now reverse the number and place the result of the operation.\n*If the new n° is greater, subtract the 1st (the one you thought of) from the 2nd \n*If the new number is less, the result goes negative", font= ("Arial",12),justify="left")
        etiqueta3.place(x = 40, y = 85)
        etiqueta3.config(bg="dodgerblue")

        resultado1 = Entry(frameJuego, textvariable=entryNum1) #Resultado de la resta del primer número con el segundo
        resultado1.place(x = 40, y = 155)
        resultado1.config( validate="key", validatecommand=(validatecommand, "%S" ))#validacion de datos  

        etiqueta4 = Label(frameJuego, text="3) Add the digits of the number you thought of and put the result", font= ("Arial",12))
        etiqueta4.place(x = 40, y = 190)
        etiqueta4.config(bg="dodgerblue")

        resultado2 = Entry(frameJuego,  textvariable=entryNum2) #Resultado de la suma de los dígitos del número pensado
        resultado2.place(x = 40, y = 225)
        resultado2.config( validate="key", validatecommand=(validatecommand, "%S" ))#validacion de datos  
            
        resultadoBoton = Button (frameJuego, text="Result", command=calculo2, bd= 5) #Botón para obtener el resultado
        resultadoBoton.place(x = 40, y = 260)
            
        etiqueta5= Label(frameJuego, text= "4) The number you thought of is: ", font= ("Arial",12))
        etiqueta5.place(x = 40, y = 295)
        etiqueta5.config(bg="dodgerblue")
            
        btn_Reset = Button (frameJuego, text="Clear", command=Resetear, bd = 5) #botón para limpiar los campos
        btn_Reset.place(x = 150, y = 260)
        
    btn_Siguiente2 = Button (ventana, text="Siguiente", command= OpcioneIdioma, bd= 7)
    btn_Siguiente2.place(x = 290, y = 320)



ventana.mainloop()
"""La idea de este proyecto es crear un programa que pruebe la conectividad de sitios web.
Puedes usar los modulos urllib y tkinter para crear una interfaz gráfica de usuario (GUI) que
permita a los usuarios ingresar una dirección web. Después de haber recopilado la dirección
web del usuario, puedes pasarla a una función para devolver un código de estado HTTP para
el sitio web actual mediante la función .getcode() del módulo urllib.
En este ejemplo, simplemente determinamos si el código HTTP es 200. Si lo es, sabemos que
el sitio está funcionando; de lo contrario, informamos al usuario de que no está disponible.
"""

#Importar modulos

from tkinter import *
from urllib.request import urlopen

#Creamos las funciones

def comprobar():
    direccion_web = urlopen(input_entry.get())
    code = direccion_web.getcode()
    if code == 200:
        label2.config(text="Resultado del test de Conectividad: El sitio web está disponible")
    else:
        label2.config(text="Resultado del test de Conectividad: El sitio web no está disponible")


#Creamos la ventana

root=Tk()
root.title("Comprobador de conectividad de Sitios Web")
root.geometry("800x600")

#Creamos los botones

imagen= PhotoImage(file="testconectividad.png")
imagen_head=Label(root, image=imagen)
imagen_head.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

label1 = Label(root, text="Ingrese la URL a comprobar:", font=("Arial", 18))
label1.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

input_entry = Entry(root, width=40, font=("Arial", 24))
input_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=10)


comprobar_button = Button(root, text="Comprobar", command=comprobar)
comprobar_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

label2 = Label(root, text="Resultado:", font=("Arial", 18))
label2.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

mainloop()

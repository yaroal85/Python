import tkinter
from tkinter import*
cEncriptada=''

##Se crea una instancia de la clase tkinter y asigna un nombre a la ventana
ventana = Tk()
ventana.title("Encriptar")

##Se crea un marco para toda la ventana
marcoVentana = Frame(ventana,width=800,height=800)

## 0 - Marco para el titulo
marcoTitulo = Frame(marcoVentana)

def encriptar():
    cEncriptada=''
    clave=eClave.get()
    if len(clave) <= 5:
        print('La longitud de la contraseña no es válida')
    else:
        for i in range(len(clave)):
            nLetra = ord(clave[i])
            for x in range(len(clave)):
                nLetra+=1
                if(nLetra>=127):
                    nLetra=33
            cEncriptada += chr(nLetra)
        print ('Su apellido es: ' + cEncriptada)

    
## 0 - Instancia un Label para el título del formulario
texto = "Encriptación de clave"
fuente = ("Trebuchet MS",18)
lTitulo = Label(marcoTitulo,text=texto,font=fuente)
lTitulo.pack(side=TOP)

marcoTitulo.pack()

##1 - Marco para el apellido
marcoApellido = Frame(marcoVentana)

##1 - Instancia un Label para el apellido
texto = "Ingrese la clave: "
fuente = ("Trebuchet MS",14)
ancho = 20
lApellido = Label(marcoApellido,text=texto,font=fuente,width=ancho)
lApellido.pack(side=LEFT)

##1 - Instancia un Entry para el ingreso del apellido
fuente = ("Trebuchet MS",14)
eClave = Entry(marcoApellido,width=20,font=fuente)
eClave.pack(side=LEFT)

marcoApellido.pack()
marcoVentana.pack()

botonimprimir = Button(marcoVentana, text="Encriptar", width=20, command=encriptar)
botonimprimir.pack()


##Mostrar la ventana
ventana.mainloop()

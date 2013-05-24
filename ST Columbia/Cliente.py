##Clase Cliente

import re

class Cliente:   
        
    def __init__(self,dni,ap,nom,dom,email,tel,cantVis):
        self.dni=dni
        self.apellido=ap
        self.nombre=nom
        self.domicilio=dom
        self.email=email
        self.telefono=tel
        self.cantVisitas=cantVis

    def incrementarVisitas(self):
        self.cantVisitas+=1

    def mostrarInformacion(self):
        print("*"*50)
        print("Cliente:",self.apellido,",",self.nombre)
        print("  DNI:",self.dni)
        print("  Domicilio:",self.domicilio)
        print("  Email:",self.email)
        print("  Teléfono:",self.telefono)
        print("  Cantidad de Visitas:",self.cantVisitas)
        print("*"*50)
        print("")

    def modificarDatos(self):
        op=0
        while op!=4:
            print("")
            print("1-Domicilio")
            print("2-Email")
            print("3-Teléfono")
            print("4-No cambiar")
            op=int(input("Seleccionar opción:"))
            if op==1:
                self.domicilio=obtenerDomicilio()
            elif op==2:
                self.email=obtenerEmail()
            elif op==3:
                self.telefono=obtenerTelefono()
                

def dniValido(dni):
    if len(dni)!=8:
        print('Número de DNI no válido')
        print('Ejemplo de número válido: 34598658')
        return(False)
    elif not dni.isdigit():
        print('El número de DNI no puede contener caracteres alfanumericos')
        return(False)
    return(True)

def obtenerDomicilio():
    ##Obtiene el domicilio
    dom=str(input('Ingrese domicilio: '))
    return(dom)

def obtenerEmail():
    ##Controla que el email sea válido
    while True:
        mail=str(input('Ingrese email: '))
        if re.match("\w+@\w+\.com", mail):
            break
        else:
            print('Nombre de email no válido')
    return(mail)

def obtenerTelefono():
    ##Controla que el número de teléfono no contenga caracteres alfanumericos
    while True:
        tel=str(input('Ingrese número de teléfono: '))
        if tel.isnumeric():
            break
        else:
            print('Número de teléfono no válido')
    return(tel)

def nuevoCliente(dni,clientes):

##    ##Controla que el número de DNI sea válido
##    ##8 díigitos y numericos    
##    while True:
##        dni=str(input('Ingrese número de DNI: '))
##        if dniValido(dni)==True:
##            existe=False
##            for i in clientes:
##                if i.dni==dni:
##                    existe=True
##            if existe:
##                print("El DNI ingresado ya existe, ingrese otro")
##                continue
##            else:
##                break

    ##Controla que el apellido no contenga numeros ni caracteres especiales   
    while True:
        ap=str(input('Ingrese apellido: '))
        valido=True
        for i in ap:
            if not (ord(i)>=97 and ord(i)<=122) and not (ord(i)>=65 and ord(i)<=90) and ord(i)!=32:
                valido=False
        if valido:
            break
        else:
            print('El apellido contiene caracteres no válidos')
            continue

    ##Controla que el nombre no contenga números ni caracteres especiales 
    while True:
        nom=str(input('Ingrese nombre: '))
        valido=True
        for i in nom:
            if not (ord(i)>=97 and ord(i)<=122) and not (ord(i)>=65 and ord(i)<=90) and ord(i)!=32:
                valido=False
        if valido:
            break
        else:
            print('El nombre contiene caracteres no válidos')
            continue

    ##Obtiene el domicilio
    dom=obtenerDomicilio()

    ##Obtiene el email 
    mail=obtenerEmail()

    ##Obtiene el telefono
    tel=obtenerTelefono()

    ##Instancia un nuevo cliente
    c = Cliente(dni,ap,nom,dom,mail,tel,1)
    return(c)

def masRecurrentes(clientes):
    ##Titulo
    print("")
    print("*"*50)
    print("Clientes más recurrentes:")
    
    ##Copia del listado de clientes
    aux=[]
    for i in clientes:
        aux.append(i)

    ##Verifica que la cantidad de clientes sea superior a 5
    if len(aux)<5:
        total=len(aux)
    else:
        total=5

    ##Itera hasta que no halla clientes o hasta los 5 clientes mas recurrentes
    cant=1
    while len(aux)>0 and cant<=total:
        ##Considera el más recurrente el primero para comparar        
        mayor=aux[0].cantVisitas
        pos=0

        ##Compara el más recurrente con el resto de la lista        
        for i in range(1,len(aux)):
            if aux[i].cantVisitas>mayor:
                mayor=aux[i].cantVisitas
                pos=i

        ##Muestra el más recurrente obtenido      
        print(cant,"- Cliente:",aux[pos].dni,",visitas:",aux[pos].cantVisitas)

        ##Elimina el más recurrente de la lista        
        aux.pop(pos)
        cant+=1
    
    print("*"*50)
    print("")

def mostrarTodosLosClientes(clientes):
    for i in clientes:
        i.mostrarInformacion();

#dado un dni, devuelve un cliente, si no existe, no devuelve nada
def existeCliente(dni,clientes):
    #existe=False
    i=0
    while i<len(clientes):
        if clientes[i].dni==dni:
            #existe=True
            return(clientes[i]);
        i+=1
    #return(existe)

def modificarCliente(clientes):
    for i in clientes:
        i.mostrarInformacion()

    while True:
        dni=str(input("Ingrese DNI del Cliente:"))
        if existeCliente(dni,clientes):
            break

    pos=0
    while dni!=clientes[pos].dni:
        pos+=1

    clientes[pos].modificarDatos()


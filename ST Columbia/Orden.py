from datetime import *
from funciones import *
class Orden():
        """Clase de Orden"""
        idn=1
        def __init__(self, fechaorden, descripcion, fechaentrega):
                self.idn = Orden.idn
                Orden.idn += 1
                self.fechaorden = fechaorden
                self.descripcion = descripcion
                self.fechaentrega = fechaentrega
                self.asignada = False
                self.resultado = "Esta orden se encuentra pendiente de arreglo"
                self.costo = 0
                self.terminado = False

        def imprimirOrden(self):
                if (self.terminado == False):
                        print('/// ORDEN N', self.idn,' ///')
                        print('Fecha de Orden: ', self.fechaorden)
                        print('Descripcion de la heladera: ', self.descripcion)
                        print('Fecha de Entrega: ', self.fechaentrega)
                        print('Resultado: ', self.resultado)
                else:
                        print('/// ORDEN N', self.idn,' ///')
                        print('Fecha de Orden');
                        imprimirFechaOk(self.fechaorden);
                        print('Descripcion de la heladera: ', self.descripcion)
                        print('Fecha de Entrega')
                        imprimirFechaOk(self.fechaentrega);
                        print('Resultado: ', self.resultado)
                        print('Costo $ ', self.costo)

        def modificarOrden(self):
                op=0
                while op!=5:
                        print("")
                        print("1-Fecha de Orden")
                        print("2-Descripcion")
                        print("3-Fecha de Entrega")
                        print("4-Resultado")
                        print("5-No Cambiar");
                        op=int(input("Seleccionar opcion:"))
                        if op==1:
                                print('Ingrese la nueva fecha de orden: ')
                                while True:
                                        fechaorden=validarFecha()
                                        if(comparar(fechaorden)== "mayor"):
                                                print('La fecha es incorrecta, ingrese nuevamente')
                                        else:
                                                break;
                                self.fechaorden = fechaorden
                        elif op==2:
                                self.descripcion=str(input("Cual es el problema de la heladera? "))
                        elif op==3:
                                print("Ingrese la nueva fecha estimada de entrega: ");
                                while(True):
                                        fechaentrega = validarFecha();
                                        if(comparar(fechaentrega) != "mayor"):#no se puede dar de alta en una fecha mayor
                                                print("La fecha es Incorrecta");
                                        else:
                                                break;
                                self.fechaentrega = fechaentrega;
                        elif op ==4:
                                self.resultado=str(input("Ingrese el nuevo resultado: "))


        def asignarTecnico(self,tecnico):
                self.asignada = True
                self.tecnico = tecnico

def verificarFechaEntrega(fechaentrega):
        if(comparar(fechaentrega) == "mayor"):
                return(True)
        return(False)

def darOrden(Ordenes):
        fechaorden=datetime.now()
        descripcion=str(input('cual es el problema de la heladera?: '))
        print('Ingrese la fecha estimada de entrega: ')
        while True:
                fechaentrega=validarFecha()
                if(verificarFechaEntrega(fechaentrega)== True):
                        orden = Orden(fechaorden, descripcion, fechaentrega)
                        break
                else:
                        print('FECHA INCORRECTA!!!')
                        print('Ingrese de nuevo la fecha estimada de entrega')
        return(orden)

def seleccionarOrden(ordenes):
        op=0
        listaP=[]
        while (not op in listaP):
                print('\nOrden')
                for i in ordenes:
                        print(i.idn," ",i.descripcion)
                        listaP.append(i.idn)
                op=leerNumero("Elija una orden")
        return(existeOrden(ordenes,op))

def existeOrden(Ordenes, idn):
        for i in Ordenes:
                if(i.idn == idn):
                        return(i)


#pide los datos para modificar una orden
def modificarOrden(ordenes):
        #elegimos orden
        o = seleccionarOrden(ordenes);
        #pedimos los nuevos datos
        o.modificarOrden();
        #mostramos sus datos
        print("----------");
        o.imprimirOrden();
        print("----------");


from Tecnico import *
from Cliente import *
from Orden import *
from Heladera import *
from funciones import *

#-----------------------------------------------
def iniciarPrograma(clientes,tecnicos,ordenes,heladeras):
#cargar tecnicos
    tecnicos.append(Tecnico("Facundo","Rada",
    datetime(datetime.now().year,1,12),datetime(datetime.now().year,7,12)));
    tecnicos.append(Tecnico("Matias","Mancuello",
    datetime(datetime.now().year,2,3),datetime(datetime.now().year,8,1)));
    tecnicos.append(Tecnico("Agustin","Ramirez",
    datetime(datetime.now().year,1,15),datetime(datetime.now().year,12,11)));

#cargar clientes
    clientes.append(Cliente("12345678","Notario","Marcelo","Resistencia-1","marcelo@algo.com","252562",1));
    clientes.append(Cliente("12345677","Figueredo","Ariel","Resistencia-2","arielo@algo.com","252563",1));
    clientes.append(Cliente("12345676","Lujan","Fernando","Resistencia-3","fernando@algo.com","252564",1));
    clientes.append(Cliente("12345675","Marcos","Cortes","Resistencia-4","marcos@algo.com","252565",1));

#cargar ordenes
    ordenes.append(Orden(datetime.now(),"Hace Falso contacto",datetime(datetime.now().year,6,15)));
    ordenes.append(Orden(datetime.now(),"NO prende",datetime(datetime.now().year,7,15)));
    ordenes.append(Orden(datetime.now(),"Tiene la chapa picada",datetime(datetime.now().year,6,23)));
    ordenes.append(Orden(datetime.now(),"No funciona el freezer",datetime(datetime.now().year,7,23)));

#cargar heladeras
    heladeras.append(Heladera(ordenes[0],clientes[0],"Blanca y cuadrada"));
    heladeras.append(Heladera(ordenes[1],clientes[1],"Negra y cuadrada"));
    heladeras.append(Heladera(ordenes[2],clientes[2],"Gris y cuadrada"));
    heladeras.append(Heladera(ordenes[3],clientes[3],"No tan gris... pero cuadrada"));
#-----------------------------------------------
def asignarOrden(tecnicos,orden):
    while(True):
        t = seleccionarTecnico(tecnicos);
        if(len(t.ordenes) == 3):
            input("Este tecnico tiene asignadas demasiadas ordenes, elija otro");
        else:
            break;
    orden.asignarTecnico(t);
    t.ordenes.append(orden);

def nuevaOrden(clientes,tecnicos,ordenes):
    #primero validamos el dni
    while(True):
        dni = str(input("Escriba su DNI: "));
        if(dniValido(dni)):
            break;
        else:
            input("El DNI no es válido");
    #comprobamos que exista, sino procedemos a cargarlo
    cliente = existeCliente(dni,clientes);
    if(not cliente):
        print("El cliente no existe");
        print("Sera cargado en el sistema");
        cliente = nuevoCliente(dni,clientes);
        clientes.append(cliente);
    else:
        #si ya esta cargado, aumentamos sus visitas
        cliente.cantVisitas += 1;
    print("Cargar Orden");
    orden = darOrden(ordenes);
    descripcion = str(input("Escriba una breve descripcion de la heladera\n"));
    heladeras.append(Heladera(orden,cliente,descripcion));
    if(pregunta("¿Asignar ahora un tecnico?")):
        asignarOrden(tecnicos,orden);
    ordenes.append(orden);

def terminarReparacion(ordenes,o,heladeras):
    o.terminado = True;
    o.costo = leerNumeroReal("Ingrese el costo: ");
    o.resultado = str(input("Escriba el Resultado de la Reparacion: "));
    t = o.tecnico;
    t.desasignarOrden(o.idn);
    h = existeHeladera(heladeras,o.idn);
    h.reparada = True;


#declaramos variables
lista = [
"Nueva Orden",#1
"Nuevo Tecnico",#2
"Modificar",#3
"Asignar una Orden",#4
"Terminar Reparacion",#5
"Retiro",#6
"Listar",#7
"Salir"];#8
tecnicos = [];
ordenes = [];
clientes = [];
heladeras = [];

#iniciamos algunos datos
iniciarPrograma(clientes,tecnicos,ordenes,heladeras);

#comienza el programa
continuar = True;
while(continuar):
    opcion = menu(lista,"Menu Principal");

    #1 Nueva Orden
    if(opcion == 1):
        nuevaOrden(clientes,tecnicos,ordenes);

    #2 Nuevo Tecnico
    elif(opcion == 2):
        nuevoTecnico(tecnicos);

    #3 Modificar [clientes,tecnicos,ordenes]
    elif(opcion == 3):
        subLista = ["Cliente",
        "Tecnico",
        "Orden",
        "Volver"];
        opcion = menu(subLista,"Modificar");
        if(opcion == 1):
            print("Clientes");
            modificarCliente(clientes);
        elif(opcion == 2):
            print("Tecnicos");
            modificarTecnico(tecnicos);
        elif(opcion == 3):
            print("Ordenes");
            modificarOrden(ordenes);
        #t = seleccionarTecnico(tecnicos);
        #t.modificarDatos();

    #Asignar una Orden
    elif(opcion == 4):
        listaPosible = [];
        for i in ordenes:
            if(not i.asignada):
                listaPosible.append(i);
        if(len(listaPosible) == 0):
            input("No hay ordenes disponibles para asignar");
        else:
            o = seleccionarOrden(listaPosible);
            asignarOrden(tecnicos,o);

    #Terminar Reparacion
    elif(opcion == 5):
        listaPosible = [];
        for i in ordenes:
            #si esta asignada pero no esta terminada
            if(i.asignada and not i.terminado):
                listaPosible.append(i);
        if(len(listaPosible) == 0):
            input("No hay ordenes disponibles para terminar la reparacion");
        else:
            o = seleccionarOrden(listaPosible);
            terminarReparacion(ordenes,o,heladeras);
            
    #Retiro
    elif(opcion == 6):
        listaPosible = [];
        for i in ordenes:
            #si esta asignada pero no esta terminada
            if(i.terminado):
                listaPosible.append(i);
        if(len(listaPosible) == 0):
            input("No hay ordenes disponibles para retirar");
        else:
            orden = seleccionarOrden(listaPosible);                
            heladera = existeHeladera(heladeras,orden.idn);
            orden.imprimirOrden();
            print("--------------");
            print("Heladera:");
            heladera.verTodo();
            ordenes.remove(orden);
            heladeras.remove(heladera);

    #Listar
    elif(opcion == 7):
        subListaListar = ["Clientes","Tecnicos","Ordenes"];
        opcion = menu(subListaListar,"Listar");

        #Listar Clientes
        if(opcion == 1):
            subListaClientes = ["Mas recurrentes",
            "Todos",
            "Volver"];
            opcion = menu(subListaClientes,"Listar Clientes");
            if(opcion == 1):
                masRecurrentes(clientes);
            elif(opcion == 2):
                print("Todos los clientes");
                mostrarTodosLosClientes(clientes);
                
        #Listar Tecnicos    
        elif(opcion == 2):
            subListaTecnicos = ["Con menos de tres trabajos",
            "Totalmente ocupados",
            "Todos",
            "Volver"];
            opcion = menu(subListaTecnicos,"Listar Tecnicos");
            if(opcion == 1):
                print("Tecnicos con menos de 3 Ordenes");
                for i in tecnicos:
                    if(len(i.ordenes) < 3):
                        print("------------");
                        i.verTodo();
                        print("------------");
            elif(opcion == 2):
                print("Tecnicos con 3 Ordenes");
                for i in tecnicos:
                    if(len(i.ordenes) == 3):
                        print("------------");
                        i.verTodo();
                        print("------------");
            elif(opcion == 3):
                print("Tecnicos");
                for i in tecnicos:
                    print("------------");
                    i.verTodo();
                    print("------------");

        #Listar Ordenes
        elif(opcion == 3):
            subListaOrdenes = ["Terminadas",
            "En espera de reparacion",
            "No Asignadas",
            "Volver"];
            opcion = menu(subListaOrdenes,"Listar Ordenes");
            if(opcion == 1):
                print("Ordenes Terminadas");
                for i in ordenes:
                    if(i.terminado):
                        print("------------------------");
                        i.imprimirOrden();
                        print("------------------------");
            elif(opcion == 2):
                print("Ordenes En espera de reparacion");
                for i in ordenes:
                    if(not i.terminado):
                        print("------------------------");
                        i.imprimirOrden();
                        print("------------------------");
            elif(opcion == 3):
                print("No Asignadas");
                for i in ordenes:
                    if(not i.asignada):
                        print("------------------------");
                        i.imprimirOrden();
                        print("------------------------");

    #Salir
    elif(opcion == 8):
        continuar = False;
        input("Fin del programa");

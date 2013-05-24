from datetime import*

#funciona de auto-menu
def menu(lista,nombre):
    opcion = '';
    #deducimos los valores que se pueden ingresar
    opcionesValidas = [];
    for i in range(len(lista)):
        opcionesValidas.append(i+1);
        
    while(not opcion in opcionesValidas):
                print("\n"+nombre);
                for i in range(len(lista)):
                        print(i+1," -> ",lista[i]);
                opcion = leerNumero("elija una opcion");
    return(opcion);

#resume un verdadero falso
def pregunta(cadena):
    continuar = str(input(cadena+"? S/N\n"));
    if(continuar == "s" or continuar == "S"):
        return(True);
    return(False);

#funciona de forma analoga al input()
#permite que solo se ingresen numeros o reales
def leerNumeroReal(cadena):
    cadena = cadena+": ";
    numeros = ["1","2","3","4","5","6","7","8","9","0"];
    continuar = True;#forzamos la entrada al bucle
    while(continuar):
        continuar = False;#habilitamos la salida del bucle
        decimalYaEscrito = False;#perminte poner punto solo una vez
        valor = str(input(cadena));#leemos el dato
        for i in valor:
            if(not i in numeros):#si no es un numero
                if(i == "." and not decimalYaEscrito):#si es un punto y aun nuo se lo escribio
                    decimalYaEscrito = True;#registra que el punto ya esta escrito
                else:
                    print("Debe ingrsesar solo numeros");
                    print("Y en su defecto un punto en lugar de coma");
                    continuar = True;
    return(float(valor));

#funciona de forma analoga al input()
#permite que solo se ingresen numeros
def leerNumero(cadena):
    cadena = cadena+": ";
    while(True):
        valor = str(input(cadena));
        if(str.isnumeric(valor)):
            return(int(valor));
        else:
            print("Debe ingrsesar solo numeros");

#te dice si una fecha es mayor, menor o igual que la actual
def comparar(fecha):
    if(datetime.now().year < fecha.year):
        return("mayor");#si el año es mayor la fecha es mayor
    elif(datetime.now().year > fecha.year):
        return("menor");#si el año es menor la fecha es menor
    elif(datetime.now().year == fecha.year):#si el año es igual comparamos los meses
        if(datetime.now().month < fecha.month):
            return("mayor");#si el mes es mayor la fecha es mayor
        elif(datetime.now().month > fecha.month):
            return("menor");#si el mes es menor la fecha es menor
        elif(datetime.now().month == fecha.month):#si el mes es igual comparamos los dias
            if(datetime.now().day > fecha.day):
                return("menor");#si el dia es menor la fecha es menor
            elif(datetime.now().day < fecha.day):
                return("mayor");#si el dia es mayor la fecha es mayor
            elif(datetime.now().day == fecha.day):
                return("igual");#si el dia igual la fecha es igual

#devuelve una fecha valida
def validarFecha():
    continuar = True;
    while(continuar):
        #el mes y el dia
        dia = leerNumero("Escriba el dia");
        mes = leerNumero("Escriba el mes");
        try:#intentamos
            d = datetime(datetime.now().year,mes,dia);#si la fecha esta mal, devuelve un error y salta al except:
            continuar = False;#si la fecha esta bien sale del bucle
        except:#si la fecha dio error
            input("Fecha Incorrecta");#presione enter para continuar...
    return(d);

def imprimirFechaOk(fecha):
    if(fecha.month == 1):
        mes='Enero'
    elif(fecha.month == 2):
        mes='Febrero'
    elif(fecha.month == 3):
        mes='Marzo'
    elif(fecha.month == 4):
        mes='Abril'
    elif(fecha.month == 5):
        mes='Mayo'
    elif(fecha.month == 6):
        mes='Junio'
    elif(fecha.month == 7):
        mes='Julio'
    elif(fecha.month == 8):
        mes='Agosto'
    elif(fecha.month == 9):
        mes='Septiembre'
    elif(fecha.month == 10):
        mes='Octubre'
    elif(fecha.month == 11):
        mes='Noviembre'
    else:
        mes='Diciembre'
    print('Dia: ',fecha.day,' /  Mes: ',mes,' /  Año: ',fecha.year)
    
    
    

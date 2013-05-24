from datetime import*
from Orden import*

class Tecnico:
	numero = 1;
	def __init__(self, nombre, apellido, fechaAlta, fechaBaja):
		self.nombre = nombre;
		self.apellido = apellido;
		self.fechaAlta = fechaAlta;
		self.fechaBaja = fechaBaja;
		self.numero = Tecnico.numero;
		Tecnico.numero += 1;
		self.ordenes = [];
	def modificarDatos(self):
		op=0
		while op!=5:
			print("\nModificar datos de Tecnico")
			print("1-Nombre")
			print("2-Apellido")
			print("3-Fecha de Alta")
			print("4-Fecha de Baja")
			print("5-Guardar Cambios");
			op=leerNumero("Seleccionar opciÃ³n:")
			if op==1:
				self.nombre = leerCadena("Escriba el nombre");
			elif op==2:
				self.apellido = leerCadena("Escriba el apellido");
			elif op==3:
				print("Definir la fecha de Alta");
				while(True):
					fechaAlta = validarFecha();
					if(comparar(fechaAlta) == "mayor"):#no se puede dar de alta en una fecha mayor
						print("La fecha es Incorrecta");
					else:
						break;
				self.fechaAlta = fechaAlta;
			elif op ==4:
				print("Definir la fecha de Baja");
				while(True):
					fechaBaja = validarFecha();
					if(comparar(fechaBaja) != "mayor"):#debe ser mayor, si o si
						print("La fecha es Incorrecta");
					else:
						break;
				self.fechaBaja = fechaBaja;
	def verTodo(self):
		print("Numero: ",self.numero);
		print("Nombre: ",self.nombre);
		print("Apellido: ",self.apellido);
		print("Fecha Baja");
		imprimirFechaOk(self.fechaBaja);
		print("Fecha Alta");
		imprimirFechaOk(self.fechaAlta);
		self.verOrdenes();
	def verOrdenes(self):
		if(len(self.ordenes) > 0):
			print("Ordenes");
			for i in self.ordenes:
				print("--------------");
				i.imprimirOrden();
				print("--------------");
		else:
			print("No tiene ordenes Cargadas");
	def desasignarOrden(self,numero):
		for i in range(len(self.ordenes)):
			if(self.ordenes[i].idn == numero):
				return(self.ordenes.pop(i));
				#nos sacamos la orden de encima y la devolvemos

#funciona de forma analoga al input()
#permite que solo se ingresen letras
def leerCadena(cadena):
	cadena = cadena+": ";
	while(True):
		valor = str(input(cadena));
		if(str.isalpha(valor)):
			return(valor);
		else:
			print("Debe ingrsesar solo letras");

#devuelve un cliente segun su DNI
#def existeCliente(DNI,clientes):
#	for i in clientes:
#		if(i.dni == DNI):
#			return(i);

#devuelve un tecnico segun su numero
def existeTecnico(lista,numero):
	for i in lista:
		if(i.numero == numero):
			return(i);

#lista los tecnicos y te permite elegir uno por su identificador
#al final devuelve el puntero del tecnico
def seleccionarTecnico(tecnicos):
	opcion = 0;
	listaPosible = []; #para seguridad de seleccion
	#elegimos el tecnico
	while(not opcion in listaPosible):
		print("\nTecnicos");
		for i in tecnicos:
			print(i.numero," ",i.nombre," ",i.apellido);
			listaPosible.append(i.numero);
		opcion = leerNumero("elija un tecnico: ");
	return(existeTecnico(tecnicos,opcion));

#pide los datos para cargar un tecnico
def nuevoTecnico(tecnicos):
	nombre = leerCadena("Escriba el nombre");
	apellido = leerCadena("Escriba el apellido");
	print("Definir la fecha de Alta");
	while(True):
		fechaAlta = validarFecha();
		if(comparar(fechaAlta) == "mayor"):#no se puede dar de alta en una fecha mayor
			print("La fecha es Incorrecta");
		else:
			break;

	print("Definir la fecha de Baja");
	while(True):
		fechaBaja = validarFecha();
		if(comparar(fechaBaja) != "mayor"):#debe ser mayor, si o si
			print("La fecha es Incorrecta");
		else:
			break;

	tecnicos.append(Tecnico(nombre,apellido,fechaAlta,fechaBaja));

#pide los datos para modificar un tecnico
def modificarTecnico(tecnicos):
	#elegimos tecnico
	t = seleccionarTecnico(tecnicos);
	#pedimos los nuevos datos
	t.modificarDatos();
	#mostramos sus datos
	print("----------");
	t.verTodo();
	print("----------");


#////////////////////
#////////MAIN////////
#////////////////////
#lista = [];
#nuevoTecnico(lista);
#print(lista);
#input();
#t = seleccionarTecnico(lista);
#t.verTodo();
#modificarTecnico(lista);


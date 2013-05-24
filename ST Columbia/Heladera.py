class Heladera:
	def __init__(self,orden,cliente,descripcion):
		self.orden = orden;
		self.cliente = cliente;
		self.reparada = False;
		self.codigo = orden.idn;
		self.descripcion = descripcion;
	def verTodo(self):
		print("Codigo: ",self.codigo);
		print("Cliente: ",self.cliente.nombre," ",self.cliente.apellido);
		print("DNI: ",self.cliente.dni);
		print("Descripcion:\n ",self.descripcion);
		if(self.reparada):
			print("Esta Heladera esta reparada");
		else:
			print("Esta Heladera aun no esta reparada");


#devuelve una heladera segun su numero
def existeHeladera(lista,numero):
	for i in lista:
		if(i.codigo == numero):
			return(i);

#lista las heladeras y te permite elegir una por su identificador
#al final devuelve el puntero de la heladera
def seleccionarHeladera(heladeras):
	opcion = 0;
	listaPosible = []; #para seguridad de seleccion
	#elegimos la heladera
	while(not opcion in listaPosible):
		print("\nHeladeras");
		for i in heladeras:
			print("Heladera ",i.codigo);
			listaPosible.append(i.codigo);
		opcion = leerNumero("elija una heladera: ");
	return(existeHeladera(heladeras,opcion));

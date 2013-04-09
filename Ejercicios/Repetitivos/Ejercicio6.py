suma=0
cont=0
ini=int(input('Ingrese el numero de inicio a calcular: '))
fin=int(input('Ingrese el numero que sera el limite a calcular: '))
while(fin>=ini):
    if((ini%2)==0):
        print('El numero ',ini,' es multiplo de 2')
        cont=cont+1
        suma=suma+ini
        ini=ini+1
    else:
        ini=ini+1
print('Hay ',cont,' numeros multiplo de 2, y que sumados entre si dan ',suma)

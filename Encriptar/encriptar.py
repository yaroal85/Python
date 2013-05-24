bandera = True
while bandera == True:
    clave = str(input('(Longitud mínima es de 6 caracteres)\nIngrese la contraseña que quiere encriptar: '))
    cEncriptada = ''
    ## Verifica si la longitud de la cadena es válida
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
        print(cEncriptada)
    continuar=str(input('Desea ingresar otra contraseña a encriptar? (S/N) '))
    if (continuar=="n" or continuar=="N"):
            bandera=False

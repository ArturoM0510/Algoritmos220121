def busquedaBinaria(lista,encontrar):
    '''busqueda binaria
        se ingresa una lista y un valor a encontrar y 
        se devuelve si lo encontro o no
    '''
    ItsInList = False
    lista.sort()
    izq= 0
    der= len(lista)-1
    while izq <= der and ItsInList==False:
        print(lista)
        medio= (izq+der)//2
        print('calculo medio', medio)
        print(f'Valor izquierda {izq}, valor medio {medio}, valor derecha {der}')
        if lista[medio] == encontrar:
            ItsInList= True
        elif lista[medio] > encontrar: 
            der = medio-1
        else: 
            izq= medio+1
    return ItsInList

lista = [2,12,34,5,11,59,4,3,1]
encontrar = int(input("Ingrese valor a buscar: "))
print (busquedaBinaria(lista, encontrar))
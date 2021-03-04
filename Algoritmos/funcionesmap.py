lista = [2,25,34,65,8]
potenciador = lambda valor = 0 : valor **2
listaCuadrados = list (map(potenciador, lista))
print(listaCuadrados)

n = 2
restarN = lambda valor = 0 : valor - n
restarNLista = list (map(restarN, lista))
print(restarNLista)
#normaizar
mayor = max(lista)
divM = lambda valor = 0 : valor/mayor
normalizar = list (map(divM, lista))
print(normalizar)
# funciones reduce
bases = [2,5,8,9]
from functools import reduce
sumarE = lambda acumulado = 0, elemento = 0 : acumulado+elemento
sumar = reduce(sumarE, bases)
print(sumar)
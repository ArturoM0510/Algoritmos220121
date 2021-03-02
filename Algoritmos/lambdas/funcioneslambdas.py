def linedesign (cantidad=60):
    print('#'*cantidad)

def sumar (a,b):
    suma = a+b
    return suma
def restar (a,b):
    restar = a-b
    return restar
def multiplicar (a,b):
    multiplicar = a*b
    return multiplicar
def dividir (a,b):
    dividir = a/b
    return dividir
def calculadora (funcion, a, b):
    return funcion(a,b)




linedesign()
print('hola a todos')
linedesign(20)
print(sumar(2,6))
linedesign(20)
print(restar(2,6))
linedesign(20)
print(multiplicar(2,6))
linedesign(20)
print(dividir(2,6))
linedesign(20)
print(calculadora(dividir, 2,6))

linedesignlambda = lambda cantidad=60 : print ('#'*cantidad)
linedesignlambda()
sumarL = lambda a=0 , b=0 : a+b
print(sumarL(2,3))
linedesignlambda()
restarL = lambda a=0, b=0 : a-b
print(restarL(2,3))
linedesignlambda()
multiplicarL =lambda a=0, b=0 : a*b
print(multiplicarL(2,3))
linedesignlambda()
dividirL = lambda a=0, b=0 :a/b
print(dividir(2,3))
linedesignlambda()

calculadoraL = lambda func= restarL ,a=0, b=0 : func(a,b)
print(calculadoraL(sumarL , 2,3))

listaEdades = [16,39,47,29]
listaEdades2 = [24,23,13,50]

lambdamaximos = lambda x = [], y = [] : print(max(x), max(y))
lambdamaximos(listaEdades, listaEdades2)

mayorEdad= lambda edad = 0 : edad>=18
print(mayorEdad(14))
print(mayorEdad(19))
mayores = list (filter(mayorEdad, listaEdades))
print(mayores)
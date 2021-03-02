import numpy as np
lista = [1, 2, 3, 4, 5]
listaC = []
for i in range(100, 800, 2):
    listaC.append(i)
# print(listaC)
# listaN = np.arange(200, 801, 2)
# print(listaN)
# listaN[::2] = 200
# print(listaN)

edades = [11, 34, 23, 56, 53, 28]
indedades = np.array(edades)
indedades1 = indedades >= 23
indedades2 = indedades <= 50
indedades3 = indedades1 & indedades2
# print(indedades3)
# print(np.sum(indedades3))
# print(np.mean(indedades))

mamas = [90, 74, 56, 39, 69, 50]
mamas = np.array(mamas)
hijosmay = indedades > 30
# print(mamas[hijosmay])
# print(mamas)
# print (np.mean(mamas[hijosMayores30]))
# print ('#'*30)
#Matriz Numpy
edadesHijos = np.array([14,18,22,24])
edadesMamas = np.array([45,54,67,74])
childrenMoms = np.array([edadesHijos,edadesMamas])
# print (childrenMoms)
# print ('#'*30)
#Transponer Matriz
indKids = childrenMoms[0] >= 18
# print (childrenMoms.transpose())
# print (np.sum(indKids))
# print ('#'*30)
# print (np.mean(childrenMoms[1][indKids])) 
# print (np.mean(childrenMoms[1][indKids]))
# print (len(childrenMoms[1][indKids])) 
#ordenando listas
listaEdades = [12,234,54,6,123,54]
# print(listaEdades)
listaEdadesNp = np.array(listaEdades)
listaEdadesNpOrd = np.sort(listaEdadesNp)
# print(listaEdadesNpOrd)
#Maximo y minimo
# print('maximo...',np.max(listaEdadesNp))
# print('minimo...',np.min(listaEdadesNp))
#mayores a 12
mayoresADoce = listaEdadesNp > 12
print (listaEdadesNp[mayoresADoce])
mayoresAOcho = np.where(listaEdadesNp>8)
print(mayoresADoce)
print(mayoresAOcho)
print (listaEdadesNp[mayoresAOcho[0]])
print(listaEdades)

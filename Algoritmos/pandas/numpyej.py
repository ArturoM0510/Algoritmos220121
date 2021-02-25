import numpy as np
lista = [1, 2, 3, 4, 5]
listaC = []
for i in range(100, 800, 2):
    listaC.append(i)
print(listaC)
listaN = np.arange(200, 801, 2)
print(listaN)
listaN[::2] = 200
print(listaN)

edades = [11, 34, 23, 56, 53, 28]
indedades = np.array(edades)
indedades1 = indedades >= 23
indedades2 = indedades <= 50
indedades3 = indedades1 & indedades2
print(indedades3)
print(np.sum(indedades3))
print(np.mean(indedades))

mamas = [90, 74, 56, 39, 69, 50]
mamas = np.array(mamas)
hijosmay = indedades > 30
print(mamas[hijosmay])

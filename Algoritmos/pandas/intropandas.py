import pandas as pd
listaVariada = ["a",1,2,3.4]
#print(listaVariada)
seriesPandas = pd.Series ([1,2,5])
#rint (seriesPandas)

dicGanancias = {}
dicGanancias ['Enero'] = 1923
dicGanancias ['Febrero'] = 1923
dicGanancias ['Marzo'] = 1923
dicGanancias ['Abril'] = 1923
seriesGananciaPorMes = pd.Series(dicGanancias)
#print (seriesGananciaPorMes)
#print (seriesGananciaPorMes['Enero':'Marzo'])

nombres = [['juan','karla'],['Arturo','laura']]
dataFrameNombres = pd.DataFrame(nombres)
#print(dataFrameNombres)

matrizEstudiantes = {
                        'Grupo1':['Karla', 'Mario', 'Laura'],
                        'Grupo2':['Santi', 'Arturo', 'Vale'],
                        'Grupo3':['Juan', 'Melany', 'Laura'],
                        'Grupo4':['Mafer', 'Esteban','Daniel'],
}
matrizEstudiantesDic = {
                        'Grupo1':['Karla', 'Mario', 'Laura'],
                        'Grupo2':['Santi', 'Arturo', 'Vale'],
                        'Grupo3':['Juan', 'Melany', 'Laura'],
                        'Grupo4':['Mafer', 'Esteban','Daniel'],
}
dataFrameNombres = pd.DataFrame(matrizEstudiantes)
dataFrameNombresDic = pd.DataFrame(matrizEstudiantesDic)
#print(dataFrameNombres)
# print(dataFrameNombresDic)
# print('#'*60)
# print(dataFrameNombresDic['Grupo2'])
# print('#'*60)
# print(dataFrameNombresDic.iloc[1:])

dicVentasPorMes = {
    'Enero (millones de pesos)' : [123,123,53454],
    'Febrero (millones de pesos)' :[293,929,9339],
    'Marzo (millones de pesos)' : [1838,484,93392]
}
dataFrameVentas = pd.DataFrame (dicVentasPorMes, index = ['Tomates','Yuca','Papa'])
# print(dataFrameVentas)
print (dataFrameVentas.iloc[:2])
print('#'*60)
print (dataFrameVentas.iloc[2])
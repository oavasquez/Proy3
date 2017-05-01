#np.savetxt("array.csv", imagenArreglo, delimiter=",",fmt='%s')

#from os import listdir
#from os.path import isfile, join
import os
import numpy as np

ruta_2048 = os.getcwd() + '/entrenamiento/2048/data/'

def todos_los_cvs(path_to_dir, suffix=".csv" ):
	archivos_csv = os.listdir(path_to_dir)
	return [ archivo for archivo in archivos_csv if archivo.endswith(suffix) ]

vectores_de_entrada = []
vectores_de_salida = []
vectores_del_tablero = []
vectores_de_movimientos = []
archivos_csv = todos_los_cvs(ruta_2048)
for archivos in archivos_csv:
	#print archivos
	vectores_de_entrada = np.genfromtxt(ruta_2048 + archivos, delimiter=',', dtype=int, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
	vectores_de_salida = np.genfromtxt(ruta_2048 + archivos, delimiter=',', dtype=int, usecols=(16, 17, 18, 19))
	for entrada in vectores_de_entrada:
		#print entrada
		vectores_del_tablero.append(entrada)
	for salida in vectores_de_salida:
		#print salida
		vectores_de_movimientos.append(salida)
print vectores_del_tablero
print vectores_de_movimientos

#np.savetxt("array.csv", imagenArreglo, delimiter=",",fmt='%s')


import numpy as np

vectores_de_entrada = np.genfromtxt('data.csv', delimiter=',', dtype=int, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
etiquetas = np.genfromtxt('data.csv', delimiter=',', dtype=int, usecols=(16, 17, 18, 19))
for x in etiquetas:
	print x 


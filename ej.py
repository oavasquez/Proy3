import Image
import numpy as np

#np.savetxt("array.csv", imagenArreglo, delimiter=",",fmt='%s')

vector_de_posiciones = [
	[492, 281], [601, 281], [711, 281], [820, 281],
	[492, 390], [601, 390], [711, 390], [820, 390],
	[492, 500],	[601, 500], [711, 500], [820, 500],
	[492, 609], [601, 609],	[711, 609],	[820, 609]
]

for posicion in vector_de_posiciones:
	print "x: " + str(posicion[0]) + "	y: " + str(posicion[1])
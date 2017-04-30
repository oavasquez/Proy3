import Image
import numpy as np

'''
	ESTA CLASE "MAPEADOR VECTORIAL" CONVIERTE LAS IMAGENES DE LOS TABLEROS
	DE LOS JUEGOS 2048 Y FLOOD-IT EN VECTORES
'''
class MapeadorVectorial:
	def __init__(self, imagen_arg):
		self.imagen = imagen_arg
		self.vector_de_posiciones = []
		self.vector_de_colores = []
		self.vector_de_numeros = []
		self.juego_2048 = False
		self.juego_flood_it = False
		self.colores_2048 = {	#UN MAPEO PARA LOS COLORES RGB DEL 2048
			(205, 193, 180): 0,
			(238, 228, 218): 2,
			(237, 224, 200): 4,
			(242, 177, 121): 8,
			(245, 149, 99): 16,
			(246, 124, 95): 32,
			(246, 94, 59): 64,
			(237, 207, 114): 128,
			(237, 204, 97): 256,
			(237, 200, 80): 512,
			(237, 197, 63): 1024,
			(237, 194, 46): 2048
		}
		self.colores_flood_it = { #UN MAPEO PARA LOS COLORES RGB DEL FLOOD-IT
			(255, 255, 0): 0, #'amarillo'
			(0, 255, 255): 1, #'cyan'
			(128, 0, 128): 2, #'morado'
			(255, 0, 0): 3, #'rojo'
			(255, 204, 102): 4, #'salmon'
			(0, 187, 0): 5, #'verde'
		}



	def definir_posiciones(self):
		if self.juego_2048:
			self.vector_de_posiciones = [
				[497, 286], [606, 286], [716, 286], [825, 286],
				[497, 395], [606, 395], [716, 395], [825, 395],
				[497, 505],	[606, 505], [716, 505], [825, 505],
				[497, 614], [606, 614],	[716, 614],	[825, 614]
			]
		elif self.juego_flood_it:
			y = 228
			for j in range(1, 14):
				y += 20
				x = 575
				for i in range(1, 14):
					x += 20
					self.vector_de_posiciones.append([x, y])


	def consultar_colores(self, imagen):
		self.definir_posiciones()
		self.vector_de_numeros = []
		self.imagen = imagen
		img = Image.open(self.imagen)
		img = img.convert('RGB')
		arreglo_imagen = np.array(img)
		if self.juego_2048:
			for posicion in self.vector_de_posiciones:
				self.vector_de_numeros.append(self.colores_2048[tuple(arreglo_imagen[posicion[1]][posicion[0]])])
			return self.vector_de_numeros
		elif self.juego_flood_it:
			for posicion in self.vector_de_posiciones:
				self.vector_de_numeros.append(self.colores_flood_it[tuple(arreglo_imagen[posicion[1]][posicion[0]])])
			return self.vector_de_numeros


	def primera_posicion(self):
		img = Image.open(self.imagen, mode='w')
		img = img.convert('RGB')
		arreglo_imagen = np.array(img)
		img.close()
		posicion = [0, 0]

		#ELEMENTO DEL ARREGLO
		bandera_posicion = False
		for y, columna in enumerate(arreglo_imagen):
			for x, fila in enumerate(columna):
				print "posicion  " + "x: " + str(x) + "  y: " + str(y)
				if np.array_equal(fila, [255, 204, 102]):
					bandera_posicion = True
					primera_posicion = [x, y]
					print primera_posicion
					break
				else:
					continue
			if(bandera_posicion):
				break
			else:
				continue
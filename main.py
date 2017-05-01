from sensores.CapturarPantalla import CapturarPantalla
from sensores.Leer import Leer
from sensores.MapeadorVectorial import MapeadorVectorial
from util.MinimizarVentanas import MinimizarVentanas
from redes_neuronales.Red2048 import Red2048
from efectores.Efectores import Efectores
import time
import numpy as np
import tensorflow as tf


def main():
	#INICIO DEL PROGRAMA
	minimizador = MinimizarVentanas()
	minimizador.minimizar()
	time.sleep(1)

	#USO DE LOS SENSORES
	capturador = CapturarPantalla()
	pantallazo = capturador.capturar_completa()

	#USO DE EFECTORES
	efector = Efectores()

	#IDENTIFICAR JUEGO
	leer = Leer(pantallazo)
	leer.obtener_imagen(pantallazo)
	leer.identificar_juego()

	mapeador = MapeadorVectorial(pantallazo)
	

	#DEFINIENDO LAS REDES NEURONALES
	rn2048 = Red2048()


	#ENTRENANDO LAS REDES NEURONALES
	vectores_de_entrada = np.genfromtxt('data.csv', delimiter=',', dtype=int, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
	etiquetas = np.genfromtxt('data.csv', delimiter=',', dtype=int, usecols=(16, 17, 18, 19))
	#for i in range(len(vectores_de_entrada)):
	#	rn2048.entrenar(vectores_de_entrada[i], etiquetas[i])
	#rn2048.entrenar(vectores_de_entrada, etiquetas)
	#print vectores_de_entrada




	'''
		******************************
		 PARTE PRINCIPAL DEL PROGRAMA
		******************************
	'''
	if leer.jugando2048:
		'''
			codigo para jugar 2048
		'''
		mapeador.juego_2048 = True
		bandera = 0
		while True:
			pantalla_2048 = capturador.capturar_completa()
			vector_de_entrada = []
			vector_tablero = mapeador.consultar_colores(pantalla_2048)
			vector_de_entrada.append(vector_tablero)
			movimiento = rn2048.predecir(vector_de_entrada)
			print movimiento
			efector.teclado(efector.teclas_2048[movimiento[0]])
			#time.sleep(1)
			bandera += 1
			if bandera > 35:
				break

	elif leer.jugandoFloodit:
		'''
			codigo para jugar flood it
		'''
		mapeador.juego_flood_it = True
		vector_de_entrada = mapeador.consultar_colores(pantallazo)
		bandera = 0
		while True:
			pantalla_2048 = capturador.capturar_completa()
			posiciones = mapeador.vector_de_posiciones
			vector_de_entrada = mapeador.consultar_colores(pantalla_2048)
			efector.clic(posiciones[bandera][0], posiciones[bandera][1])
			#time.sleep(1)
			bandera += 1
			if bandera > 483:
				break
	else:
		print "No se esta jugando nada"
		'''
			codigo en caso de no jugar
		'''



if __name__ == '__main__':
	main()
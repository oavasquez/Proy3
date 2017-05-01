from sensores.CapturarPantalla import CapturarPantalla
from sensores.Leer import Leer
from sensores.MapeadorVectorial import MapeadorVectorial
from util.MinimizarVentanas import MinimizarVentanas
from redes_neuronales.Red2048 import Red2048
from efectores.Efectores import Efectores
import time
import numpy as np
import tensorflow as tf
import os


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
	'''
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
	#print vectores_del_tablero
	#print vectores_de_movimientos
	print "Empezando a entrenar la Red Neuronal" 
	rn2048.entrenar(vectores_del_tablero, vectores_de_movimientos)
	'''


	#vectores_de_entrada = np.genfromtxt('data.csv', delimiter=',', dtype=int, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
	#etiquetas = np.genfromtxt('data.csv', delimiter=',', dtype=int, usecols=(16, 17, 18, 19))
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
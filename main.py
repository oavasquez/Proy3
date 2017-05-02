from sensores.CapturarPantalla import CapturarPantalla
from sensores.Leer import Leer
from sensores.MapeadorVectorial import MapeadorVectorial
from util.MinimizarVentanas import MinimizarVentanas
from redes_neuronales.Red2048 import Red2048
from redes_neuronales.RedFloodIt import RedFloodIt
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
	rn_2048 = Red2048()
	rn_flood_it = RedFloodIt()


	#ENTRENANDO LAS REDES NEURONALES
	''' RED DE 2048
	print "Empezando a entrenar la Red Neuronal de 2048"
	ruta_2048 = os.getcwd() + '/entrenamiento/2048/data/' 
	vctrs_del_tablero = rn_2048.vectores_del_tablero(ruta_2048)
	vctrs_de_movimientos = rn_2048.vectores_de_movimientos(ruta_2048)
	print len(vctrs_del_tablero)
	print len(vctrs_de_movimientos)
	#rn_2048.entrenar(vctrs_del_tablero, vctrs_de_movimientos)
	'''

	''' RED DE FLOOD-IT
	print "Empezando a entrenar la Red Neuronal de Flood-It"
	ruta_flood_it = os.getcwd() + '/entrenamiento/flood it 22x22-6/data/' 
	vctrs_del_tablero = rn_flood_it.vectores_del_tablero(ruta_flood_it)
	vctrs_de_colores = rn_flood_it.vectores_de_colores(ruta_flood_it)
	print len(vctrs_del_tablero)
	print len(vctrs_de_colores)
	#rn_flood_it.entrenar(vctrs_del_tablero, vctrs_de_colores)
	'''
	

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
			mapeador.definir_posiciones()
			vector_tablero = mapeador.consultar_colores(pantalla_2048)
			vector_de_entrada.append(vector_tablero)
			movimiento = rn2048.predecir(vector_de_entrada)
			print movimiento[0]
			efector.teclado(efector.teclas_2048[movimiento[0]])
			#time.sleep(1)
			bandera += 1
			if bandera > 50:
				break

	elif leer.jugandoFloodit:
		'''
			codigo para jugar flood it
		'''
		mapeador.juego_flood_it = True
		bandera = 0
		while True:
			pantalla_flood_it = capturador.capturar_completa()
			vector_de_entrada = []
			mapeador.definir_posiciones()
			vector_tablero = mapeador.consultar_colores(pantalla_flood_it)
			vector_de_entrada.append(vector_tablero)
			color = rn_flood_it.predecir(vector_de_entrada)
			print color[0]
			posicion = mapeador.coordenadas_de_color(color[0])
			efector.clic(posicion[0], posicion[1])
			#time.sleep(1)
			bandera += 1
			if bandera > 39:
				break
	else:
		print "No se esta jugando nada"
		'''
			codigo en caso de no jugar
		'''




if __name__ == '__main__':
	main()
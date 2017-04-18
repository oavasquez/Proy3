import Image
import numpy as np
import os
from sensores.CapturarPantalla import CapturarPantalla

class Leer_RGB():

	def __init__(self):
		pass

	def LeerImagen(self,ruta):
		img=Image.open(ruta)
		img = img.convert('RGB')
		arreglo = np.array(img)
		self.buscarJuego2(arreglo)
	
	#se le puede cambiar por BuscarBordeFlood_it
	def buscarJuego(self,arreglo):
		ArregloCantPixel=[]
		print  "tamano de pantalla en x:"+str(len(arreglo))
		print  "tamano de pantalla en y:"+str(len(arreglo[0]))

		#lo que se busca es la linea que tenga mas pixeles negros osea los bordes
		contadorPixel=0
		for x, fila in enumerate(arreglo):
			for y, columna in enumerate(fila):
				if np.array_equal(columna,[0,0,0]):
					contadorPixel=contadorPixel+1

			ArregloCantPixel.append([x,contadorPixel])
			contadorPixel=0

		#encontrar el maximo valor de pixeles negros 
		maxPixel=[]
		for x,contadorPixel in ArregloCantPixel:
			maxPixel.append(contadorPixel)



		maximoValor=max(maxPixel)
		print maximoValor
		maximoValorCont=0

		#luego buscamos de cuanto es el grosor de los bordes


		for elemento in maxPixel:
			if elemento==maximoValor:
				maximoValorCont=maximoValorCont+1
		print str(maximoValor)+": "+str(maximoValorCont)
		print "tamano del borde: "+str(maximoValorCont/2)

		#ademas buscamos cuales son los ejes en donde estan los bordes

		
		bordeDectectadoX=[]
		ejeX=[]
		
		for i in range(len(arreglo)):
			x,contadorPixel=ArregloCantPixel[i]
			if contadorPixel==maximoValor:
				bordeDectectadoX.append(arreglo[x])
				ejeX.append(x)
		

		ejeY=[]
		for y,columna in enumerate(bordeDectectadoX[0]):
				if np.array_equal(columna,[0,0,0]):
					ejeY.append(y)

		#recoremos el arreglo en donde todo lo que este dentro de los limites
		#osea los borde se agrege a un arreglo
		# 8 pixel es el tamano del borde 

		imagenArreglo=[]
		for fila in arreglo[range(ejeX[0]+8,ejeX[-1]-8)]:
			imagenArreglo.append(fila[range(ejeY[0]+8,ejeY[-1]-8)])

		#el arreglo se convierte en imagen para prueba de lo que contiene el arreglo

		arregloColor=[]
		for fila in imagenArreglo[20:40]:
					arregloColor.append(fila[0:20])

		print len(imagenArreglo),len(imagenArreglo[0])
		





		
		patron=np.array(arregloColor)
		imgPatron = Image.fromarray(patron.astype('uint8'))
		imgPatron.show()





	def buscarJuego2(self,arreglo):
		ArregloCantPixel=[]
		print  "tamano de pantalla en x:"+str(len(arreglo))
		print  "tamano de pantalla en y:"+str(len(arreglo[0]))

		#lo que se busca es la linea que tenga mas pixeles negros osea los bordes
		contadorPixel=0
		for x, fila in enumerate(arreglo):
			for y, columna in enumerate(fila):
				if np.array_equal(columna,[187,173,160]):
					contadorPixel=contadorPixel+1

			ArregloCantPixel.append([x,contadorPixel])
			contadorPixel=0
		

		
		#encontrar el maximo valor de pixeles negros 
		maxPixel=[]
		for x,contadorPixel in ArregloCantPixel:
			maxPixel.append(contadorPixel)



		maximoValor=max(maxPixel)
		print maximoValor
		maximoValorCont=0

		#luego buscamos de cuanto es el grosor de los bordes


		for elemento in maxPixel:
			if elemento==maximoValor:
				maximoValorCont=maximoValorCont+1
		print str(maximoValor)+": "+str(maximoValorCont)
		

		#ademas buscamos cuales son los ejes en donde estan los bordes

		
		bordeDectectadoX=[]
		ejeX=[]
		
		for i in range(len(arreglo)):
			x,contadorPixel=ArregloCantPixel[i]
			if contadorPixel==maximoValor:
				bordeDectectadoX.append(arreglo[x])
				ejeX.append(x)
		

		ejeY=[]
		for y,columna in enumerate(bordeDectectadoX[0]):
				if np.array_equal(columna,[187,173,160]):
					ejeY.append(y)

		#recoremos el arreglo en donde todo lo que este dentro de los limites
		#osea los borde se agrege a un arreglo

		imagenArreglo=[]
		for fila in arreglo[range(ejeX[0],ejeX[-1])]:
			imagenArreglo.append(fila[range(ejeY[0],ejeY[-1])])

		#el arreglo se convierte en imagen para prueba de lo que contiene el arreglo 

		

		arregloNumero=[]
		arregloContenedorNum=[]
		contaf=40
		contbf=100
		contac=40
		contbc=100

		for i in range(4):
			for j in range(4):
				for fila in imagenArreglo[contaf:contbf]:
					arregloNumero.append(fila[contac:contbc])
				contac=contac+100
				contbc=contbc+100
				arregloContenedorNum.append([arregloNumero[:]])
				del arregloNumero[:]
			contaf=contaf+100
			contbf=contbf+100
			contac=40
			contbc=100


		mostrarNumero=[]
		for arregloNum in arregloContenedorNum:
			mostrarNumero.append(self.BuscarNumero(arregloNum))
		print mostrarNumero
		#print arregloContenedorNum[1]
		
		patron=np.array(imagenArreglo)
		imgPatron = Image.fromarray(patron.astype('uint8'))
		imgPatron.show()
		
		

	


	def BuscarNumero(self,arregloNumero):
		valor=1

		for fila in arregloNumero[0]:
			for columna in fila:
				if np.array_equal(columna,[205, 193, 180]):#0
					valor=0
					break
				if np.array_equal(columna,[238,228,218]):#2
					valor=2
					break
				if np.array_equal(columna,[237,224,200]):#4
					valor=4
					break
				if np.array_equal(columna,[242,177,121]):#8
					valor=8
					break
				if np.array_equal(columna,[245,149,99]):#16
					valor=16
					break
				if np.array_equal(columna,[246,124,95]):#32
					valor=32
					break
				if np.array_equal(columna,[246,94,59]):#64
					valor=64
					break
				if np.array_equal(columna,[237,207,114]):#128
					valor=128
					break
				if np.array_equal(columna,[237,204,97]):#256
					valor=256
					break
				if np.array_equal(columna,[237,200,80]):#512
					valor=512
					break
				if np.array_equal(columna,[237,197,63]):#1024
					valor=1024
					break
				if np.array_equal(columna,[237,194,46]):#2048
					valor=2048
					break
			if not valor==1:
				break
		return valor




		



		

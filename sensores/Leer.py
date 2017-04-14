from PIL import Image,ImageFilter
import numpy


import os

import ImageChops
import math, operator
from util.notificacion import notificacion

class Leer:
	def __init__(self,ruta):
		self.patronn=[]
		self.errfloodit=0
		self.err2048=0
		self.ruta=ruta
		self.jugando2048=False
		self.jugandoFloodit=False
		self.nt=notificacion()


	def identificar_juego(self):
		
		imgActual=self.obtener_imagen(self.ruta)
		img2048=self.obtener_imagen(os.getcwd()+"/util/Capturas/2048/2048.png")
		imgFloofit=self.obtener_imagen(os.getcwd()+"/util/Capturas/floodit/floodit.png")

		self.err2048=self.calcular_RMS(imgActual,img2048)
		self.errfloodit=self.calcular_RMS(imgActual,imgFloofit)

		imagencomb=ImageChops.multiply(img2048, imgFloofit)
	
		errcomb=self.calcular_RMS(imgActual,imagencomb)
		


		if self.err2048<60 or self.errfloodit<60:
			if self.err2048<self.errfloodit:
				self.nt.mirando("2048")
				self.jugando2048=True
			elif self.errfloodit<self.err2048:
				self.nt.mirando("Floot-It")
				self.jugandoFloodit=True
		else:
			self.nt.no_mirando()

	
	def obtener_imagen(sef,ruta):
		imageFile = Image.open(ruta).convert(mode='L', dither=3)
		imageSize = imageFile.size
		rawData = imageFile.tobytes('raw')
		img = Image.frombytes('L', imageSize, rawData)
		#numpy.savetxt(os.getcwd()+"/util/Capturas/array.csv", img, delimiter=",",fmt='%s')

		return img

	def calcular_RMS(self,img1,img2):
		h = ImageChops.difference(img1, img2).histogram()
		rms=math.sqrt(reduce(operator.add, map(lambda h, i: h*(i**2), h, range(256))) / (float(img1.size[0]) * img1.size[1]))
		return rms

	def estado_juego(self):

		if self.jugandoFloodit:
			imgGameOver=self.obtener_imagen(os.getcwd()+"/util/Capturas/floodit/gameOver.png")
			imgContinuar=self.obtener_imagen(os.getcwd()+"/util/Capturas/floodit/continuar.png")
			imgActual=self.obtener_imagen(self.ruta)

			imgActual=self.transformar_bn_floodit(imgActual)
		

			errorGameOver=self.calcular_RMS(imgGameOver,imgActual)
			errorContinuar=self.calcular_RMS(imgContinuar,imgActual)

			

			if errorContinuar>8:
					print "el juego a terminado en floodit"
					self.nt.juego_terminado()

			

		if self.jugando2048:
			imgGameOver=self.obtener_imagen(os.getcwd()+"/util/Capturas/2048/gameOver.png")
			imgContinuar=self.obtener_imagen(os.getcwd()+"/util/Capturas/2048/continuar.png")
		
			imgActual=self.obtener_imagen(self.ruta)

			imgActual=self.transformar_bn_2048(imgActual)

			
			errorGameOver=self.calcular_RMS(imgGameOver,imgActual)
			errorContinuar=self.calcular_RMS(imgContinuar,imgActual)

			
			

			if errorGameOver<50:
					print "el juego a terminado en 2048"
					self.nt.juego_terminado()


	def arreglo_image(self):
		imgActual=self.obtener_imagen(self.ruta)
		patron = numpy.asarray(imgActual, dtype="float") 

		
	

		for i in range(len(patron)):
			for j in range(len(patron[0])):
				if patron[i][j]==0.0:
					patron[i][j] = 0.0
				else:
					patron[i][j] = 255.0
		

		imgPatron = Image.fromarray(patron)
		imgPatron.show()

	def transformar_bn_2048(self,img):
		patron = numpy.asarray(img, dtype="float") 
		for i in range(len(patron)):
			for j in range(len(patron[0])):
				if patron[i][j]==175: 
					patron[i][j] = 0.0
				else:
					patron[i][j] = 255.0
		

		imgPatron = Image.fromarray(patron.astype('uint8'))
		return imgPatron

	def transformar_bn_floodit(self,img):
		patron = numpy.asarray(img, dtype="float") 
		for i in range(len(patron)):
			for j in range(len(patron[0])):
				if patron[i][j]==0.0: 
					patron[i][j] = 0.0
				else:
					patron[i][j] = 255.0
		

		imgPatron = Image.fromarray(patron.astype('uint8'))
		return imgPatron



























		


		
		



				



		

		 
		
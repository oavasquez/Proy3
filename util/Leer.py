from PIL import Image,ImageFilter
import numpy
import os

import ImageChops
import math, operator

class Leer:
	def __init__(self,ruta):
		self.patronn=[]
		self.errfloodit=0
		self.err2048=0
		self.ruta=ruta


	def identificarJuego(self):
		
		imgActual=self.obtenerImagen(self.ruta)
		img2048=self.obtenerImagen(os.getcwd()+"/util/Capturas/2048/2048.png")
		imgFloofit=self.obtenerImagen(os.getcwd()+"/util/Capturas/floodit/floodit.png")

		self.err2048=self.calcularRMS(imgActual,img2048)
		self.errfloodit=self.calcularRMS(imgActual,imgFloofit)

		imagencomb=ImageChops.multiply(img2048, imgFloofit)
	
		errcomb=self.calcularRMS(imgActual,imagencomb)


		if errcomb>(self.err2048+self.errfloodit)/2:
			if self.err2048<self.errfloodit:
				print "El juego es 2048"
			elif self.errfloodit<self.err2048:
				print "el juego es flood-it"
		else:
			print "No se reconoce ningun juego"


		

	def obtenerImagen(self,ruta):
		imageFile = Image.open(ruta).convert(mode='L', dither=3)
		imageSize = imageFile.size
		rawData = imageFile.tobytes('raw')
		img = Image.frombytes('L', imageSize, rawData)
		return img

	def calcularRMS(self,img1,img2):
		h = ImageChops.difference(img1, img2).histogram()
		rms=math.sqrt(reduce(operator.add, map(lambda h, i: h*(i**2), h, range(256))) / (float(img1.size[0]) * img1.size[1]))
		return rms

	def estadoJuego(self):
		imgGameOver=self.obtenerImagen(os.getcwd()+"/util/Capturas/2048/gameOver.png")
		imgActual=self.obtenerImagen(self.ruta)
		
		errorGameOver=self.calcularRMS(imgGameOver,imgActual)

		if errorGameOver<self.errfloodit:
				print "el juego a terminado"

		print errorGameOver,self.errfloodit

	def arregloImage(self):
		imgActual=self.obtenerImagen(self.ruta)
		patron = numpy.asarray(imgActual, dtype="float") 
		



























		


		
		



				



		

		 
		
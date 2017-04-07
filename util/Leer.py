from PIL import Image,ImageFilter
import numpy
import os
class Leer:
	def __init__(self):
		self.patron=[]

	
	
	def leerImagen(self,ruta):
		imageFile = Image.open(ruta).convert(mode='L', dither=3)
		imageSize = imageFile.size
		rawData = imageFile.tobytes('raw')
		img = Image.frombytes('L', imageSize, rawData)
		self.patron = numpy.asarray(img, dtype=numpy.uint8) 
		print self.patron
		
		#numpy.savetxt(os.getcwd()+"/util/Capturas/array.csv", patron, delimiter=",",fmt='%s')

	def comparar(self):
		array=[]
		array=numpy.genfromtxt(os.getcwd()+"/util/Capturas/array.csv", delimiter=',')
		 
		print numpy.sum(array.astype(int)==self.patron)

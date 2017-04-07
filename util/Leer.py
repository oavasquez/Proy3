from PIL import Image,ImageFilter
import numpy


class Leer:
	def __init__(self):
		pass
	
	def leer_imagen(sef,ruta):
		imageFile = Image.open(ruta).convert(mode='L', dither=3)
		imageSize = imageFile.size
		rawData = imageFile.tobytes('raw')
		img = Image.frombytes('L', imageSize, rawData)
		patron = numpy.asarray(img, dtype="float") #.__xor__(1)

		print patron 

		
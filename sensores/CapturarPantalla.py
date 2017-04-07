import pyscreenshot as ImageGrab
import os

class CapturarPantalla:
	def __init__(self):
		pass
		

	def capturar_completa(self):
		imagen = ImageGrab.grab()
		imagen.save(os.getcwd() + '/util/Capturas/im.png')
		return os.getcwd() + '/util/Capturas/im.png'	
	

	def capturar_reducida(self, x, y, height, width):
		imagen = ImageGrab.grab(bbox=(x, y, height, width))
		imagen.save(os.getcwd() + '/Capturas/imreducida.png')
	




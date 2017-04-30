import pyscreenshot as ImageGrab
import os

class CapturarPantalla:
	def __init__(self):
		pass
		

	def capturar_completa(self):
		imagen = ImageGrab.grab(childprocess=None)
		imagen.save(os.getcwd() + '/util/Capturas/im.png', format='PNG')
		imagen.close()
		return os.getcwd() + '/util/Capturas/im.png'	
	

	def capturar_reducida(self, x, y, height, width):
		imagen = ImageGrab.grab(bbox=(x, y, height, width), childprocess=None)
		imagen.save(os.getcwd() + '/util/Capturas/im_reducida.png', format='PNG')
		imagen.close()

	




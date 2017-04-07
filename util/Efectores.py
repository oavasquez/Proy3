from pymouse import PyMouse
from pykeyboard import PyKeyboard

class Efectores:
	def __init__(self):
		pass

	def clic(self, arreglo_clic):
		mouse = PyMouse()
		for posicion_x,posicion_y in arreglo_clic:
			mouse.click(posicion_x, posicion_y, 1)
			#El numero (tercer argumento) significa el tipo de clic, 1 clic izquierdo y 2 clic derecho
		
	def teclado(self, tecla):
		key = PyKeyboard()
		key.press_key(tecla)
		key.release_key(tecla)
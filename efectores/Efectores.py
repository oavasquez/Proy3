from pymouse import PyMouse
from pykeyboard import PyKeyboard

class Efectores:
	def __init__(self):
		self.tecla = PyKeyboard()
		self.raton = PyMouse()

	def clic(self, posicion_x, posicion_y): 
		#El numero (tercer argumento) significa el tipo de clic, 1 clic izquierdo y 2 clic derecho
		self.raton.click(posicion_x, posicion_y, 1)
			
		
	def teclado(self, tecla):
		self.tecla.press_key(tecla)
		self.tecla.release_key(tecla)
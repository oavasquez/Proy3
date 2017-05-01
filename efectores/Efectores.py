from pymouse import PyMouse
from pykeyboard import PyKeyboard

class Efectores:
	def __init__(self):
		self.tecla = PyKeyboard()
		self.raton = PyMouse()
		self.teclas_2048 = {
			0: self.tecla.up_key,
			1: self.tecla.right_key,
			2: self.tecla.down_key,
			3: self.tecla.left_key
		}

	def clic(self, posicion_x, posicion_y): 
		#El numero (tercer argumento) significa el tipo de clic, 1 clic izquierdo y 2 clic derecho
		self.raton.click(posicion_x, posicion_y, 1)
			
		
	def teclado(self, tecla):
		self.tecla.press_key(tecla)
		self.tecla.release_key(tecla)
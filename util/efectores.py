from pymouse import PyMouse
from pykeyboard import PyKeyboard

class efectores:

	def clic(self,posicion_x,posicion_y):
		mouse = PyMouse()
		mouse.click(posicion_x,posicion_y,1)#el numero significa el tipo de clic, 1 clic izquierdo y 2 clic derecho
		
	def teclado(self,tecla):
		key = PyKeyboard()
		key.press_key(tecla)
		key.release_key(tecla)
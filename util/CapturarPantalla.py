import pyscreenshot as ImageGrab
import os
##install pyscreenshot

class CapturarPantalla:
	def __init__(self):
		va=0
		

	def capturarFullSize(self):
		im=ImageGrab.grab()
		im.save( os.getcwd()+'/util/Capturas/im.png')
		return os.getcwd()+'/util/Capturas/im.png'	
	

	def capturarReducida(self,x,y,height,width,):
		im=ImageGrab.grab(bbox=(x,y,height,width))
		im.save( os.getcwd()+'/Capturas/imreducida.png')
	




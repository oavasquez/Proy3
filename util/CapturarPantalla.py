import pyscreenshot as ImageGrab
##install pyscreenshot

class CapturarImagen:
	def __init__(self):
		va=0
		

	def capturarFullSize(self):
		im=ImageGrab.grab()
		im.save('im.png')

	def capturarReducida(self,x,y,height,width,):
		im=ImageGrab.grab(bbox=(x,y,height,width))
		im.save('imreducida.png')


if __name__=="__main__":
	ci=CapturarImagen()
	ci.capturarFullSize()
	ci.capturarReducida(10,10,500,500)
from sensores.CapturarPantalla import CapturarPantalla
from sensores.Leer import Leer


def main():

	ci=CapturarPantalla()
	ruta=ci.capturar_completa()

	leer=Leer(ruta)
	leer.identificarJuego()
	leer.arregloImage()

if __name__ == '__main__':
	main()


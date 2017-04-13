from sensores.CapturarPantalla import CapturarPantalla
from sensores.Leer import Leer
from util.minimizarVentanas import minimizarVentanas
import time


def main():
	mv=minimizarVentanas()
	mv.minimizar()
	time.sleep(2)
	ci=CapturarPantalla()
	ruta=ci.capturar_completa()

	leer=Leer(ruta)
	leer.identificar_juego()
	leer.estado_juego()

if __name__ == '__main__':
	main()


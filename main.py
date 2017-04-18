from sensores.CapturarPantalla import CapturarPantalla
from sensores.Leer import Leer
from sensores.Leer_RGB import Leer_RGB
from util.minimizarVentanas import minimizarVentanas
import time


def main():
	mv=minimizarVentanas()
	mv.minimizar()
	time.sleep(2)
	ci=CapturarPantalla()
	ruta=ci.capturar_completa()
	leer=Leer_RGB()
	leer.LeerImagen(ruta)

	#leer=Leer(ruta)
	#leer.obtener_imagen(ruta)
	#leer.identificar_juego()
	#leer.estado_juego()

if __name__ == '__main__':
	main()


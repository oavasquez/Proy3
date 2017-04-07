from sensores.CapturarPantalla import CapturarPantalla
from sensores.Leer import Leer


def main():
	capturador = CapturarPantalla()
	ruta = capturador.capturar_completa()

	lector = Leer()
	lector.leer_imagen(ruta)


if __name__ == '__main__':
	main()